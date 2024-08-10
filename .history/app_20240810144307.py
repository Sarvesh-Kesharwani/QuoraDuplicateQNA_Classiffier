import streamlit as st 
import pickle 

st.title('Duplicate Question Predictor')

pickle.load(r'model.pkl')