import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



df = pd.read_csv(r"H:\mid_year_project\df_cleaned.csv")
numeric_columns = df.select_dtypes(include='number').columns
Categorical_columns = df.select_dtypes(include='O').columns


selected_country = st.selectbox('select your country', df['Country'].unique())
df_country = df[df['Country'] == selected_country].groupby('Age groups')['Heart Attack Risk'].mean().reset_index()
fig = px.bar(df_country, x='Age groups', y='Heart Attack Risk', color='Heart Attack Risk', title= f'Heart Attack Risk by Age for {selected_country}',width=800, height=400)
st.plotly_chart(fig) 

selected_feature = st.selectbox('select your feature',Categorical_columns)
second_feature = st.selectbox('select second feature', numeric_columns)
df_feature = df.groupby(selected_feature)[second_feature].mean().reset_index()
fig = px.bar(df_feature, x=selected_feature, y=second_feature, color=selected_feature)
st.plotly_chart(fig)
selected = st.selectbox('select your feature',numeric_columns)
fig = px.box(df, x=selected)
st.plotly_chart(fig)


  
