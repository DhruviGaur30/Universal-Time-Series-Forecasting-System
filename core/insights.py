# core/insights.py
# Purpose: business-friendly insights(generic)

def generate_insights(df, forecast, schema):
    growth = (
        forecast["forecast"].mean() /
        df[schema.target_col].mean() - 1
    )

    volatility = forecast["forecast"].std()

    return {
        "growth_rate": round(growth * 100, 2),
        "volatility": round(volatility, 2),
        "trend": "Upward" if growth > 0 else "Downward"
    }
