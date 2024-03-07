import streamlit as st
import pandas as pd
import numpy as np



df = pd.read_csv("df_cleaned.csv")
st.markdown("<h1 style='text-align: center; color: black;'>Heart Attack Prediction</h1>",unsafe_allow_html=True)
st.image(r'https://www.nhlbi.nih.gov/sites/default/files/styles/meta_image/public/2022-09/Heart.jpg?itok=Mfe23Jii')
st.write('''Patient Information:

Patient ID: Unique identifier for each patient.
Age: Age of the patient.
Sex: Gender of the patient.
Cholesterol: Cholesterol level of the patient.
Blood Pressure: Blood pressure of the patient, given as systolic/diastolic.
Heart Rate: Heart rate of the patient.
Diabetes: Boolean indicating whether the patient has diabetes.
Family History: Boolean indicating whether the patient has a family history of heart disease.
Smoking: Boolean indicating whether the patient smokes.
Obesity: Boolean indicating whether the patient is obese.
Additional Health Parameters:

Sleep Hours Per Day: Number of hours per day the patient sleeps.
Demographic Information:

Country: Country where the patient is located.
Continent: Continent where the patient is located.
Hemisphere: Hemisphere where the patient is located.
Target Variable:

Heart Attack Risk: Boolean indicating whether the patient is at risk of a heart attack.
Derived Features:

Age groups: Categorized age groups, possibly derived from the 'Age' column.
systolic pressure: The systolic component of blood pressure.
diastolic pressure: The diastolic component of blood pressure.
blood cats: Categorized blood pressure levels.
Exercise_Cats: Categorized physical activity level.
This dataset seems to be a collection of health-related information for multiple patients, including various health parameters, demographic details, and risk assessment for heart attack. It could be used for analysis to understand factors influencing heart health and risk assessment across different demographics.''')

st.dataframe(df, width=800, height=400, use_container_width=True, hide_index=True )
