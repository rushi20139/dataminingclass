# prompt: give an app.py file with all features which i can deploy to the streamlit cloud using the svm_model.sav

# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the saved SVM model
model = pickle.load(open('svm_model.sav', 'rb'))  # Replace 'svm_model.sav' with your actual model file

# Create a title for your Streamlit app
st.title("Fraud Detection App")

# Define input fields for user data
st.header("Enter Claim Information")
# Replace these with the actual feature names from your dataset
Month = st.number_input("Month", min_value=1, max_value=12, value=1)
WeekOfMonth = st.number_input("Week of the Month", min_value=1, max_value=5, value=1)
DayOfWeek = st.number_input("Day of the Week", min_value=1, max_value=7, value=1)
Make = st.number_input("Make", min_value=1, max_value=100, value=1) # Replace with appropriate range
AccidentArea = st.number_input("Accident Area", min_value=1, max_value=100, value=1)
DayOfWeekClaimed = st.number_input("Day of Week Claimed", min_value=1, max_value=7, value=1)
MonthClaimed = st.number_input("Month Claimed", min_value=1, max_value=12, value=1)
WeekOfMonthClaimed = st.number_input("Week of Month Claimed", min_value=1, max_value=5, value=1)
Sex = st.number_input("Sex", min_value=1, max_value=2, value=1)
MaritalStatus = st.number_input("Marital Status", min_value=1, max_value=3, value=1)
Age = st.number_input("Age", min_value=18, max_value=100, value=30)
Fault = st.number_input("Fault", min_value=0, max_value=1, value=0)
PolicyType = st.number_input("Policy Type", min_value=1, max_value=4, value=1)
VehicleCategory = st.number_input("Vehicle Category", min_value=1, max_value=2, value=1)
VehiclePrice = st.number_input("Vehicle Price", min_value=1000, max_value=100000, value=10000)
PolicyNumber = st.number_input("Policy Number", min_value=1, max_value=1000, value=1)
RepNumber = st.number_input("Rep Number", min_value=1, max_value=1000, value=1)
Deductible = st.number_input("Deductible", min_value=500, max_value=5000, value=1000)
DriverRating = st.number_input("Driver Rating", min_value=1, max_value=4, value=3)
Days_Policy_Accident = st.number_input("Days Policy Accident", min_value=0, max_value=365, value=0)
Days_Policy_Claim = st.number_input("Days Policy Claim", min_value=0, max_value=365, value=0)
PastNumberOfClaims = st.number_input("Past Number of Claims", min_value=0, max_value=10, value=0)
AgeOfVehicle = st.number_input("Age of Vehicle", min_value=0, max_value=20, value=5)
AgeOfPolicyHolder = st.number_input("Age of Policy Holder", min_value=18, max_value=100, value=40)
PoliceReportFiled = st.number_input("Police Report Filed", min_value=0, max_value=1, value=0)
WitnessPresent = st.number_input("Witness Present", min_value=0, max_value=1, value=0)
AgentType = st.number_input("Agent Type", min_value=0, max_value=1, value=0)
NumberOfSuppliments = st.number_input("Number of Suppliments", min_value=0, max_value=10, value=0)
AddressChange_Claim = st.number_input("Address Change Claim", min_value=0, max_value=1, value=0)
NumberOfCars = st.number_input("Number of Cars", min_value=1, max_value=10, value=1)
Year = st.number_input("Year", min_value=1994, max_value=2015, value=2010)
BasePolicy = st.number_input("Base Policy", min_value=1, max_value=4, value=1)


# Create a button to make the prediction
if st.button("Predict Fraud"):
    # Create a Pandas DataFrame from the user input
    user_input = pd.DataFrame({
        "Month": [Month],
        "WeekOfMonth": [WeekOfMonth],
        "DayOfWeek": [DayOfWeek],
        "Make": [Make],
        "AccidentArea": [AccidentArea],
        "DayOfWeekClaimed": [DayOfWeekClaimed],
        "MonthClaimed": [MonthClaimed],
        "WeekOfMonthClaimed": [WeekOfMonthClaimed],
        "Sex": [Sex],
        "MaritalStatus": [MaritalStatus],
        "Age": [Age],
        "Fault": [Fault],
        "PolicyType": [PolicyType],
        "VehicleCategory": [VehicleCategory],
        "VehiclePrice": [VehiclePrice],
        "Deductible": [Deductible],
        "DriverRating": [DriverRating],
        "Days_Policy_Accident": [Days_Policy_Accident],
        "Days_Policy_Claim": [Days_Policy_Claim],
        "PastNumberOfClaims": [PastNumberOfClaims],
        "AgeOfVehicle": [AgeOfVehicle],
        "AgeOfPolicyHolder": [AgeOfPolicyHolder],
        "PoliceReportFiled": [PoliceReportFiled],
        "WitnessPresent": [WitnessPresent],
        "AgentType": [AgentType],
        "NumberOfSuppliments": [NumberOfSuppliments],
        "AddressChange_Claim": [AddressChange_Claim],
        "NumberOfCars": [NumberOfCars],
        "Year": [Year],
        "BasePolicy": [BasePolicy],
        
    })

    # Make the prediction using the loaded model
    prediction = model.predict(user_input)

    # Display the prediction
    if prediction[0] == 1:
        st.error("Fraudulent Claim Detected!")
    else:
        st.success("Claim is likely not fraudulent.")
