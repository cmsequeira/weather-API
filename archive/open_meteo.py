import requests
from datetime import datetime

# Vancouver Coordinates
latitude = 49.166592
longitude = -123.133568

url = "https://archive-api.open-meteo.com/v1/archive"

params = {"latitude": latitude,
    "longitude": longitude,
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "daily": "temperature_2m_mean",
    "timezone": "auto"}

response = requests.get(url, params=params)
data = response.json()

dates = data["daily"]["time"]
temps = data["daily"]["temperature_2m_mean"]

rows = []
for date_str, temp in zip(dates, temps):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    rows.append({
        "month": date.month,
        "day": date.day,
        "avg_temp": temp
    })

for r in rows[:5]:
    print(r)

print(data["daily"].keys())