# core/schema.py
#Purpose: Defines what the dataset means, not how it’s named.
#Replaces hard-coded column assumptions
#Central contract used by all modules

class ForecastSchema:
    def __init__(self, time_col, target_col, entity_cols, freq):
        self.time_col = time_col
        self.target_col = target_col
        self.entity_cols = entity_cols
        self.freq = freq

    def is_future_safe(self, col):
        # Explicitly unsafe
        unsafe_keywords = [
            "price", "discount", "promo", "competitor",
            "forecast", "demand", "sales"
        ]
        return not any(k in col.lower() for k in unsafe_keywords)

