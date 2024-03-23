import streamlit as st
import pandas as pd
import numpy as np



df = pd.read_csv("df_cleaned.csv")
st.markdown("<h1 style='text-align: center; color: black;'>Heart Attack Prediction</h1>",unsafe_allow_html=True)
st.image(r'https://www.nhlbi.nih.gov/sites/default/files/styles/meta_image/public/2022-09/Heart.jpg?itok=Mfe23Jii')
st.markdown("""
    ## Description of Columns
    
    - **Patient ID**: Unique identifier for each patient.
    - **Age**: Age of the patient.
    - **Sex**: Gender of the patient.
    - **Cholesterol**: Cholesterol level of the patient.
    - **Blood Pressure**: Blood pressure reading of the patient (systolic/diastolic).
    - **Heart Rate**: Heart rate of the patient.
    - **Diabetes**: Whether the patient has diabetes or not.
    - **Family History**: Whether the patient has a family history of heart disease.
    - **Smoking**: Whether the patient is a smoker or not.
    - **Obesity**: Whether the patient is obese or not.
    - **Country**: Country of the patient.
    - **Continent**: Continent of the patient's country.
    - **Hemisphere**: Hemisphere of the patient's location.
    - **Heart Attack Risk**: Indicates if the patient is at risk of a heart attack.
    - **Age groups**: Categorization of age into groups like 'Old' or 'Youth'.
    - **Stress Level Cats**: Categorization of stress level.
    - **Systolic Pressure**: The systolic value of blood pressure.
    - **Diastolic Pressure**: The diastolic value of blood pressure.
    - **Blood cats**: Categorization of blood pressure.
    - **Exercise_Cats**: Categorization of exercise levels.
    
    <style>
        h2 {
            color: #1f618d; /* Change color of header */
        }
        ul {
            list-style-type: none; /* Remove bullet points */
            padding-left: 0; /* Remove default padding */
        }
        li {
            margin-bottom: 10px; /* Add spacing between items */
        }
        li strong {
            color: #c0392b; /* Change color of bold text */
        }
    </style>
""", unsafe_allow_html=True)

st.dataframe(df, width=800, height=400, use_container_width=True, hide_index=True )
