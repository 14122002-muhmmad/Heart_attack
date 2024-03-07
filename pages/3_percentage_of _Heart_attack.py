import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



df = pd.read_csv('df_cleaned.csv')
st.markdown("<h1 style='text-align: center; color: black;'>Percentage of Heart Attack</h1>",unsafe_allow_html=True)
with st.form('Your Status'):
    col1, Empty_col , col2 = st.columns([2,1,2])
    with col1:
        Age = st.selectbox('Age Group',df['Age groups'].unique())
        # smoking = st.selectbox('Smoking',df['Smoking'].unique())
    with col2:
        #Sex = st.selectbox('Sex',df['Sex'].unique())
        Alcohol = st.selectbox('Alcohol',df['Alcohol Consumption'].unique())
    with col1:
        bloodcats = st.selectbox('Blood Pressure Cats',df['blood cats'].unique())
        Diet = st.selectbox('Diet',df['Diet'].unique())
    with col2:
        Diabetes = st.selectbox('Diabetes',df['Diabetes'].unique())
        Stress = st.selectbox('Stress Level',df['Stress Level Cats'].unique())
        
    submitted = st.form_submit_button(label='Submit')
    if submitted:
        prediction = df[(df['Diabetes']==Diabetes)&(df['Stress Level Cats']==Stress)&(df['Age groups']==Age)&(df['Alcohol Consumption']==Alcohol)&(df['blood cats']==bloodcats)&(df['Diet']==Diet)]['Heart Attack Risk'].mean() *100
        try :
            prediction = prediction.round(2)
        except:
            prediction = 'nan'

        if prediction == 'nan':    
            st.write('Your percentage of getting a heart attack is 49.14%')
        else:
            st.write(f'Your percentage of getting a heart attack is {prediction}% ')
        if prediction >= 40:
            st.snow()
        else:
            st.balloons()
       