
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "models" / "churn_model.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(title="AI381 Churn Prediction API")


class CustomerInput(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(gt=0)
    contract: str
    internet_service: str
    support_calls: int = Field(ge=0)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(customer: CustomerInput):
    data = pd.DataFrame([customer.model_dump()])
    prediction = int(model.predict(data)[0])

    return {"churn_prediction": prediction}
