import os
import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import Custom_Exception
from src.logger import logging
from src.components.data_transform import DataTransformation
from src.components.data_transform import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion process.")
        try:
            df = pd.read_csv("/Users/anand/Desktop/mlProject/Notebook/data/stud.csv")
            logging.info("Dataset loaded successfully.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Splitting dataset into train and test sets.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion process completed successfully.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise Custom_Exception(e, sys)

if __name__ == "__main__":
    try:
        ingestion = DataIngestion()
        train_data, test_data = ingestion.initiate_data_ingestion()

        transformation = DataTransformation()
        transformation.initiate_data_transformation(train_data, test_data)

    except Exception as e:
        logging.error(f"Error in main: {e}")
