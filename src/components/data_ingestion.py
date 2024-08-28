import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data Ingestion Component")
        try:
            data_path = os.path.join('notebooks', 'data', 'Flight-Price.xlsx')
            df = pd.read_excel(data_path) # Dataset Loading from the source
            logging.info("Read Dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Making some necessary changes for this dataset only :)
            df = df.dropna()
            df[['Date_of_Journey']] = df[['Date_of_Journey']].apply(pd.to_datetime)
            df['day'] = df['Date_of_Journey'].dt.day.astype(int)
            df['month'] = df['Date_of_Journey'].dt.month.astype(int)
            df['Duration_min'] = df['Duration'].str.extract('(\d+)h').fillna(0).astype(int) * 60 + df['Duration'].str.extract('(\d+)m').fillna(0).astype(int)
            stops = {
                'non-stop': 0,
                '1 stop': 1,
                '2 stops': 2,
                '3 stops': 3,
                '4 stops': 4
            }

            df['Total_Stops'] = df['Total_Stops'].map(stops)

            df = df.drop(columns=['Date_of_Journey', 'Dep_Time', 'Arrival_Time', 'Duration', 'Route', 'Unnamed: 0'])
            
            
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Split Dataset into Train and Test")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Ingestion Complete")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path


        except Exception as e:
            logging.error("Error in Data Ingestion Component")
            raise CustomException(e, sys)
        
