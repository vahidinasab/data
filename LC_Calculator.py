import streamlit as st
import numpy as np
from PIL import Image

# Load and display University of Salford logo
logo = Image.open("https://www.salford.ac.uk/themes/custom/uos/img/logo-horizontal.png")

st.set_page_config(page_title="Lifecycle Cost & Loan Calculator", page_icon="💡")

# Layout with logo in the top right corner
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Lifecycle Cost & Loan Calculator ⚡")
    st.subheader("Compare LPG vs. Electric for Hot Water Systems 🔥⚡")
with col2:
    st.image(logo, width=150)

st.markdown("---")

# User inputs for lifecycle cost comparison
st.subheader("Compare Lifecycle Costs 🏨")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### LPG System 🔥")
    lpg_initial = st.number_input("Initial Investment (£)", min_value=0.0, value=5000.0)
    lpg_fuel_cost = st.number_input("Annual LPG Cost (£)", min_value=0.0, value=2000.0)
    lpg_maintenance = st.number_input("Annual Maintenance (£)", min_value=0.0, value=500.0)
    lpg_price_growth = st.slider("LPG Price Growth Rate (% per year)", 0, 10, 3)

with col2:
    st.markdown("### Electric System ⚡")
    elec_initial = st.number_input("Initial Investment (£)", min_value=0.0, value=8000.0)
    elec_fuel_cost = st.number_input("Annual Electricity Cost (£)", min_value=0.0, value=1500.0)
    elec_maintenance = st.number_input("Annual Maintenance (£)", min_value=0.0, value=400.0)
    elec_price_growth = st.slider("Electricity Price Growth Rate (% per year)", 0, 10, 2)

years = st.slider("Project Lifetime (years)", 1, 30, 10)
inflation = st.slider("Inflation Rate (% per year)", 0, 10, 2)

def calculate_lifecycle_cost(initial, fuel_cost, maintenance, price_growth, years, inflation):
    total_cost = initial
    for year in range(1, years + 1):
        fuel_cost *= (1 + price_growth / 100)
        maintenance *= (1 + inflation / 100)
        total_cost += fuel_cost + maintenance
    return total_cost

if st.button("Calculate Lifecycle Costs ✅"):
    lpg_total = calculate_lifecycle_cost(lpg_initial, lpg_fuel_cost, lpg_maintenance, lpg_price_growth, years, inflation)
    elec_total = calculate_lifecycle_cost(elec_initial, elec_fuel_cost, elec_maintenance, elec_price_growth, years, inflation)
    
    st.markdown("### Results 📊")
    st.write(f"**Total Cost for LPG System:** £{lpg_total:,.2f} 🔥")
    st.write(f"**Total Cost for Electric System:** £{elec_total:,.2f} ⚡")
    
    if elec_total < lpg_total:
        st.success("Switching to electric will save money in the long run! ✅")
    else:
        st.warning("LPG might still be the cheaper option. Consider fuel price trends. ⚠️")

st.markdown("---")

# Loan Calculator
st.subheader("Loan Calculator 💰")
loan_amount = st.number_input("Loan Amount (£)", min_value=0.0, value=5000.0)
interest_rate = st.slider("Annual Interest Rate (% per year)", 0.1, 15.0, 5.0)
loan_term = st.slider("Loan Term (years)", 1, 30, 10)

def calculate_loan_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    months = years * 12
    if monthly_rate > 0:
        payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    else:
        payment = principal / months
    return payment * months, payment

if st.button("Calculate Loan Payments 💳"):
    total_payment, monthly_payment = calculate_loan_payment(loan_amount, interest_rate, loan_term)
    st.markdown("### Loan Repayment Details 🏦")
    st.write(f"**Monthly Payment:** £{monthly_payment:,.2f}")
    st.write(f"**Total Repayment Over {loan_term} Years:** £{total_payment:,.2f}")
