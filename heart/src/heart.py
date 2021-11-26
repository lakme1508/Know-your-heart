import streamlit as st
import io
from model import logisticR
from utils import load_data
def write():
    st.title('Heart Disease Prediction')
    st.markdown('This is a demo of a machine learning model that predicts whether a person has heart disease.')
    st.markdown('**Data Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease)')
    st.markdown('**Model:** Logistic Regression')
    
    data = load_data()
    if st.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(data)
    
    st.subheader('Enter data to predict')
    #create input variables for age sex trestbps chol fbs restecg thalach exang oldpeak 
    
    age = st.number_input('Age', min_value=0, max_value=100)
    sex = st.number_input('Enter 1 for Male 0 for Female', min_value=0, max_value=1)
    bps = st.number_input("Enter Blood Pressue")
    chol = st.number_input("Enter cholestrol levels")
    ecg = st.number_input("Enter ecg reading")







    if st.button('Acc'):
        acc = logisticR(data)
        acc = acc.predict()
        st.write(acc)
