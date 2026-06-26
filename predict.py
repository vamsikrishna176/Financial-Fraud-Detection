import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/fraud_model.pkl")

st.set_page_config(page_title="Financial Fraud Detection", page_icon="💳")

st.title("💳 Financial Fraud Detection")
st.write("Enter transaction details below to predict whether a transaction is Fraud or Normal.")

# User Inputs
time = st.number_input("Time", value=0.0)

features = []
for i in range(1, 29):
    value = st.number_input(f"V{i}", value=0.0)
    features.append(value)

amount = st.number_input("Amount", value=100.0)

# Predict Button
if st.button("Predict"):

    input_data = pd.DataFrame(
        [[time] + features + [amount]],
        columns=[
            "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
            "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
            "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")