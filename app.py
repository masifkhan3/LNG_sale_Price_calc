import streamlit as st

def calculate_lng_rate(brent_price_avg, brent_to_lng_percent=16.65):
    """
    Calculate LNG Rate in $/MMBTU based on Brent crude oil price and Brent to LNG percentage.

    Parameters:
    brent_price_avg (float): Average Brent crude oil price in $/bbl.
    brent_to_lng_percent (float): Fixed percentage to convert Brent price to LNG rate (default: 16.65%).

    Returns:
    float: LNG rate in $/MMBTU.
    """
    lng_rate = brent_price_avg * (brent_to_lng_percent / 100)
    return round(lng_rate, 4)

# Streamlit app
st.title("LNG Sale Price Calculator")
st.write("""
This app calculates the LNG (Liquefied Natural Gas) in $/mmbtu sale price based on Brent crude oil prices.

""")

# Input: Data for last three months
st.subheader("Enter Brent Crude Oil Prices")
data = []
for i in range(1, 4):
    col1, col2 = st.columns(2)
    with col1:
        month_year = st.text_input(f"Month and Year for Month {i} (e.g., 'December 2024')", key=f"month_{i}")
    with col2:
        price = st.number_input(f"Average Brent crude oil price for {month_year} ($/bbl)", 
                                min_value=0.0, value=0.0, step=0.1, key=f"price_{i}")
    if month_year and price > 0.0:
        data.append((month_year, price))

# Calculate and display results if all data is entered
if len(data) == 3:
    st.subheader("Results")
    
    # Calculate average Brent price
    brent_price_avg = sum(price for _, price in data) / len(data)
    
    # Calculate LNG rate
    lng_rate = calculate_lng_rate(brent_price_avg)
    
    # Display input data
    st.write("### Input Data")
    st.write("| Month/Year      | Brent Price ($/bbl) |")
    st.write("|-----------------|---------------------|")
    for month_year, price in data:
        st.write(f"| {month_year} | {price:.2f} |")
    
    # Display calculations
    st.write(f"**Average Brent Price:** ${brent_price_avg:.4f} per barrel")
    st.write(f"**LNG Rate:** ${lng_rate:.4f} per MMBTU")
else:
    st.info("Please enter data for all three months to calculate the LNG Sale Price.")
