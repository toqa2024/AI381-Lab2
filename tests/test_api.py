
from fastapi.testclient import TestClient

from src.app.main import app, model, CustomerInput

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_endpoint_returns_prediction():
    response = client.post(
        "/predict",
        json={
            "tenure_months": 12,
            "monthly_charges": 75.0,
            "contract": "month-to-month",
            "internet_service": "fiber",
            "support_calls": 3,
        },
    )
    assert response.status_code == 200
    assert response.json()["churn_prediction"] in [0, 1]


def test_model_is_loaded():
    assert model is not None


def test_input_schema_rejects_negative_tenure():
    response = client.post(
        "/predict",
        json={
            "tenure_months": -1,
            "monthly_charges": 75.0,
            "contract": "month-to-month",
            "internet_service": "fiber",
            "support_calls": 3,
        },
    )
    assert response.status_code == 422


def test_prediction_is_deterministic():
    customer = {
        "tenure_months": 12,
        "monthly_charges": 75.0,
        "contract": "one-year",
        "internet_service": "dsl",
        "support_calls": 1,
    }

    first_response = client.post("/predict", json=customer)
    second_response = client.post("/predict", json=customer)

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert (
        first_response.json()["churn_prediction"]
        == second_response.json()["churn_prediction"]
    )
