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

# Inputs for LPG system
st.sidebar.subheader("LPG System")
lpg_initial_cost = st.sidebar.number_input("LPG Initial Investment (£)", min_value=0, value=5000)
lpg_energy_consumption = st.sidebar.number_input("LPG Annual Energy Consumption (kWh)", min_value=0, value=10000)
lpg_fuel_price = st.sidebar.number_input("LPG Current Fuel Price (per kWh in £)", min_value=0.0, value=0.12)
lpg_price_growth = st.sidebar.slider("LPG Annual Fuel Price Growth (%)", min_value=0.0, max_value=10.0, value=2.0) / 100

# Inputs for Electric system
st.sidebar.subheader("Electric System")
elec_initial_cost = st.sidebar.number_input("Electric Initial Investment (£)", min_value=0, value=7000)
elec_energy_consumption = st.sidebar.number_input("Electric Annual Energy Consumption (kWh)", min_value=0, value=8000)
elec_fuel_price = st.sidebar.number_input("Electric Current Fuel Price (per kWh in £)", min_value=0.0, value=0.15)
elec_price_growth = st.sidebar.slider("Electric Annual Fuel Price Growth (%)", min_value=0.0, max_value=10.0, value=1.5) / 100

# System lifetime
lifespan = st.sidebar.slider("System Lifetime (years)", min_value=1, max_value=30, value=15)

# Lifecycle cost calculation
lpg_total_cost = calculate_lifecycle_cost(lpg_initial_cost, lpg_energy_consumption, lpg_fuel_price, lpg_price_growth, lifespan)
elec_total_cost = calculate_lifecycle_cost(elec_initial_cost, elec_energy_consumption, elec_fuel_price, elec_price_growth, lifespan)

# Display results
st.subheader("Comparison Results")
st.write(f"**Total Lifecycle Cost for LPG System:** £{lpg_total_cost:,.2f}")
st.write(f"**Total Lifecycle Cost for Electric System:** £{elec_total_cost:,.2f}")
if lpg_total_cost < elec_total_cost:
    st.write("LPG system appears to be more cost-effective over its lifetime.")
else:
    st.write("Electric system appears to be more cost-effective over its lifetime.")

# Loan option
st.subheader("Loan Calculator")
st.sidebar.subheader("Loan Inputs")
use_loan = st.sidebar.checkbox("Use a Loan for Investment?")
if use_loan:
    loan_amount = st.sidebar.number_input("Loan Amount (£)", min_value=0, value=5000)
    interest_rate = st.sidebar.slider("Loan Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
    loan_term = st.sidebar.slider("Loan Term (years)", min_value=1, max_value=30, value=10)
    total_loan_cost = calculate_loan_payment(loan_amount, interest_rate, loan_term)
    st.write(f"**Total Loan Repayment:** £{total_loan_cost:,.2f}")
    st.write("Using a loan increases the total cost but allows spreading payments over time. Assess affordability based on monthly payments.")
else:
    st.write("Without a loan, upfront investment is required, but long-term costs may be lower.")
