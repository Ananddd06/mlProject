import os 
import sys
import dill

from src.exception import Custom_Exception

def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok= True)
        with open(file_path , 'wb') as file:
            dill.dump(obj , file)
    except Exception as e:
        raise Custom_Exception(e , sys)
