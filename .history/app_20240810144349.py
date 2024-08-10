import streamlit as st 
import pickle 

st.title('Duplicate Question Predictor')
input_question = st.input('Enter the question:')

model = pickle.load(r'model.pkl', 'rb')

prediction_result = model.predict(input_question)