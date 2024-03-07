import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st. set_page_config(layout="wide")


df = pd.read_csv(r"H:\mid_year_project\df_cleaned.csv")
col1, col2, col3,  = st.columns(3)
with col1:
    fig = px.funnel(df,x='Continent',y='Heart Attack Risk',color='Country',title='Continent vs. Heart Attack Risk',hover_name='Country',width=800,height=600,color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
   
    Age_GR = df[df['Heart Attack Risk']==True].groupby('Age groups')['Heart Attack Risk'].count().reset_index()
    fig = px.pie(Age_GR,values='Heart Attack Risk',names='Age groups',color='Age groups',hole=0.5,title='Age groups vs. Heart Attack Risk',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
    
    l = df[df['Medication Use']==True].groupby('Age groups')['Heart Attack Risk'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(l,x='Age groups',y='Heart Attack Risk',color='Age groups',title='Heart Attack Risk by Age with Medication Use',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
    
    m = df.groupby(['Stress Level','Diabetes'])['Heart Attack Risk'].mean().reset_index()
    fig = px.line(m,x='Stress Level',y='Heart Attack Risk',color='Diabetes',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark',title='Stress Level vs. Heart Attack Risk')
    st.plotly_chart(fig, use_container_width=True)

    z = df[df['Family History'] == True].groupby('Smoking')['Heart Attack Risk'].count().sort_values(ascending=False).reset_index()
    fig = px.bar(z,x='Heart Attack Risk',y='Smoking',title='Smoking vs. Heart Attack Risk(had family history)',color='Smoking',color_discrete_sequence=px.colors.qualitative.Set3_r)
    st.plotly_chart(fig, use_container_width=True)

    
with col3:
    
    
    blood_cats = df.groupby('blood cats')['Heart Attack Risk'].mean().sort_values(ascending=False).reset_index()  
    fig = px.pie(blood_cats,values='Heart Attack Risk',names='blood cats',color='blood cats',title='blood cats vs. Heart Attack Risk(had  heart problems)',hole=0.5,color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    u = df.groupby(['Stress Level','Previous Heart Problems'])['Heart Attack Risk'].mean().reset_index()
    fig = px.line(u,x='Stress Level',y='Heart Attack Risk',color='Previous Heart Problems',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark',title='Stress Level vs. Heart Attack Risk')
    st.plotly_chart(fig, use_container_width=True)

    y = df[df['Previous Heart Problems'] == True].groupby('Alcohol Consumption')['Heart Attack Risk'].count().sort_values(ascending=False).reset_index()
    fig = px.bar(y,x='Heart Attack Risk',y='Alcohol Consumption',title='Alcohol Consumption vs. Heart Attack Risk',color_discrete_sequence=px.colors.qualitative.Set3_r)
    st.plotly_chart(fig, use_container_width=True)

    previous_attack = df[df['Previous Heart Problems']==True].groupby('Diabetes')['Heart Attack Risk'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(previous_attack,x='Diabetes',y='Heart Attack Risk',color='Diabetes',title='Diabetes vs. Heart Attack Risk(had  heart problems)',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    Dieto = df[df['Previous Heart Problems']==True].groupby('Diet')['Heart Attack Risk'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(Dieto,x='Diet',y='Heart Attack Risk',color='Diet',title='Diet vs. Heart Attack Risk (had previous heart problems)',color_discrete_sequence=px.colors.qualitative.Set3_r,template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
    

  