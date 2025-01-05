import sys
import os
import pandas as pd
import numpy as np
from src.exception import Custom_Exception
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise Custom_Exception(e, sys)

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,  # Renamed from race/ethnicity
                 parental_level_of_education: str,  # Renamed from parental level of education
                 lunch: str,
                 test_preparation_course: str,  # Renamed from test preparation course
                 reading_score: int,  # Renamed from reading score
                 writing_score: int):  # Renamed from writing score

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],  # Corrected variable name
                "parental level of education": [self.parental_level_of_education],  # Corrected variable name
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],  # Corrected variable name
                "reading score": [self.reading_score],  # Corrected variable name
                "writing score": [self.writing_score],  # Corrected variable name
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise Custom_Exception(e, sys)
