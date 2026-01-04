#Automatically understand any dataset. 
# 1) Detects time column
# 2) Detects target column
# 3) Detects entity columns
# 4) Detects frequency

# core/schema_inference.py

import pandas as pd
import numpy as np
from core.schema import DatasetSchema

def infer_schema(df):
    time_col = next(
        col for col in df.columns
        if "date" in col.lower() or "time" in col.lower()
    )

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    target_col = df[numeric_cols].var().idxmax()

    entity_cols = [
        col for col in df.columns
        if df[col].dtype == "object" and col not in [time_col]
    ]

    freq = pd.infer_freq(pd.to_datetime(df[time_col])) or "D"

    return DatasetSchema(time_col, target_col, entity_cols, freq)
