import streamlit as st
import numpy as np

def calculate_lifecycle_cost(initial_cost, energy_consumption, fuel_price, price_growth, lifespan):
    total_cost = initial_cost
    for year in range(1, lifespan + 1):
        total_cost += energy_consumption * fuel_price * (1 + price_growth) ** year
    return total_cost

def calculate_loan_payment(loan_amount, interest_rate, loan_term):
    monthly_rate = interest_rate / 12 / 100  # Convert annual rate to monthly decimal
    num_payments = loan_term * 12  # Total months
    if monthly_rate > 0:
        payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    else:
        payment = loan_amount / num_payments
    return payment * num_payments  # Total loan repayment

st.title("Hotel Hot Water System: LPG vs. Electric Lifecycle Cost Calculator")

st.sidebar.header("User Inputs")

# System selection
option = st.sidebar.radio("Select System Type", ("LPG", "Electric"))

# Inputs for both systems
initial_cost = st.sidebar.number_input("Initial Investment (£)", min_value=0, value=5000)
energy_consumption = st.sidebar.number_input("Annual Energy Consumption (kWh)", min_value=0, value=10000)
fuel_price = st.sidebar.number_input("Current Fuel Price (per kWh in £)", min_value=0.0, value=0.12)
price_growth = st.sidebar.slider("Annual Fuel Price Growth (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
lifespan = st.sidebar.slider("System Lifetime (years)", min_value=1, max_value=30, value=15)

# Loan option
use_loan = st.sidebar.checkbox("Use a Loan for Investment?")
if use_loan:
    loan_amount = st.sidebar.number_input("Loan Amount (£)", min_value=0, value=5000)
    interest_rate = st.sidebar.slider("Loan Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
    loan_term = st.sidebar.slider("Loan Term (years)", min_value=1, max_value=30, value=10)
    total_loan_cost = calculate_loan_payment(loan_amount, interest_rate, loan_term)
else:
    total_loan_cost = 0

# Lifecycle cost calculation
total_cost = calculate_lifecycle_cost(initial_cost, energy_consumption, fuel_price, price_growth, lifespan) + total_loan_cost

# Display results
st.subheader("Results")
st.write(f"**Total Lifecycle Cost for {option} System:** £{total_cost:,.2f}")
if use_loan:
    st.write(f"**Total Loan Repayment:** £{total_loan_cost:,.2f}")

# Conclusion
st.subheader("Conclusion")
if use_loan:
    st.write("Using a loan increases the total cost but allows spreading payments over time. Assess affordability based on monthly payments.")
else:
    st.write("Without a loan, upfront investment is required, but long-term costs may be lower.")
