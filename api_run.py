import requests

url = "http://127.0.0.1:8000/predict_temperature"

# add one or more of the following cities: Richmond, Vancouver, Surrey, Gibsons, Victoria
cities = ["Richmond", "Surrey", "Gibsons"]
date = "2026-01-21"

for city in cities:
    payload = {"city": city, "date": date}
    response = requests.post(url, json=payload)
    print(response.json())