import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join('artifacts', 'model.joblib')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Spliting training and testing input data for model training")
            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]
            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]
            logging.info("Data Splitting Done")
            
            # Now, the model training part.

            models = {
                'RandomForestRegressor': RandomForestRegressor(),
                'GradientBoostingRegressor': GradientBoostingRegressor(),
                'XGBRegressor': XGBRegressor()
            }

            params = {
                'RandomForestRegressor': {
                    'n_estimators': [500, 1000],
                    'max_depth': [9, 7]
                },
                'GradientBoostingRegressor': {
                    'n_estimators': [1000, 500],
                    'learning_rate': [0.2, 0.5]
                },
                'XGBRegressor': {
                    'gamma': [0.1, 0.3],
                    'max_depth': [3, 5],
                    'learning_rate': [0.3, 0.5],
                    'min_child_weight' : [3, 7]
                }
            }
            model_report: dict = evaluate_models(
                X_train, y_train, X_test, y_test, models, params
            )
            logging.info("Model evaluation done")
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            if best_model_score < 0.6:
                logging.error("Best model score is less than 0.6, hence not saving the model")
                raise CustomException("No best model found")
            save_object(self.model_trainer_config.trained_model_path, best_model)
            return best_model_name, best_model_score


        except Exception as e:
            logging.error("Error in model trainer component")
            raise CustomException(e, sys)