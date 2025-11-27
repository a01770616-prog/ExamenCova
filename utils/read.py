import streamlit as st
import pandas as pd

@st.cache_data
def data_reader():
    return pd.read_csv("data/exam_data.csv")