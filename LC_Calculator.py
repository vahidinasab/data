import numpy as np\
\
def lifecycle_cost(initial_cost, annual_energy_consumption, fuel_price, inflation_rate, lifespan):\
    total_cost = initial_cost\
    for year in range(lifespan):\
        total_cost += annual_energy_consumption * fuel_price * ((1 + inflation_rate) ** year)\
    return total_cost\
\
def co2_emissions(annual_energy_consumption, emission_factor, lifespan):\
    return annual_energy_consumption * emission_factor * lifespan\
\
st.title("Lifecycle Cost & CO2 Emissions Calculator")\
\
st.sidebar.header("Input Parameters")\
initial_cost_LPG = st.sidebar.number_input("Initial Cost (LPG) in GBP", 5000)\
initial_cost_electric = st.sidebar.number_input("Initial Cost (Electric) in GBP", 7000)\
annual_energy_consumption = st.sidebar.number_input("Annual Energy Consumption (kWh)", 20000)\
LPG_price = st.sidebar.number_input("LPG Price (GBP/kWh)", 0.09)\
electricity_price = st.sidebar.number_input("Electricity Price (GBP/kWh)", 0.25)\
inflation_rate = st.sidebar.slider("Inflation Rate (%)", 0.0, 10.0, 3.0) / 100\
lifespan = st.sidebar.slider("System Lifespan (years)", 1, 30, 15)\
CO2_LPG = st.sidebar.number_input("CO2 Emission Factor (LPG) kg CO2/kWh", 0.214)\
CO2_electric = st.sidebar.number_input("CO2 Emission Factor (Electric) kg CO2/kWh", 0.1)\
\
LPG_cost = lifecycle_cost(initial_cost_LPG, annual_energy_consumption, LPG_price, inflation_rate, lifespan)\
electric_cost = lifecycle_cost(initial_cost_electric, annual_energy_consumption, electricity_price, inflation_rate, lifespan)\
LPG_emissions = co2_emissions(annual_energy_consumption, CO2_LPG, lifespan)\
electric_emissions = co2_emissions(annual_energy_consumption, CO2_electric, lifespan)\
\
st.subheader("Results")\
st.write(f"**Total Lifecycle Cost (LPG):** \'a3\{LPG_cost:,.2f\}")\
st.write(f"**Total Lifecycle Cost (Electric):** \'a3\{electric_cost:,.2f\}")\
st.write(f"**Total CO2 Emissions (LPG):** \{LPG_emissions:,.2f\} kg CO2")\
st.write(f"**Total CO2 Emissions (Electric):** \{electric_emissions:,.2f\} kg CO2")\
\
if electric_cost < LPG_cost:\
    st.success("Switching to electric heating is cost-effective.")\
else:\
    st.warning("LPG remains cheaper over the lifetime.")\
\
if electric_emissions < LPG_emissions:\
    st.success("Electric heating significantly reduces carbon emissions.")}
