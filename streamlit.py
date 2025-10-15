
import streamlit as st
from prediction import prediction_count
import calendar
from src.exception import CustomException
import sys

# Title
st.title("🚲 Number Rental Requests ")

# Input Section
st.header("📋 Input Features")

season = st.selectbox(
    "Season",
    options=[1, 2, 3, 4],
    format_func=lambda x: {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}[x]
)

weather = st.selectbox(
    "Weather Condition",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Clear / Few clouds / Partly cloudy",
        2: "Mist + Cloudy / Broken clouds",
        3: "Light Snow / Light Rain + Thunderstorm",
        4: "Heavy Rain + Ice / Snow + Fog"
    }[x]
)

temp = st.slider("Temperature (°C)", 0.0, 40.0, 22.5)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 55.0)
windspeed = st.slider("Windspeed (km/h)", 0.0, 50.0, 25.6)
casual = st.number_input("Casual Rider Count", min_value=0, value=120)

year = st.selectbox("Year", list(range(2024, 2029)))
month = st.slider("Month", 1, 12, 10)
max_day = calendar.monthrange(year, month)[1]
day = st.slider("Day", 1, max_day, min(15, max_day))

weekday = calendar.weekday(year, month, day)
weekday_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][weekday]
st.markdown(f"**Weekday:** {weekday_name}")

am_or_pm = st.radio(
    "Time of Day",
    options=[0, 1],
    format_func=lambda x: "AM" if x == 0 else "PM"
)

holidays = st.selectbox(
    "Is it a Holiday?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# Predict Button
st.markdown("---")
if st.button("📊 Predict Demand"):
    try:
        result = prediction_count(
            season, weather, temp, humidity, windspeed,
            casual, year, month, day, weekday, am_or_pm, holidays
        )
        st.success(f"📈 Predicted Rental Count: {result}")
    except Exception as e:
        custom_error = CustomException(e, sys)
        st.error("⚠️ Prediction failed. Please check your inputs.")
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"{custom_error}\n")


