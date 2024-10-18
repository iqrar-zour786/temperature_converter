import streamlit as st

# Title of the app
st.title("Temperature Converter")

# Input: Temperature in Fahrenheit
fahrenheit = st.number_input("Enter temperature in Fahrenheit", format="%.2f")

# Conversion formula: Celsius = (Fahrenheit - 32) * 5/9
if st.button("Convert to Celsius"):
    celsius = (fahrenheit - 32) * 5 / 9
    st.success(f"{fahrenheit} °F is equal to {celsius:.2f} °C")
