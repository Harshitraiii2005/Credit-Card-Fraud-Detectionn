import streamlit as st
import numpy as np
import joblib
import time
from PIL import Image

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Load trained Random Forest model
@st.cache_resource
def load_model():
    try:
        return joblib.load("best_model_rf.pkl")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Add background GIF and animations
background_gif = """
<style>
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
@keyframes glow {
    0% {box-shadow: 0 0 5px cyan;}
    50% {box-shadow: 0 0 20px cyan;}
    100% {box-shadow: 0 0 5px cyan;}
}
body {
    background: url("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif") center/cover no-repeat fixed;
    animation: fadeIn 2s ease-in-out;
}
[data-testid="stAppViewContainer"] {
    background: rgba(0, 0, 0, 0.6);  /* Semi-transparent overlay */
    padding: 20px;
    border-radius: 15px;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    visibility: hidden;  /* Hide default header */
}
button {
    animation: glow 1.5s infinite alternate;
    transition: transform 0.2s ease-in-out;
}
button:hover {
    transform: scale(1.05);
}
</style>
"""
st.markdown(background_gif, unsafe_allow_html=True)

# Header Section
st.image("https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif", width=200)
st.title("💳 Credit Card Fraud Detection")
st.markdown("### Detect fraudulent transactions with AI-powered insights.")

# Sidebar Info
st.sidebar.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=180)
st.sidebar.header("ℹ️ About Fraud Detection")
st.sidebar.write(
    "Credit card fraud detection helps identify suspicious transactions. "
    "High fraud probability means the transaction is likely fraudulent."
)
st.sidebar.write("🔹 **Tip:** Enter realistic values for accurate predictions.")

# Transaction Details
st.subheader("🛒 Transaction Details")
time_of_transaction = st.slider("⏳ Time of Transaction (seconds)", 0, 86400, 3600)
transaction_amount = st.number_input("💵 Transaction Amount ($)", min_value=0.0, value=50.0, step=0.1)

# Risk Factors
st.subheader("🚨 Fraud Risk Indicators")
spending_pattern = st.slider("📊 Card Holder's Spending Pattern (Risk Score)", 0.0, 1.0, 0.5)
location_consistency = st.slider("📍 Transaction Location Consistency (Risk Score)", 0.0, 1.0, 0.5)
card_expiry_risk = st.slider("📅 Card Expiry Risk Factor", 0.0, 1.0, 0.5)
unusual_merchant = st.selectbox("🛒 Unusual Merchant Code Usage?", ["No", "Yes"])
chargebacks = st.slider("📉 Past Chargebacks in Last 30 Days", 0, 10, 2)
velocity_score = st.slider("⚡ Transaction Velocity Score", 0.0, 1.0, 0.5)
international_transaction = st.radio("🌍 International Transaction?", ["No", "Yes"])
high_risk_merchant = st.radio("🔴 High-Risk Merchant Category?", ["No", "Yes"])
multiple_transactions = st.slider("🔄 Multiple Transactions in a Short Time", 0, 10, 1)
ip_risk_score = st.slider("🌐 Transaction IP Address Risk Score", 0.0, 1.0, 0.5)
device_match = st.slider("📱 Device ID Match Score", 0.0, 1.0, 0.5)
mismatched_billing = st.radio("🏠 Mismatched Billing and Shipping Address?", ["No", "Yes"])
past_fraud = st.radio("🚫 Past Fraudulent Transactions?", ["No", "Yes"])
unusual_time = st.radio("🌙 Unusual Transaction Timing (e.g., Midnight)?", ["No", "Yes"])
declined_transactions = st.slider("🚨 Repeated Declined Transactions", 0, 5, 0)
credit_utilization = st.slider("💳 Credit Limit Utilization (%)", 0, 100, 30)

# Additional Features
st.subheader("📌 Additional Risk Factors")
new_device_usage = st.radio("📱 New Device Used for Transaction?", ["No", "Yes"])
atm_withdrawal_risk = st.radio("🏧 ATM Withdrawal Risk?", ["No", "Yes"])
business_card_mismatch = st.radio("🏢 Business vs. Personal Card Mismatch?", ["No", "Yes"])
bank_internal_risk = st.slider("🏦 Bank's Internal Risk Score", -1.0, 1.0, 0.0)
geo_location_score = st.slider("📍 Geolocation Consistency Score", 0.0, 1.0, 0.5)
previous_account_locks = st.slider("🔒 Previous Account Lock Events", -1.0, 1.0, 0.0)

# Convert categorical inputs to numerical format
categorical_mapping = {"No": 0, "Yes": 1}
features = [
    time_of_transaction, transaction_amount, spending_pattern, location_consistency,
    card_expiry_risk, categorical_mapping[unusual_merchant], chargebacks, velocity_score,
    categorical_mapping[international_transaction], categorical_mapping[high_risk_merchant],
    multiple_transactions, ip_risk_score, device_match,
    categorical_mapping[mismatched_billing], categorical_mapping[past_fraud],
    categorical_mapping[unusual_time], declined_transactions, credit_utilization,
    categorical_mapping[new_device_usage], categorical_mapping[atm_withdrawal_risk],
    categorical_mapping[business_card_mismatch], bank_internal_risk, geo_location_score,
    previous_account_locks
]

# Ensure we match 29 features
while len(features) < 29:
    features.append(0.0)  # Fill missing features with 0

# Predict button
if st.button("🔍 Predict Fraud"):
    if model:
        try:
            data = np.array(features, dtype=float).reshape(1, -1)
            prediction = model.predict(data)[0]
            probability = model.predict_proba(data)[:, 1][0]

            st.subheader("📊 Prediction Result")
            if prediction == 1:
                st.error("🚨 Fraudulent Transaction Detected!")
                st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=200)
            else:
                st.success("✅ Legitimate Transaction")
                st.image("https://media.giphy.com/media/l0HlJ3jlV6r6jUgda/giphy.gif", width=200)
                
                # 🎉 Confetti animation for non-fraudulent transactions
                st.balloons()
            
            st.write(f"Fraud Probability: **{probability:.4f}**")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model not loaded properly. Please check your model file.")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed by **Harshit Rai** | 🚀 Powered by AI & ML")
