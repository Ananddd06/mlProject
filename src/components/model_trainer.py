import os
import sys
from dataclasses import dataclass

from src.utils import save_object, evaluate_model
from src.logger import logging
from src.exception import Custom_Exception

from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig():
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array, preprocessor_path=None):
        try:
            logging.info("Splitting the train and test datasets")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            
            # Define the models
            models = {
                "LinearRegression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            logging.info("Evaluating models")
            
            # Use evaluate_model from utils
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)

            # Get the best model score
            best_model_score = max(model_report.values())  # No need for sorting
            best_model_name = max(model_report, key=model_report.get)  # Get model name directly

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise Custom_Exception("No best model found with sufficient score")

            logging.info(f"Best model: {best_model_name} with score: {best_model_score}")

            # Ensure the directory exists for saving the model
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Make predictions and calculate R2 score
            predicted = best_model.predict(X_test)
            logging.info(f"Predicted values are: {predicted[:10]}...")  # Print only the first 10 for brevity

            r2_square = r2_score(y_test, predicted)
            logging.info(f"R-squared score: {r2_square}")

            # Return the r2_score so you can also see it in your main script
            return r2_square

        except Exception as e:
            raise Custom_Exception(e, sys)
