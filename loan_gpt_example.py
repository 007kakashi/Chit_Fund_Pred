import pandas as pd
import streamlit as st
import joblib as jb
from xgboost import Booster 

# Load the XGBoost model from the .pkl file
model =jb.load('LoanPredictor.pkl')

st.title('Loan Eligibility Checker')

# Get user input for various loan information
income = st.number_input('Enter Applicant Salary')
co_income = st.number_input('Enter Co-Applicant Income')
loan_amount = st.number_input('Loan Amount')
duration = st.number_input('Duration of Loan')
credit_history = st.selectbox('Credit History',['Yes','No'])

# Convert credit history input to a binary value
if credit_history == 'Yes':
    credit_history = 1
else:
    credit_history = 0

# Create a dataframe with the user input
data = {'income':income,'co_income':co_income,'loan_amount':loan_amount,'duration':duration,'credit_history':credit_history}
data_df = pd.DataFrame(data, index=[0])

if st.button('Check Eligibility'):
    # Use the model to predict loan eligibility
    prediction = model.predict(data_df)
    # Convert prediction to binary value
    prediction = prediction[0] >= 0.5
    # Output the result to the user
    if prediction:
        st.success('Congratulations, you are eligible for the loan!')
    else:
        st.error('Sorry, you are not eligible for the loan.')
