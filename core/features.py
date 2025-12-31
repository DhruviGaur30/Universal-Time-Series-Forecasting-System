# core/features.py
#Purpose: Frequency-aware feature engineering.
# Works for daily / weekly / monthly
# Generic lag & rolling features

import numpy as np

def create_features(df, schema):
    df = df.sort_values(schema.time_col)
    target = schema.target_col

    # Seasonal lag mapping
    seasonal_lag = {"D": 7, "W": 4, "M": 12}.get(schema.freq[0], 7)

    group = schema.entity_cols or [None]

    df["lag_1"] = df.groupby(group)[target].shift(1)
    df["lag_seasonal"] = df.groupby(group)[target].shift(seasonal_lag)

    df["rolling_mean"] = (
        df.groupby(group)[target]
        .shift(1)
        .rolling(3)
        .mean()
    )

    df = df.fillna(0)
    return df
