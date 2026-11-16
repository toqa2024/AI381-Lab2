
import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = ROOT / "artifacts" / "model.joblib"
METADATA_PATH = ROOT / "artifacts" / "metadata.json"

model = joblib.load(MODEL_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as file:
    metadata = json.load(file)

app = FastAPI(title="AI381 Churn Prediction API")


class CustomerInput(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(gt=0)
    contract: str
    internet_service: str
    support_calls: int = Field(ge=0)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": metadata["model_version"],
    }


@app.post("/predict")
def predict(customer: CustomerInput):
    data = pd.DataFrame([customer.model_dump()])

    prediction = int(model.predict(data)[0])

    probabilities = model.predict_proba(data)[0]
    positive_class_index = list(model.classes_).index(1)
    churn_probability = float(probabilities[positive_class_index])

    return {
        "churn_prediction": prediction,
        "churn_probability": churn_probability,
    }
