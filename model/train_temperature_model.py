import requests
import joblib
import os
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

# Vancouver Coordinates
latitude = 49.166592
longitude = -123.133568

url = "https://archive-api.open-meteo.com/v1/archive"

params = {"latitude": latitude,
    "longitude": longitude,
    "start_date": "2010-01-01",
    "end_date": "2024-12-31",
    "daily": "temperature_2m_mean",
    "timezone": "auto"}

response = requests.get(url, params=params)
data = response.json()

dates = data["daily"]["time"]
temps = data["daily"]["temperature_2m_mean"]

X = []
Y = []

for date_str, temp in zip(dates, temps):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    X.append([date.month, date.day])
    Y.append(temp)

X = np.array(X)
Y = np.array(Y)

model = LinearRegression()
model.fit(X, Y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/temperature_model.joblib")

print("Temperature model saved to model/temperature_model.joblib")