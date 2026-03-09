import streamlit as st

st.title("📋 Introduction")
st.markdown("""
## Project Overview
This project explores the key risk factors associated with stroke occurrence 
using a dataset of patient health and demographic information.

## Dataset
- **Source:** Stroke Prediction Dataset from Kaggle
- **Records:** 5,110 patients
- **Target Variable:** Stroke (0 = No Stroke, 1 = Stroke)

## Key Findings
- Age was given the greatest weight as a predictor of stroke occurrence
- Higher average glucose levels had a strong relationship with increased stroke risk
- Individuals with medical histories that included hypertension and heart disease showed higher stroke rates

## Methodology
1. Data cleaning and ETL
2. Exploratory Data Analysis (EDA)
3. Feature encoding and preprocessing
4. Machine Learning model training and evaluation

## Conclusion
The Logistic Regression model was selected as the most suitable model 
for stroke prediction, achieving a recall of 0.79 for stroke cases.
""")
