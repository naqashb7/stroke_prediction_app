import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



st.sidebar.title("🔽 Filter Data")


df = pd.read_csv("data_files/ModellingData/stroke_data_modelling.csv")

st.sidebar.header("Filter the data and display it on the visualisations")

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

age_filter = st.sidebar.slider(
    "Age Range",
    min_value=int(df["age"].min()),
    max_value=int(df["age"].max()),
    value=(0, 80)
)

stroke_filter = st.sidebar.multiselect(
    "Stroke",
    options=[0, 1],
    default=[0, 1],
    format_func=lambda x: "Stroke" if x == 1 else "No Stroke"
)
hypertension_filter = st.sidebar.multiselect(
    "Hypertension",
    options=[0, 1],
    default=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

heart_disease_filter = st.sidebar.multiselect(
    "Heart Disease",
    options=[0, 1],
    default=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age"].between(age_filter[0], age_filter[1])) &
    (df["stroke"].isin(stroke_filter)) &
    (df["hypertension"].isin(hypertension_filter)) &      
    (df["heart_disease"].isin(heart_disease_filter))      
]

st.title("📈 Visualisations")
st.write(f"Showing {len(filtered_df)} records")
st.info(""" Use the Filters on the left to see how the data changes when changing variable output""")
st.markdown("---")

st.subheader("🔍 Interactive: Age vs Average Glucose Level by Stroke")
st.info("""Play around with the chart below to see how Age and Average blood Glucose levels can affect stroke likelihood!
The White dots represent stroke cases while the Blue dots represent no stroke cases.
\n\n The Analysis shows:
    - As Age increases, Stroke cases increase""")

fig = px.scatter(
    filtered_df,
    x="age",
    y="avg_glucose_level",
    color="stroke",
    color_discrete_map={0: "steelblue", 1: "red"},
    labels={"stroke": "Stroke", "age": "Age", "avg_glucose_level": "Avg Glucose Level"},
    title="Age vs Average Glucose Level by Stroke Occurrence",
    hover_data=["bmi", "gender"]
)
st.plotly_chart(fig, use_container_width=True)




st.markdown("---")


st.subheader("Age vs Stroke")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.violinplot(data=filtered_df, x="stroke", y="age", palette="Set2", inner="quartile", ax=ax1)
ax1.set_xticklabels(["No Stroke", "Stroke"])
ax1.set_title("Age vs Stroke Occurrence")
st.pyplot(fig1)
st.info("In the above figure we can see that as age of person increases then the likelihood of stroke occurrence also increases.")
st.markdown("---")


st.subheader("Average Glucose Level by Stroke")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.violinplot(data=filtered_df, x="stroke", y="avg_glucose_level", palette="Set2", inner="quartile", ax=ax2)
ax2.set_xticklabels(["No Stroke", "Stroke"])
ax2.set_title("Glucose Level Distribution by Stroke Occurrence")
st.pyplot(fig2)
st.info(""" 
- The initial violinplot for this data indicated that there was a significantly higher amount of individuals with stroke history when average blood glucose levels were high. This required further analysis as there were two nodes on this plot, one on the lower half of the plot and one on the upper half of the plot.
- The plot was split by both nodes at the 150mg/dl point.
- After assessing the proportional differences of both plots, it was possible to see that the upper half of the plot indicated that stroke was 3x more likely in individuals with an average blood glucose higher than 150mg/dl.
- Further statistical analysis indicated that there was a large difference between the groups of both nodes and the difference between both was statistically significant and so the results could not be attributed to chance.""")
st.markdown("---")


st.subheader("📊 Clinical & Numerical Analysis")


col1, col2 = st.columns(2)

with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 5))
    hyp_summary = filtered_df.groupby("hypertension")["stroke"].mean() * 100
    hyp_summary = hyp_summary.reindex([0, 1], fill_value=0)  # ← ensures both categories exist
    ax4.bar(["No Hypertension", "Hypertension"], hyp_summary.values, color=["steelblue", "salmon"], edgecolor="black")
    ax4.set_ylabel("Stroke Rate (%)")
    ax4.set_title("Stroke Rate by Hypertension")
    st.pyplot(fig4)
st.info("""
- Upon analysis, those with hypertension history had a 10% higher chance of having a stroke occurrence in their medical history.
- The data showed that a person with heart disease was shown to be 13% more likely to have a stroke """)
with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    hd_summary = filtered_df.groupby("heart_disease")["stroke"].mean() * 100
    hd_summary = hd_summary.reindex([0, 1], fill_value=0)  # ← ensures both categories exist
    ax5.bar(["No Heart Disease", "Heart Disease"], hd_summary.values, color=["steelblue", "salmon"], edgecolor="black")
    ax5.set_ylabel("Stroke Rate (%)")
    ax5.set_title("Stroke Rate by Heart Disease")
    st.pyplot(fig5)

st.markdown("---")


st.markdown("#### Hypertension & Heart Disease vs Stroke")
col3, col4 = st.columns(2)

with col3:
    fig6, ax6 = plt.subplots(figsize=(6, 5))
    sns.countplot(data=filtered_df, x="hypertension", hue="stroke", palette="Set2", ax=ax6, order=[0, 1])
    ax6.set_xticks([0, 1])
    ax6.set_xticklabels(["No Hypertension", "Hypertension"])
    ax6.set_title("Hypertension vs Stroke")
    ax6.legend(["No Stroke", "Stroke"])
    st.pyplot(fig6)

with col4:
    fig7, ax7 = plt.subplots(figsize=(6, 5))
    sns.countplot(data=filtered_df, x="heart_disease", hue="stroke", palette="Set2", ax=ax7, order=[0, 1])
    ax7.set_xticks([0, 1])
    ax7.set_xticklabels(["No Heart Disease", "Heart Disease"])
    ax7.set_title("Heart Disease vs Stroke")
    ax7.legend(["No Stroke", "Stroke"])
    st.pyplot(fig7)

st.markdown("---")




st.markdown("#### BMI vs Glucose by Stroke")
fig10 = px.scatter(
    filtered_df,
    x="bmi",
    y="avg_glucose_level",
    color="stroke",
    color_discrete_map={0: "steelblue", 1: "red"},
    labels={"bmi": "BMI", "avg_glucose_level": "Avg Glucose Level", "stroke": "Stroke"},
    title="BMI vs Average Glucose Level by Stroke"
)
st.info("""  This dataset shows an almost even spread of BMI's amongst those individuals who experienced stroke vs those who did not.""")
st.plotly_chart(fig10, use_container_width=True)