"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.9
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder


def delete_outlier_values(data: pd.DataFrame) -> pd.DataFrame:
    data = data[data["price"] <= 100000]
    return data

def create_num_cat(data: pd.DataFrame):
    data_cols = ["airline", "source_city", "departure_time", "stops", "arrival_time",
             "destination_city", "class", "duration", "days_left"]
    target_cols = "price"

    final_data = data[data_cols].copy()
    final_target = data[target_cols]
    
    numerical_columns = data[data_cols].select_dtypes(include=np.number).columns.tolist()
    categorical_columns = data[data_cols].select_dtypes(include="object").columns.tolist()
    
    return numerical_columns, categorical_columns

def encoder(data: pd.DataFrame, categorical_columns: list):
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    encoder.fit(data[categorical_columns])
    encoder_columns = encoder.get_feature_names_out(categorical_columns)
    data[encoder_columns] = encoder.transform(data[categorical_columns])
    return data, encoder_columns

def scalar(data: pd.DataFrame, numerical_columns: list):
    scalar = MinMaxScaler()
    scalar.fit(data[numerical_columns])
    data[numerical_columns] = scalar.transform(data[numerical_columns])
    
    return data


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data = delete_outlier_values(data)
    target = data["price"]
    numerical_columns, categorical_columns = create_num_cat(data)
    data, encoder_columns = encoder(data, categorical_columns)
    data = scalar(data, numerical_columns)
    
    X = pd.concat([data[numerical_columns], data[encoder_columns], target], axis=1)

    return X
