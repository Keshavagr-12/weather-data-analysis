# 🌤️ Weather Data Analysis and Temperature Prediction

A Machine Learning project that analyzes historical weather data and predicts the temperature based on weather conditions using **Linear Regression**. The project also includes an interactive **Streamlit Web Application** for real-time predictions.

---

## 📌 Features

- Analyze historical weather data
- Perform Exploratory Data Analysis (EDA)
- Train a Linear Regression model
- Predict temperature based on user inputs
- Interactive Streamlit web application
- Display temperature in both Celsius and Fahrenheit

---

## 📂 Dataset

The dataset contains hourly weather observations with the following features:

- Dew Point Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)
- Visibility (km)
- Atmospheric Pressure (kPa)
- Month
- Day
- Hour

**Target Variable**

- Temperature (°C)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
weather-data-analysis/
│
├── app.py
├── Weather Prediction.ipynb
├── weather_model.pkl
├── Weather Data.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Keshavagr-12/weather-data-analysis.git
```

Move to the project directory

```bash
cd weather-data-analysis
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Model

Algorithm Used:

- Linear Regression

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---


## 🔮 Future Improvements

- Random Forest Regressor
- XGBoost Regressor
- LSTM for Time Series Forecasting
- Weather Forecast API Integration
- Better Feature Engineering
- Model Deployment on Streamlit Community Cloud

---

## 👨‍💻 Author

**Keshav Agrawal**

GitHub: https://github.com/Keshavagr-12

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
