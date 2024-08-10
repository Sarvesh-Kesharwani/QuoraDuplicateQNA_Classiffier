import streamlit as st 
import pickle 

st.title('Duplicate Question Predictor')

model = pickle.load(r'model.pkl', 'rb')

model.predict()