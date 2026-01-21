import joblib
import os

def load_model():
    model_path = os.path.join("model", "temperature_model.joblib")
    model = joblib.load(model_path)
    return model