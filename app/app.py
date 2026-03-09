import streamlit as st
import os

st.set_page_config(
    page_title="Stroke Prediction App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🧠 Stroke Prediction App")
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown("This app predicts stroke likelihood based on patient health data.")

BASE_DIR = os.getcwd()  

intro = st.Page(os.path.join(BASE_DIR, "pages", "1_Introduction.py"), title="Introduction", icon="📋")
dataset = st.Page(os.path.join(BASE_DIR, "pages", "2_Dataset.py"), title="Dataset", icon="📊")
visuals = st.Page(os.path.join(BASE_DIR, "pages", "3_Visualisations.py"), title="Visualisations", icon="📈")
model = st.Page(os.path.join(BASE_DIR, "pages", "4_Model_Summary.py"), title="Model Summary", icon="🤖")
prediction = st.Page(os.path.join(BASE_DIR, "pages", "5_Stroke_Prediction.py"), title="Stroke Prediction", icon="🩺")

pg = st.navigation([intro, dataset, visuals, model, prediction])
pg.run()