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
from sklearn.preprocessing import StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join('artifacts', 'preprocessor.joblib')

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_transformation_obj(self):
        try:
            pass
        
        except Exception as e:
            logging.error("Error in getting transformation object")
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_data_path, test_data_path):
        try:
            pass

        except Exception as e:
            logging.error("Error in Data Transformation Component")
            raise CustomException(e, sys)