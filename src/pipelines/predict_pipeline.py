import sys
import os
from src.exception import CustomException
from src.utils import load_object

import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features):
        try:
            model_path = os.path.join('artifacts', 'model.joblib')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.joblib')
            print('Artifacts Loading..........')
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            print('After Loading..........')
            features_preprocessed = preprocessor.transform(features)
            prediction = model.predict(features_preprocessed)
            print('Flight Fare Predicted: ', prediction)
            return prediction
        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:
    def __init__():
        pass

    def get_data_as_df(self):
        try:
            input_dict = {
                
            }
            return pd.DataFrame(input_dict)
        except Exception as e:
            raise CustomException(e, sys)