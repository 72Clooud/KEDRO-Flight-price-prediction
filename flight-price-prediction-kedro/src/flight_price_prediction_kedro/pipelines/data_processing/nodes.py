"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.9
"""
import pandas as pd
from datetime import datetime

def concat_2_tables(x: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(x, ignore_index=True)

def to_price(x: pd.DataFrame) -> pd.Series:
    return x.str.replace(",", "").astype(float)

def add_class(x: pd.DataFrame, y: str) -> pd.DataFrame:    
    if y == "economy":
        x["class"] = "economy"
        return x
    elif y == "business":
        x["class"] = "business"
        return x
def label_time_of_day(x: pd.Series) -> pd.Series:
    def assign_time_of_day(time):
        if isinstance(time, str):
            time = datetime.strptime(time, "%H:%M").time()  
            
        if time >= datetime.strptime("05:00", "%H:%M").time() and time < datetime.strptime("08:00", "%H:%M").time():
            return "Early_morning"
        elif time >= datetime.strptime("08:00", "%H:%M").time() and time < datetime.strptime("12:00", "%H:%M").time():
            return "Morning"
        elif time >= datetime.strptime("12:00", "%H:%M").time() and time < datetime.strptime("17:00", "%H:%M").time():
            return "Afternoon"
        elif time >= datetime.strptime("17:00", "%H:%M").time() and time < datetime.strptime("21:00", "%H:%M").time():
            return "Evening"
        else:
            return "Night"

    return x.apply(lambda time: assign_time_of_day(time))

        
def create_flights_code(x: pd.DataFrame) -> pd.DataFrame:
    x["flights"] = x["ch_code"].astype(str) + "-" + x["num_code"].astype(str)
    x.drop(columns=["ch_code", "num_code"], inplace=True)
    return x


def days_until_departure(data: pd.DataFrame) -> pd.Series:
    purchase_day = datetime(2022, 2, 11).date()
    
    def calculate_days(row_date):
        if row_date == purchase_day:
            return 1
        delta = row_date - purchase_day
        return delta.days

    data["date"] = pd.to_datetime(data["date"], dayfirst=True, errors='coerce').dt.date  

    if data["date"].isnull().any():
        raise ValueError("Error")
    return data["date"].apply(calculate_days)

def stops(x: pd.Series) -> pd.Series:
    def process_stop_value(val):
        val = str(val).strip()  
        if val == "non-stop":
            return "zero"
        elif val in ["1-stop", "1-stop Via IDR", "1-stop Via IXU"]:
            return "one"
        elif val == "2+-stop":
            return "two_or_more"
        else:
            return "unknown"  
    
    return x.apply(process_stop_value)

def preprocess_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1 = add_class(df1, "business")
    df2 = add_class(df2, "economy")
    df_final = concat_2_tables([df1, df2])
    df_final = create_flights_code(df_final)
    df_final["date"] = days_until_departure(df_final)
    df_final["stop"] = stops(df_final["stop"])
    df_final["dep_time"] = label_time_of_day(df_final["dep_time"])
    df_final["arr_time"] = label_time_of_day(df_final["arr_time"])
    
    return df_final