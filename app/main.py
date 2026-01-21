from fastapi import FastAPI, HTTPException
from app.utils import load_model
from joblib import load 
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

model = load_model()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(temperature: float, humidity: float):
    prediction = model.predict([[temperature, humidity]])

    return {"forecast_error": float(prediction[0])}

city_coords = {
    "Richmond": (49.166592, -123.133568),
    "Vancouver": (49.2827, -123.1207),
    "Surrey": (49.10635, -122.82509),
    "Gibsons": (49.39539, -123.50555),
    "Victoria": (48.407326, -123.329773)
}

class TemperatureRequest(BaseModel):
    city: str
    date: str

@app.post("/predict_temperature")
def predict_temperature(request: TemperatureRequest):
    city = request.city
    date = request.date

    if city not in city_coords:
        raise HTTPException(status_code=400, detail="City not supported")

    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format, use YY-MM-DD")

    month = dt.month
    day = dt.day

    pred = model.predict([[month, day]])[0]

    temp_str = f"{round(float(pred), 2)} C"

    return {"city": city, "date": date, "predicted_temperature": temp_str}