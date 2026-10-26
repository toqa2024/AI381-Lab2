
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Find the main project folder
ROOT = Path(__file__).resolve().parents[2]

# Load the Lab 1 training data
data_path = ROOT / "data" / "churn_v1.csv"
df = pd.read_csv(data_path)

# Prepare the features and target
X = df[
    [
        "tenure_months",
        "monthly_charges",
        "contract",
        "internet_service",
        "support_calls",
    ]
]
y = df["churn"]

# Preprocess categorical and numerical columns
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            ["contract", "internet_service"],
        ),
        (
            "numerical",
            "passthrough",
            ["tenure_months", "monthly_charges", "support_calls"],
        ),
    ]
)

# Create and train the model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(X, y)

# Save the trained model
model_path = ROOT / "models" / "churn_model.joblib"
model_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, model_path)

print("Model trained successfully!")
print(f"Model saved to: {model_path}")
