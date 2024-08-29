import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join('artifacts', 'preprocessor.joblib')

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_transformation_obj(self):
        try:

            
            cat_cols = ['Source', 'Destination', 'Airline', 'Additional_Info']
            num_cols = ['Total_Stops', 'day', 'month', 'Duration_min']

            num_pipeline = Pipeline(steps=[
                ('scaler', StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ('label_encoder', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, num_cols),
                ('cat_pipeline', cat_pipeline, cat_cols)
            ])

            logging.info('Preprocessing Pipeline Created')

            return preprocessor
        
        except Exception as e:
            logging.error("Error in getting transformation object")
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_data_path, test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Read Train & Test Data')

            preprocessing_obj = self.get_transformation_obj()
            target_col = 'Price'

            input_feature_train_df = train_df.drop(columns=[target_col], axis=1)
            target_feature_train_df = train_df[target_col]
            input_feature_test_df = test_df.drop(columns=[target_col], axis=1)
            target_feature_test_df = test_df[target_col]

            logging.info('Applying Preprocessing object....')
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr.toarray(), target_feature_train_df.values.reshape(-1, 1)]
            test_arr = np.c_[input_feature_test_arr.toarray(), target_feature_test_df.values.reshape(-1, 1)]
            save_object(
                file_path=self.transformation_config.preprocessor_obj_path,
                obj=preprocessing_obj
            )

            logging.info('Data Transformation Complete.')

            return (
                train_arr, test_arr, self.transformation_config.preprocessor_obj_path
            )

        except Exception as e:
            logging.error("Error in Data Transformation Component")
            raise CustomException(e, sys)