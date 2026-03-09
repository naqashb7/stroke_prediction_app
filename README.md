# Stroke Prediction App

**Stroke Prediction app** is an application to help patients understand the likelihood of a stroke occurrence in their life based off a variety of lifestyle factors when entered into the app.[Click here to visit the app!](https://stroke-prediction-app-fc9b227f2a45.herokuapp.com/)

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset selected was a stroke prediction dataset from Kaggle. (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data)
* The dataset was selected as it had a large variety of features to analyse that could impact stroke occurrences and also it was upvoted the most on Kaggle which indicated it was a reliable dataset to use amongst the data science community.
* The dataset contained the following columns:
    * Id (removed)
    * Gender - Male or Female
    * Age
    * Hypertension - 1 or 0 dependent on the presence in the patient's life
    * Heart Disease - 1 or 0 dependent on the presence in the patient's life
    * Marital history - If the patient was ever married
    * Work type - If they are in the private sector, public sector, self-employed, caring for children or never employed
    * Residence type - If they live in an urban or a rural environment
    * Average Blood glucose level
    * BMI
    * Smoking status - If they smoke, used to smoke or have never smoked
    * Stroke - 1 or 0 dependent on whether the patient ever had a stroke in their life or not
* The dataset is related to real-world issues as stroke is a life threatening disease that affects many people worldwide.
* The dataset also had about 5000 records which allowed for deriving meaningful conclusions and being able to understand the impact of different variables on stroke occurrence.
* The dataset did not have many missing values and so remained easy to clean.

## Business Requirements
Business requirements were as follows:
1. Identify the significance of the following factors on the likelihood of stroke occurrence:
    * Age
    * Gender
    * Average Blood Glucose Levels
    * Presence of Hypertension
    * Presence of Heart Disease
    * BMI
    * Smoking
    * Marital History
2. Based off historical data, create a model to allow patients to input information and predict stroke occurrence probability



## Hypothesis and how to validate?

1) Age
    * **H<sub>1</sub>**: As a person's age increases, so will the likelhood of stroke occurrences.
2) Blood glucose
    * **H<sub>0</sub>**: As a person's blood glucose levels increase, the likelihood of stroke occurrences will not increase.
3) Heart Disease
    * **H<sub>1</sub>**: If a person has heart disease, then they are more likely to have a stroke.
4) Hypertension
    * **H<sub>1</sub>**: If a person has hypertension, then they are more likely to have a stroke.
5) Gender
    * **H<sub>0</sub>**: Gender has no impact on stroke likelihood.
6) Smoking history
    * **H<sub>1</sub>**: Smoking has a direct impact on stroke likelihood.
7) BMI
    * **H<sub>1</sub>**: Higher BMI's indicate a higher likelihood of stroke occurrences.
8) Marital History
    * **H<sub>0</sub>**: Marriage has no relation to stroke occurrence likelihood.
9) Job type
    * **H<sub>0</sub>**: Job type has no relation to stroke occurrence likelihood.
10) Residence type
    * **H<sub>0</sub>**: Residence type has no relation to stroke occurrence likelihood.

## Project Plan
* The steps taken for analysis were as follows:
    1) ETL pipeline - Clean the raw data and export it to a clean data file
    2) EDA - visualise the data to determine patterns and connections
    3) Modelling - Create a new Model dataset and then use a Machine Learning model to predict stroke outcomes
    4) App - Build Streamlit App and deploy with predictive model
* A breakdown of the tasks undertaken for the project can be seen [here](https://github.com/users/naqashb7/projects/2/views/1)


## The rationale to map the business requirements to the Data Visualisations
* Business requirements were as follows (alongside the plots used to visualise them):
1. Identify the significance of the following factors on the likelihood of stroke occurrence:
    * Age - Violin plot
    * Gender - Bar chart
    * Average Blood Glucose Levels - Violin plot & Count Plots
    * Presence of Hypertension
    * Presence of Heart Disease
    * BMI - Violin plot & Count plots
    * Smoking - Bar chart
    * Marital History - Count Plots
2. Based off historical data, create a model to allow patients to input information and predict stroke occurrence probability - the model selected after evaluation was the Logistic Regression Model

## Analysis techniques used
* Data visualisation using Violin plots, Count plots, Bar charts and Correlation Matrices were used to analyse the clean data.
* Statistical methods such as p-value and T-test were also used alongside Variance, Standard deviation and Coefficient of Variation analyses techniques were used.
* The Data was split between analysis of Numerical data and then Categorical data. It seemed like the natural split when analysing the data.
* The dataset was small and not of good quality. This limited me in achieving accurate conclusions from the data (even though it was real-world data). It also impacted the ML model and it predictive capabilities. In fact, the dataset was so poor that, 2 of the 3 ML models, when trained and tested, still could not accurately predict stroke occurrences.
* I used Claude AI to help with code debugging and project structure planning.

## Ethical considerations
* There were no data privacy issues as all data was anonymised.
* The only issue was the dataset was too small and this did not allow EDA & Modelling to be as accurate as it could have been.
* A larger dataset with better quality data would have increasd the reliability of the models and allowed for more accurate analysis.

## Dashboard Design
* The Dashboard was built as a Streamlit App and was structured as follows:
    1) Introduction - A summary of the project as a whole
    2) Dataset - A snapshot of the dataset
    3) Visualisations - Visualisations derived from the dataset
    4) Model Summary - A summary of the model selection process
    5) Stroke prediction - A page to help predict stroke outcomes based off user inputs
* The dashboard caters for both Technical and Non-technical audiences because:
    * Technical Audiences can understand the model selection criteria and statistical analysis
    * Non-technical audiences can understand the data used and the visualisations while also being able to use the prediction section


## Development Roadmap
* It was difficult as the ML Pipeline and Streamlit App were both new but by using online research and Claude AI to guide me I was able to build a successful model and an app with Predictive capabilities.
* The Dataset also made it difficult as I am a perfectionist and so would want to build a perfect model but the dataset helped teach me that in the real-world no dataset will be perfect and so evaluation of the data is important and then learning how to deal with data going forward.
* I think going forward I will be able to create the app and ML pipeline more smoothly now that I have done it once.
* I also think, going forward, I would use a larger dataset and possibly from a different source (potentially NHS). This may give more definitive results and help shape the ML model better.
* I also think in the future I would play around with model hyperparameters to better train the model and see which hyperparameters have a stronger impact on the model performance.

## Deployment
### Heroku

* Heroku was used to deploy the app.
* Initially there was an issue and the app wouldn't deploy.
* It was determined that libraries that weren't needed had to be removed from the requirements.txt file and the app path had to be defined in the Procfile.


## Main Data Analysis Libraries

The following Python libraries were used, alongside which section of the project they were utilised in:

* Pandas - ETL, EDA, Modelling, App
* Matplotlib - EDA, App
* Seaborn - EDA, App
* Plotly - App
* Scipy - Modelling
* Scikitlearn - Modelling, App
* Imbalanced Learn - Modelling
* Streamlit - App


## Credits 

* Kaggle for the dataset


