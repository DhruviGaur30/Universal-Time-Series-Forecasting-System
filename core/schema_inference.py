#Automatically understand any dataset. 
# 1) Detects time column
# 2) Detects target column
# 3) Detects entity columns
# 4) Detects frequency

# core/schema_inference.py

import pandas as pd
import numpy as np
from core.schema import DatasetSchema

def infer_schema(df: pd.DataFrame) -> DatasetSchema:
    # 1. Time column detection
    time_candidates = [
        col for col in df.columns
        if 'date' in col.lower() or 'time' in col.lower()
    ]
    time_col = time_candidates[0]

    df[time_col] = pd.to_datetime(df[time_col])

    # 2. Target column detection (numeric, high variance)
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    target_col = df[numeric_cols].var().idxmax()

    # 3. Entity columns (categorical with repetition)
    entity_cols = [
        col for col in df.columns
        if df[col].dtype == 'object' or df[col].nunique() < 50
        if col not in [time_col, target_col]
    ]

    # 4. Frequency detection
    freq = pd.infer_freq(df[time_col]) or "D"

    return DatasetSchema(
        time_col=time_col,
        target_col=target_col,
        entity_cols=entity_cols,
        freq=freq,
        numeric_features=numeric_cols,
        categorical_features=entity_cols
    )
