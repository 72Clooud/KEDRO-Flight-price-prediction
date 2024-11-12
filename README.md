# Flight-price-prediction
This project is a machine learning pipeline for predicting flight prices using the Kedro framework. It processes a dataset of flight prices, builds and trains models to estimate ticket prices based on features such as departure and arrival times, airline, and duration. The pipeline structure helps organize data engineering, model training, and evaluation in a reproducible way.
# Dataset
The project uses the Flight Price Prediction Dataset from Kaggle, which includes data on various flight characteristics:
## Columns:
- Airline
- Source and Destination cities
- Route taken
- Departure and Arrival Times
- Flight Duration
- Number of Stops
- Price (target variable)
https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction/data
# Technologies Used
- Kedro: A Python framework that simplifies the process of building robust, modular, and reproducible data science pipelines.
- Pandas: Essential library for data manipulation and analysis, used here for cleaning, transforming, and preparing flight data.
- NumPy: Fundamental package for numerical operations in Python, supporting data processing and manipulation.
- Scikit-learn: Popular machine learning library, providing tools for model selection, training, and evaluation, as well as utilities for preprocessing.
- Matplotlib and Seaborn: Visualization libraries used for exploring and visualizing data patterns and model performance metrics.
- Jupyter Notebook: An interactive environment for conducting exploratory data analysis (EDA) and prototyping machine learning models
# Setup
'''bash
git clone https://github.com/72Clooud/KEDRO-Flight-price-prediction.git
cd KEDRO-Flight-price-prediction
'''
'''bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
'''
'''bash
pip install -r src/requirements.txt
'''
'''bash
kedro run
'''


