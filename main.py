import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import time
import datetime
import plotly.graph_objects as go
import plotly.express as px
import requests




addr_state = ['CA', 'TX', 'NY', 'FL', 'IL', 'NJ', 'PA', 'OH', 'GA', 'NC', 'VA', 'MI', 'AZ', 'MD', 'MA', 'CO', 'WA', 'MN', 'IN', 'TN', 'MO', 'NV', 'CT', 'WI', 'AL', 'OR', 'SC', 'LA', 'KY', 'OK', 'KS', 'AR', 'UT', 'MS', 'NM', 'HI', 'NH', 'RI', 'WV', 'NE', 'DE', 'MT', 'DC', 'AK', 'WY', 'VT', 'SD', 'ME', 'ND ', 'ID']
purpose = ['debt_consolidation','credit_card','home_improvement','other','major_purchase',
           'medical','car','small_business','moving','vacation','house',
           'renewable_energy','wedding','educational']
verification_status = ["Source Verified","Not Verified","Verified"]
initial_list_status = ['w','f']
application_type  = ["Individual","Joint App"]
home_ownership= ["MORTGAGE","RENT","OWN","ANY","NONE"]



user_input = pd.DataFrame(columns=X_test.columns)
user_input['id'] = user_input['id'].astype(str)

loan_details = {
    'loan_amnt': 8000.0,
    'term': 36,
    'int_rate': 15.99,
    'installment': 300.50,
    'emp_length': 3.0,
    'annual_inc': 65000.0,
    'issue_d': 10.235,
    'zip_code': 92101,
    'dti': 18.5,
    'earliest_cr_line': 15.0,
    'open_acc': 10.0,
    'pub_rec': 0.0,
    'revol_bal': 5000.0,
    'revol_util': 30.5,
    'total_acc': 20.0
}

# Assign loan details to the first row of user_input DataFrame
for key, value in loan_details.items():
    user_input.at[0, key] = value

# Function to update user_input DataFrame based on addr_state selection
def update_user_input(user_input, value):
    if value in addr_state:
        user_input.at[0, f'addr_state_{value}'] = 1
    elif value in purpose:
#         if f'purpose_' in user_input.columns:
#             user_input.drop(columns=[f'purpose_'], inplace=True)
        user_input.at[0, f'purpose_{value.replace(" ", "_")}'] = 1
    elif value in verification_status:
        user_input.at[0, f'verification_status_{value.replace(" ", "_")}'] = 1
    elif value in initial_list_status:
        user_input.at[0, f'initial_list_status_{value}'] = 1
    elif value in application_type:
        user_input.at[0, f'application_type_{value.replace(" ", "_")}'] = 1
    elif value in home_ownership:
        user_input.at[0, f'home_ownership_{value}'] = 1
    
    return user_input


user_addr_state = input("Enter the addr_state: ")
user_input = update_user_input(user_input, user_addr_state)

purpose = input("Enter the loan purpose: ")
user_input = update_user_input(user_input, purpose)

verification_status = input("Enter the verification_status: ")
user_input = update_user_input(user_input, verification_status)

initial_list_status = input("Enter the initial_list_status: ")
user_input = update_user_input(user_input, initial_list_status)
                               
application_type = input("Enter the application_type: ")
user_input = update_user_input(user_input, application_type)

home_ownership = input("Enter the home_ownership: ")
user_input = update_user_input(user_input, home_ownership)

user_input.fillna(0, inplace=True)
user_input


# Dropdown menus for specific columns
user_addr_state = st.selectbox("Select addr_state:", addr_state)
purpose = st.selectbox("Select loan purpose:", purpose)
verification_status = st.selectbox("Select verification status:", verification_status)
initial_list_status = st.selectbox("Select initial list status:", initial_list_status)
application_type = st.selectbox("Select application type:", application_type)
home_ownership = st.selectbox("Select home ownership:", home_ownership)

# Update user_input based on dropdown selections
user_input = update_user_input(user_input, user_addr_state)
user_input = update_user_input(user_input, purpose)
user_input = update_user_input(user_input, verification_status)
user_input = update_user_input(user_input, initial_list_status)
user_input = update_user_input(user_input, application_type)
user_input = update_user_input(user_input, home_ownership)

# # Display the updated user input DataFrame
# st.write(user_input)

# Make predictions using the trained AutoML model
predictions = automl2.predict_proba(user_input)
prediction_percentage = 1- predictions[0][0] * 100
st.write(f"Probability of Default: {prediction_percentage:.2f}%")    

if __name__ == "__main__":
    main()
