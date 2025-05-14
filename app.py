import streamlit as st
import requests
from datetime import datetime

st.title("Economic Conditions Indicator")

# user inputs
now = datetime.now()
current_year = now.year
current_month = now.month

with st.expander("Year"):
    year = st.number_input("", min_value=2000, max_value=2100, value=current_year, key="year")

with st.expander("Month"):
    month = st.number_input("", min_value=1, max_value=12, value=current_month, key="month")

with st.expander("Business Applications"):
    business_applications = st.number_input(" ", key="business_applications")

with st.expander("Construction Spending"):
    construction_spending = st.number_input(" ", key="construction_spending")

with st.expander("Durable Goods New Orders"):
    durable_goods_new_orders = st.number_input(" ", key="durable_goods_new_orders")

with st.expander("International Trade - Exports"):
    exports = st.number_input(" ", key="exports")

with st.expander("International Trade - Imports"):
    imports = st.number_input(" ", key="imports")

with st.expander("Manufacturing Inventories"):
    manu_inventories = st.number_input(" ", key="manu_inventories")

with st.expander("Manufacturing New Orders"):
    manu_new_orders = st.number_input(" ", key="manu_new_orders")

with st.expander("New Homes for Sale"):
    new_homes_for_sale = st.number_input(" ", key="new_homes_for_sale")

with st.expander("New Homes Sold"):
    new_homes_sold = st.number_input(" ", key="new_homes_sold")

with st.expander("Residential Construction Permits"):
    res_const_permits = st.number_input(" ", key="res_const_permits")

with st.expander("Residential Units Completed"):
    res_const_units_completed = st.number_input(" ", key="res_const_units_completed")

with st.expander("Residential Units Started"):
    res_const_units_started = st.number_input(" ", key="res_const_units_started")

with st.expander("Retail Inventories"):
    retail_inventories = st.number_input(" ", key="retail_inventories")

with st.expander("Sales for Retail and Food"):
    sales_retail_food = st.number_input(" ", key="sales_retail_food")

with st.expander("Wholesale Inventories"):
    wholesale_inventories = st.number_input(" ", key="wholesale_inventories")

with st.expander("% Change CPI"):
    cpi_change = st.number_input(" ", key="cpi_change")

with st.expander("Composite Leading Indicator (CLI)"):
    cli = st.number_input(" ", key="cli")

with st.expander("% Change CLI"):
    cli_change = st.number_input(" ", key="cli_change")



if st.button("Determine Economic Regime"):
    user_data = {
        "Year": year,
        "Month": month,
        "BusinessApplications": business_applications,
        "ConstructionSpending": construction_spending,
        "DurableGoodsNewOrders": durable_goods_new_orders,
        "InternationalTrade_Exports": exports,
        "InternationalTrade_Imports": imports,
        "ManuInventories": manu_inventories,
        "ManuNewOrders": manu_new_orders,
        "NewHomesForSale": new_homes_for_sale,
        "NewHomesSold": new_homes_sold,
        "ResConstPermits": res_const_permits,
        "ResConstUnitsCompleted": res_const_units_completed,
        "ResConstUnitsStarted": res_const_units_started,
        "RetailInventories": retail_inventories,
        "SalesForRetailAndFood": sales_retail_food,
        "WholesaleInventories": wholesale_inventories,
        "PercentChangeCPI": cpi_change,
        "CLI": cli,
        "PercentChangeCLI": cli_change
    }
    user_data = {k: v for k, v in user_data.items() if v != -1.0} #only keep key/value pairs where value!= -1 (initial placeholder value)

    result = requests.post("http://localhost:8000/data/", json=user_data)

    if result.status_code == 200:
        regime = result.json()["regime"]
        st.success(f"The economy was determined to be in {regime}")
    else:
        st.error(f"Error from API :  {result.status_code} — {result.text}")

    
