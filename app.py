import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

model = pickle.load(open('model1.pkl', 'rb'))

st.title("Diamond Price Prediction system")

input_Carat = st.number_input("Enter Carat")
input_Cut = st.number_input("Enter Cut")
input_Clarity = st.number_input("Enter Clarity")
input_Color = st.number_input("Enter Color")

if st.button('Predict'):
    st.header(model.predict([[input_Carat,input_Cut,input_Clarity,input_Color]])[0]*0.1)




# C:\Users\sahil\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\streamlit.exe run app.py


