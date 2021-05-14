<h1>Recommendation System(RecSys) Modelling </h1>

```
Chen Yan 
```

Please note that all our python scripts need Python3.7+ to run.
You can find the web frontend demo video here: [Video link](https://github.com/chenyan1998)

## Overview
Given the datasets of clicks of merchants on Shopback Korea between January - March 2021, here are two functions that I done:

1. Build a prediction model to predict what is the next merchant a user will click.
2. Serve the model in a web service use streamlit.

## UI Demo 

```
pip install streamlit
```

```
streamlit run web.py
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

## Task and function implemented 

> Explore the Given datasets (EDA_ExploreDataset.ipynb)
1. The most clicked merchant for month January 2021
2. The distribution of clicks of merchant for month March 2021
3. On average, The number of clicks user make in 1 month


> Model Building (model_building.ipynb)
1. Perform Train-Test split for the datasets
2. Measure the performance of the Test Dataset using any RecSys metrics.

> Model Serving on Streamlit web service
1. The web service should have an endpoint called `/predict`, that takes in user-defined input as return a `merchant_id` as its prediction output. 
2. Document clearly the steps to run the web service locally.

### Nice to have:
1. Any additional endpoints, e.g. `/batch_predict`, for completeness.
2. Dockerization of the service(s)
3. Good Code Style (e.g. PEP 8 for python)
4. Unit Testing

## Submission
Organize your files and folder like how you would organize in a proper Git Repository. Include the notebooks or scripts used during the exercise.
Please attach a `README.md` file in your root directory that documents:
1. Your file directories
2. Notebooks Path for the corresponding task.
3. Steps to run the Model Web Service
4. and any that would help the interviewers navigate through the repository

Zip the whole repository and send them back to Shopback Talent Acquisition Team.
