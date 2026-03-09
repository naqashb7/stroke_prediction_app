import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

st.title("🤖 Model Summary")

# Load model and test data
lr_model = joblib.load("model/lr_model.pkl")
X_test = pd.read_csv("model/X_test.csv")
y_test = pd.read_csv("model/y_test.csv")

st.subheader("Model Selected: Logistic Regression")
st.markdown("""
## Why Logistic Regression?
After evaluating three models, Logistic Regression was selected because:
- Highest **recall of 0.79** for stroke cases — catching 42 out of 53 actual strokes
- Random Forest and Decision Tree achieved near-zero recall for stroke cases
- Most appropriate for **binary medical classification**
- Most interpretable — important in a healthcare context
""")

st.markdown("---")

# Model comparison table
st.subheader("Model Comparison")
comparison_df = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest", "Decision Tree"],
    "Accuracy": [0.72, 0.95, 0.92],
    "Stroke Recall": [0.79, 0.00, 0.06],
    "Stroke F1": [0.22, 0.00, 0.07]
})
st.dataframe(comparison_df, use_container_width=True)

st.markdown("---")

# Classification report
st.subheader("Logistic Regression Classification Report")
report_df = pd.DataFrame({
    "Class": ["No Stroke (0)", "Stroke (1)"],
    "Precision": [0.98, 0.13],
    "Recall": [0.71, 0.79],
    "F1 Score": [0.83, 0.22],
    "Support": [975, 53]
})
st.dataframe(report_df, use_container_width=True)

st.markdown("---")

# Key metrics
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "0.72")
col2.metric("Stroke Recall", "0.79")
col3.metric("Stroke Precision", "0.13")
col4.metric("Stroke F1", "0.22")

st.markdown("---")

# Confusion matrix
st.subheader("Confusion Matrix")
y_pred = lr_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(6, 5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(ax=ax)
ax.set_title("Logistic Regression Confusion Matrix")
st.pyplot(fig)
