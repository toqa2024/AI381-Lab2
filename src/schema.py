
NUMERIC = [
    "tenure_months",
    "monthly_charges",
    "support_calls",
]

CATEGORICAL = [
    "contract",
    "internet_service",
]

FEATURES = NUMERIC + CATEGORICAL

TARGET = "churn"


def validate(df):
    required_columns = FEATURES + [TARGET]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df[TARGET].isna().any():
        raise ValueError("Target column contains missing values.")

    return df
