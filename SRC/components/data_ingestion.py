import os
import sys
from SRC.exception import CustomException
from SRC.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from SRC.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Above mentioned path will be saved in this ingestion_config after calling

    def initiate_data_ingestion(self):
         '''
         If the data is stored in some databases, the code below will read from databases.
         '''
         logging.info("Entered the data ingestion method or component")

         try:
            # reading the data from directiory
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe in DataIngestion')

            '''
            This code creates a directory (or multiple directories) for storing training data used in some ingestion process.
            os.makedirs is a method from the os module in Python that creates a directory recursively. 
            It creates all directories specified in the input path, even if the intermediate directories do not exist.
            The os.path.dirname() method returns the directory name from a path string. In this case, it returns the parent directory of self.ingestion_config.train_data_path.
            By passing the directory name returned by os.path.dirname() as an argument to os.makedirs(), the code creates the parent directory of the train_data_path if it does not already exist.
            The exist_ok=True argument tells os.makedirs() to not raise an error if the directory already exists.
            In summary, this code creates the parent directory for the train_data_path specified in self.ingestion_config, or does nothing if the directory already exists.
            '''
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # Docstring for this line of code

            # Converting data to csv file
            df.to_csv(self.ingestion_config.raw_data_path, index =False, header = True)

            logging.info('Train Test Split initiated')
            # Performing train-test-split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving train & test files to csv to train and test path
            train_set.to_csv(self.ingestion_config.train_data_path, index =False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index =False, header = True)

            logging.info('Ingestion of the data is completed!')

            # returning train-test data paths
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
         
         except Exception as e:
             raise CustomException(e, sys)
         

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)