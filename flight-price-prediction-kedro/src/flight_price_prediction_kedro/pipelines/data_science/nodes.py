"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.9
"""

import logging
import typing as t
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def split_data(data: pd.DataFrame, parameters: dict) -> t.Tuple:
    X =  data.drop(columns="price")
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=parameters["test_size"])
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series, parameters: dict) -> RandomForestRegressor:
    model = RandomForestRegressor(random_state=parameters["random_state"])
    model.fit(X_train, y_train)
    return model

def evaluate_model(X_test: pd.DataFrame, y_test: pd.DataFrame, model: RandomForestRegressor) -> None:
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    
    logger = logging.getLogger(__name__)
    logger.info(f"R2_score: {score}")
    