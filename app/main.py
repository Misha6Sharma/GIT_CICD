# Import libraries
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Define path to save/load model
MODEL_PATH = "app/model.pkl"

# 1️⃣ Train model if not exists
if not os.path.exists(MODEL_PATH):
    iris = load_iris()
    X, y = iris.data, iris.target

    # Simple Random Forest
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)

    # Save trained model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

# 2️⃣ Load the trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# 3️⃣ FastAPI app setup
app = FastAPI(title="Iris Flower Classifier API")

# 4️⃣ Input data format
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 5️⃣ Health check endpoint
@app.get("/")
def root():
    return {"message": "Iris model API is running!"}

# 6️⃣ Prediction endpoint
@app.post("/predict")
def predict(features: IrisFeatures):
    X_new = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    pred = model.predict(X_new)[0]
    return {"prediction": int(pred)}
