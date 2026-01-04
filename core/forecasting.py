# core/forecasting.py
# Purpose : Generate future predictions generically.

# ==========================================================
# core/forecasting.py
# Universal, future-safe forecasting logic
# ==========================================================

import pandas as pd


def generate_forecast(
    *,
    df: pd.DataFrame,
    time_col: str,
    target_col: str,
    feature_cols: list,
    encoder,
    model,
    horizon: int = 14,
    freq: str = "D"
):
    """
    Generate future forecasts safely.
    Uses keyword-only arguments to avoid ordering bugs.
    """

    # Sort data
    df = df.sort_values(time_col).copy()

    # Last timestamp
    last_date = df[time_col].max()

    # Create future dates
    future_dates = pd.date_range(
        start=last_date,
        periods=horizon + 1,
        freq=freq
    )[1:]

    future_df = pd.DataFrame({time_col: future_dates})

    # Repeat last known feature values
    last_row = df.iloc[-1]

    for col in feature_cols:
        future_df[col] = last_row[col]

    # Recreate time features
    future_df["_year"] = future_df[time_col].dt.year
    future_df["_month"] = future_df[time_col].dt.month
    future_df["_week"] = future_df[time_col].dt.isocalendar().week.astype(int)
    future_df["_dayofweek"] = future_df[time_col].dt.dayofweek
    future_df["_day"] = future_df[time_col].dt.day

    # Encode features
    X_future = future_df[feature_cols]
    X_future_encoded = encoder.transform(X_future).astype(float)

    # Predict
    future_df["forecast"] = model.predict(X_future_encoded)

    return future_df[[time_col, "forecast"]]
