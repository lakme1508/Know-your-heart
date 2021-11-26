import pandas as pd
import streamlit as st
@st.cache(persist=True)
def load_data():
        data = pd.read_csv('../data/heart.csv')
        return data
