from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import os

X = np.array([[20, 50], [25, 60], [30, 70], [35, 80]])
Y = np.array([2, 3, 5, 6])

model = LinearRegression()
model.fit(X, Y)

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/example_model.joblib")

print("Dummy model saved to model/example_model.joblib")