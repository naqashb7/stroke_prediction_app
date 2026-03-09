import streamlit as st
import pandas as pd
import joblib

st.title("🩺 Stroke Risk Prediction")
st.markdown("Enter your details below to predict your likelihood of stroke.")

st.markdown("---")

# User inputs
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=0, max_value=100, value=45)
    bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, value=25.0)
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
    hypertension = st.selectbox("Hypertension", options=["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", options=["No", "Yes"])

with col2:
    gender = st.selectbox("Gender", options=["Male", "Female"])
    ever_married = st.selectbox("Ever Married", options=["Yes", "No"])
    work_type = st.selectbox("Work Type", options=["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    residence_type = st.selectbox("Residence Type", options=["Urban", "Rural"])
    smoking_status = st.selectbox("Smoking Status", options=["never smoked", "formerly smoked", "smokes"])

st.markdown("---")

def encode_inputs():
    data = {
        "age": [age],
        "hypertension": [1 if hypertension == "Yes" else 0],
        "heart_disease": [1 if heart_disease == "Yes" else 0],
        "avg_glucose_level": [avg_glucose_level],
        "bmi": [bmi],
        "ever_married_encoded": [1 if ever_married == "Yes" else 0],
        "Residence_type_encoded": [1 if residence_type == "Urban" else 0],
        "gender_encoded": [1 if gender == "Male" else 0],
        "work_type_Govt_job": [1 if work_type == "Govt_job" else 0],
        "work_type_Never_worked": [1 if work_type == "Never_worked" else 0],
        "work_type_Private": [1 if work_type == "Private" else 0],
        "work_type_Self-employed": [1 if work_type == "Self-employed" else 0],
        "work_type_children": [1 if work_type == "children" else 0],
        "smoking_status_formerly smoked": [1 if smoking_status == "formerly smoked" else 0],
        "smoking_status_never smoked": [1 if smoking_status == "never smoked" else 0],
        "smoking_status_smokes": [1 if smoking_status == "smokes" else 0],
    }

    column_order = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
                    'ever_married_encoded', 'Residence_type_encoded', 'gender_encoded',
                    'work_type_Govt_job', 'work_type_Never_worked', 'work_type_Private',
                    'work_type_Self-employed', 'work_type_children',
                    'smoking_status_formerly smoked', 'smoking_status_never smoked',
                    'smoking_status_smokes']

    return pd.DataFrame(data)[column_order]

# Predict button
if st.button("Predict Stroke Risk"):
    input_df = encode_inputs()

    model = joblib.load("model/lr_model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")

    if prediction == 1:
        st.error(f"⚠️ High Stroke Risk Detected — Probability: {probability:.1%}")
        st.markdown("Your stroke risk is elevated. Please consider consulting a medical professional as soon as possible.")
    else:
        st.success(f"✅ Low Stroke Risk — Probability: {probability:.1%}")
        st.markdown("You are currently safe from stroke risk.")

    st.warning("⚠️ This is not official medical advice and should not replace professional medical advice. If you have any concerns about your health, please seek medical attention")
