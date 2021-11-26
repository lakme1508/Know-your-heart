
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import logisticR
from utils import load_data
def write():
    st.title('KNOW YOUR HEART!!')
    st.markdown('This is a demo of a machine learning model that predicts whether a person has heart disease.')
    st.markdown('**Data Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease)')


    df = load_data()
    daf = pd.DataFrame(df[:200])

    if st.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(df)

    if st.checkbox('Show data description'):
        st.subheader('Data Description')
        st.write(df.describe())

    if st.checkbox('Show data head'):
        st.subheader('Data Head')
        st.write(df.head())

    if st.checkbox('Show data tail'):
        st.subheader('Data Tail')
        st.write(df.tail())

    if st.checkbox('Show data info'):
        st.subheader('Data Info')
        st.write(df.info())

    if st.checkbox('Show data correlation'):
        st.subheader('Data Correlation')
        st.write(df.corr())

    if st.checkbox('Show data histogram'):
        st.subheader('Data Histogram')
        #st.write(df.hist())
        #st.bar_chart(df)
        #df = pd.DataFrame(weekly_data[:200], columns = [‘num_orders’,’checkout_price’,’base_price’])
        daf.hist()
        plt.show()
        st.pyplot()


    if st.checkbox('Show data density'):
        st.subheader('Data Density')
        st.write(df.plot(kind='density', subplots=True))

    if st.checkbox('Show data boxplot'):
        st.subheader('Data Boxplot')
        st.write(df.plot(kind='box', subplots=True))

    if st.checkbox('Show data scatterplot'):
        st.subheader('Data Scatterplot')
        st.write(df.scatter())

    