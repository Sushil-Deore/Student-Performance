import os
import sys
import pandas as pd
from SRC.exception import CustomException
from SRC.utils import load_object
from SRC.logger import logging

class PredictPipleine:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            logging.info("Defining Pickle File path for model")
            model_path = os.path.join('artifacts\model.pkl')

            logging.info("Defining Pickle File path for Preprocessor")
            preprocessor_path = os.path.join('artifacts\preprocessor.pkl')

            logging.info("Loading model from model Path")
            model = load_object(file_path = model_path)

            logging.info("Loading preprocessor object from Preprocessor path")
            preprocessor = load_object(file_path = preprocessor_path)
            
            logging.info("Transforming data using Preprocessor")
            data_scaled = preprocessor.transform(features)

            logging.info("Predicting data using Model")
            preds = model.predict(data_scaled)

            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    """
    Responsible for mapping all the inputs that are given in the HTML to the BackEnd with Particular values
    """

    def __init__(self, 
                 gender:str, 
                 race_ethnicity: str, 
                 parental_level_of_education, 
                 lunch: str, 
                 test_preparation_course: str, 
                 reading_score: int, 
                 writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {"gender" : [self.gender],
                                      "race_ethnicity" : [self.race_ethnicity], 
                                      "parental_level_of_education" : [self.parental_level_of_education],
                                      "lunch" : [self.lunch],
                                      "test_preparation_course": [self.test_preparation_course],
                                      "reading_score" : [self.reading_score], 
                                      "writing_score" : [self.writing_score]}
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)