# core/forecasting.py

# Purpose : Generate future predictions generically.

import pandas as pd

def generate_forecast(df, schema, model, horizon):
    last_time = df[schema.time_col].max()
    future = pd.date_range(
        start=last_time,
        periods=horizon + 1,
        freq=schema.freq
    )[1:]

    future_df = pd.DataFrame({schema.time_col: future})

    X_future = future_df.drop(columns=[schema.time_col], errors="ignore")
    future_df["forecast"] = model.predict(X_future)

    return future_df
