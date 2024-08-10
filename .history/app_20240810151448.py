import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
# Set the title of the app
st.title('Duplicate Question Predictor')

# Input for the user to enter a question
input_question = st.text_input('Enter the question:')

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Check if the input question is not empty
if input_question:
    # Make a prediction
    prediction_result = model.predict([input_question])  # Wrap input in a list

    # Display the result based on the prediction
    if prediction_result[0] == 1:  # Access the first element of the prediction
        st.write('The question is a duplicate')
    else:
        st.write('The question is not a duplicate')
else:
    st.write('Please enter a question to get a prediction.')
