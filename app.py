import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("weather_model.pkl", "rb"))

st.set_page_config(page_title="Weather Prediction", page_icon="🌤️")

st.title("🌤️ Weather Temperature Prediction")

st.write("Enter the weather details below.")

# User Inputs
dew_point = st.number_input(
    "Dew Point Temperature (°C)",
    value=10.0,
    step=0.5
)

humidity = st.number_input(
    "Relative Humidity (%)",
    value=60,
    step=1
)

wind_speed = st.number_input(
    "Wind Speed (km/h)",
    value=10,
    step=1
)

visibility = st.number_input(
    "Visibility (km)",
    value=20.0,
    step=0.1
)

pressure = st.number_input(
    "Pressure (kPa)",
    value=101.3,
    step=0.1
)

year = st.number_input(
    "Year",
    value=2026,
    step=1
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=7
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)

if st.button("Predict Temperature"):

    sample = np.array([[
        dew_point,
        humidity,
        wind_speed,
        visibility,
        pressure,
        year,
        month,
        day,
        hour
    ]])

    prediction = model.predict(sample)[0]

    st.success(f"🌡️ Predicted Temperature: {prediction:.2f} °C")
    st.info(f"🌡️ Temperature in Fahrenheit: {(prediction * 9/5 + 32):.2f} °F")