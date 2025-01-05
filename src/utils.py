import os
import sys
import dill
from sklearn.metrics import r2_score
from src.exception import Custom_Exception
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
    except Exception as e:
        raise Custom_Exception(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate R2 scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Log the model performance (optional)
            print(f"Model: {model_name} - Train R2: {train_model_score}, Test R2: {test_model_score}")

            # Store the test model score in the report
            report[model_name] = test_model_score
        
        return report
    
    except Exception as e:
        raise Custom_Exception(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise Custom_Exception(e, sys)
