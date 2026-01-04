# core/insights.py
# Purpose: business-friendly insights(generic)

import numpy as np
import pandas as pd

def generate_insights(df, forecast, schema):
    growth = (
        forecast["forecast"].mean() /
        df[schema.target_col].mean() - 1
    ) * 100

    return {
        "growth_rate": round(growth, 2),
        "volatility": round(forecast["forecast"].std(), 2),
        "trend": "Upward" if growth > 0 else "Downward"
    }
