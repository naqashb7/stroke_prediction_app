import streamlit as st

st.title("📋 Introduction")
st.markdown("""
## App Overview
This app looks to predict stroke likelihood on individuals. It explores risk factors associated with stroke occurrence 
using a dataset of historic health and demographic information. 
            
---
            
## Background
A Stroke is a medical emergency caused by interrupted blood flow to the brain. This can lead to cell death. Approximately, 12 million **NEW** cases of stroke
occur every year, affecting 1 in 4 people over the age of 25 in their lifetime.

---

## Dataset background
- **Source:** [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) from Kaggle
- **Records:** 5,110 patients
- **Target Variable:** Stroke (0 = No Stroke, 1 = Stroke)
- **Other Variables:**
    - Age
    - Gender 
    - Hypertension
    - Heart Disease
    - Marital History
    - Work Type
    - Residence Type
    - Average Blood Glucose Levels
    - BMI
    - Smoking Status

---
            
## Key Findings
- Age was given the greatest weight as a predictor of stroke occurrence
- Higher average glucose levels had a strong relationship with increased stroke risk
- Individuals with medical histories that included hypertension and heart disease showed higher stroke rates

---            

## Full Project Process
1. ETL pipeline
2. Exploratory Data Analysis (EDA)
3. Machine Learning Pipeline
4. Predictive App and dashboard design and deployment

---            
## Hypotheses
            
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

            

---

## Conclusions


1) Age
    * **H<sub>1</sub>**: As a person's age increases, so will the likelhood of stroke occurrences.
        * From the data it was possible to see that this hypothesis is correct. Those individuals who reported a medical history of stroke occurrence were clustered more to the older years of age, while those who did not report a medical history of stroke were spread throughout all ages.
2) Blood glucose
    * **H<sub>0</sub>**: As a person's blood glucose levels increase, the likelihood of stroke occurrences will not increase.
        * The initial analysis for this data indicated that there was a significantly higher amount of individuals with stroke history when average blood glucose levels were high. This required further analysis as there were two nodes on this plot, one on the lower half of the plot and one on the upper half of the plot.
        * The plot was split by both nodes at the 150mg/dl point.
        * After assessing the proportional differences of both plots, it was possible to see that the upper half of the plot indicated that stroke was 3x more likely in individuals with an average blood glucose higher than 150mg/dl.
        * Further statistical analysis indicated that there was a large difference between the groups of both nodes and the difference between both was statistically significant and so the results could not be attributed to chance.
        * This null hypothesis could be rejected. 
3) Heart Disease
    * **H<sub>1</sub>**: If a person has heart disease, then they are more likely to have a stroke.
        * Upon analysis, the data showed that a person with heart disease was shown to be 13% more likely to have a stroke. This hypothesis can be accepted.
4) Hypertension
    * **H<sub>1</sub>**: If a person has hypertension, then they are more likely to have a stroke.
        * Upon analysis, those with hypertension history had a 10% higher chance of having a stroke occurrence in their medical history.
        * This hypothesis can be accepted.
5) Gender
    * **H<sub>0</sub>**: Gender has no impact on stroke likelihood.
        * Upon analysis, there was no significant difference in gender on stroke likelihood and so this hypothesis failed to be rejected.
6) Smoking history
    * **H<sub>1</sub>**: Smoking has a direct impact on stroke likelihood.
        * According to the data, when analysed, there was no significant impact of any smoking status on stroke likelihood therefore, this hypothesis can be rejected.
7) BMI
    * **H<sub>1</sub>**: Higher BMI's indicate a higher likelihood of stroke occurrences.
        * Although the Median value was slightly higher, according to the analysis of this dataset, it is not true and so this hypothesis can be rejected. This dataset shows an almost even spread of BMI's amongst those individuals who experienced stroke vs those who did not.
8) Marital History
    * **H<sub>0</sub>**: Marriage has no relation to stroke occurrence likelihood.
        * On analysis of the data, it was found that individuals who had a marital history were 3x more likely to have a stroke than those who did not. The likelihood was small however, it was still more likely than not.
        * This hypothesis can be rejected.
9) Job type
    * **H<sub>0</sub>**: Job type has no relation to stroke occurrence likelihood.
        * According to the data the job types in order of most likely to cause a stroke to least likely are as follows:
            * Self Employment
            * Private Sector
            * Government Job
            * Unemployment
            * Care of children
        * As a result, even though the likelihood was low, it was still there therefore, the hypothesis can be rejected.
10) Residence type
    * **H<sub>0</sub>**: Residence type has no relation to stroke occurrence likelihood.
        * According to the data, when analysed, there was no significant impact of any residence type on stroke likelihood therefore, this hypothesis can be accepted.   
            

---
## Machine Learning Summary
3 ML models were tested to see which would work best in predicting stroke occurrences:

    -Logistic Regression
    -Decision Tree
    -Random Forest

The Logistic Regression model was selected as the most suitable model 
for stroke prediction, achieving a recall of 0.79 for stroke cases and an accuracy of 0.72.            
            
            
""", unsafe_allow_html=True)
