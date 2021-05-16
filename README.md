<h1>Recommendation System(RecSys) Modelling </h1>

```
Chen Yan 
```

Please note that all our python scripts need Python3.7+ to run.
You can find the web frontend demo video here: [Video link](https://drive.google.com/file/d/1im3I8BUbp66ieUmJY9IBLckXa2t19F3_/view?usp=sharing)


## Overview
Given the datasets of clicks of merchants on Shopback Korea between January - March 2021, here are two functions that I done:

1. Build a prediction model to predict what is the next merchant a user will click.
2. Serve the model in a web service use streamlit.

## UI Demo 

```
pip install streamlit
```

```
streamlit run web2.py
```
## The steps to predit the next merchant with the web service

1. The web service have an endpoint called `/predict`, that takes in user-defined input as return a `merchant_id` as its prediction output. 

## Notebook file directories

1. data (It includes original data)
2. data_csv (It transfers original data to csv format and store it in this file)
3. data_select_features (It includes a dataset that after data cleaning and features selection)
4. train_models (This file include different trained models)
5. web_framework (This file include streamlit web service code)
6. EDA_ExploreDataset.ipynb (This is the main code for exploring the given datasets)
7. model_building.ipynb (This is the main code for model building)
8. web.py (This is the main code for model serving on stremlit web service)

## Outline of this notebook : EDA_ExploreDataset.ipynb

        Part1 : Visualize Parquet Data in Python
        Part2 : Data clean
                1. Rename cols of dataframe
                2. Merge three dataframe
                3. Calculate click number of stores and add to dataset
        Part3 : EDA Task
                1. Task1 : The most clicked merchant for month January 2021
                2. Task2 : The distribution of clicks of merchant for month March 2021
                3. Task3 : On average, what are the number of clicks user make in 1 month?
        Part4 : Dataset preparation
                1.List all classes of each features
                2.Label selected features with numeric format for fit in model
                3.Create a new dataset for training and testing with numeric label and selected features
                4.Create a list of labels for prediction
                5.Store final dataset for training model new_dataset_features2

## Outline of this notebook : model_building.ipynb

        Part1 : EDA : Visualise how balance our new_dataset is
        Part2 : Training and Test dataset Split
        Part3 : Define and train the model (Machine Learning)
                1. GNB model
                2. Decision three model
                3. K near neighbor model
                4. Random Forest model
        Part4 : Set evaluate metrix function
                1.AUC
                2.Report
                3.Confusion
                4.Rocfig
        Part5 : Predict and evaluate metric
        Part6 : Save Predict Result
        Part7 : Save models

## Task and function implemented 

> Explore the Given datasets (EDA_ExploreDataset.ipynb)
1. The most clicked merchant for month January 2021
2. The distribution of clicks of merchant for month March 2021
3. On average, The number of clicks user make in 1 month


> Model Building (model_building.ipynb)
1. Perform Train-Test split for the datasets
2. Measure the performance of the Test Dataset using any RecSys metrics.

> Model Serving on Streamlit web service (web.py)
1. The web service have an endpoint called `Get next prediction`, that takes in user-defined input , click `Predict now` button as return a `merchant_id` as its prediction output. 
2. The video above clearly show the steps to run the web service locally.

