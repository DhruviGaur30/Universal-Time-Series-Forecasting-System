# core/features.py
#Purpose: Frequency-aware feature engineering.
# Works for daily / weekly / monthly
# Generic lag & rolling features
import pandas as pd
import numpy as np

def create_features(df, schema):
    df = df.copy()

    df[schema.time_col] = pd.to_datetime(df[schema.time_col])

    # Time features (always safe)
    df["year"] = df[schema.time_col].dt.year
    df["month"] = df[schema.time_col].dt.month
    df["week"] = df[schema.time_col].dt.isocalendar().week.astype(int)
    df["day"] = df[schema.time_col].dt.day
    df["dayofweek"] = df[schema.time_col].dt.dayofweek

    # Lag features (safe)
    df["lag_1"] = df[schema.target_col].shift(1)
    df["lag_7"] = df[schema.target_col].shift(7)

    return df.dropna()
