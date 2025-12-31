# core/schema.py
#Purpose: Defines what the dataset means, not how it’s named.
#Replaces hard-coded column assumptions
#Central contract used by all modules

class DatasetSchema:
    def __init__(
        self,
        time_col: str,
        target_col: str,
        entity_cols: list,
        freq: str,
        numeric_features: list,
        categorical_features: list
    ):
        self.time_col = time_col
        self.target_col = target_col
        self.entity_cols = entity_cols
        self.freq = freq
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
