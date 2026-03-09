import streamlit as st
import pandas as pd

st.title("📊 Dataset Overview")

df = pd.read_csv("data_files/ModellingData/stroke_data_modelling.csv")

# Dataset shape
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", df.shape[0])
col2.metric("Total Features", df.shape[1])
col3.metric("Stroke Cases", df["stroke"].sum())

st.markdown("---")

# Raw data
st.subheader("Raw Data Sample")
st.dataframe(df.head(20))

st.markdown("---")

# Descriptive statistics
st.subheader("Descriptive Statistics")
st.dataframe(df.describe())

st.markdown("---")

# Missing values
st.subheader("Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Feature", "Missing Values"]
st.dataframe(missing)

st.markdown("---")

# Class distribution
st.subheader("Stroke Class Distribution")
col1, col2 = st.columns(2)
col1.metric("No Stroke (0)", df[df["stroke"] == 0].shape[0])
col2.metric("Stroke (1)", df[df["stroke"] == 1].shape[0])
