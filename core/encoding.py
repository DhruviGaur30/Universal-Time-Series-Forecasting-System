import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class FeatureEncoder:
    def __init__(self):
        self.categorical_cols = []
        self.numeric_cols = []
        self.encoder = None
        self.feature_names_ = None

    def fit(self, X: pd.DataFrame):
        """
        Learn categorical encodings and feature space.
        """

        # Identify categorical vs numeric
        self.categorical_cols = X.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        self.numeric_cols = X.select_dtypes(
            exclude=["object", "category"]
        ).columns.tolist()

        # Initialize encoder safely
        self.encoder = OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        )

        # Fit encoder only on categorical columns
        if self.categorical_cols:
            self.encoder.fit(X[self.categorical_cols])

            encoded_feature_names = self.encoder.get_feature_names_out(
                self.categorical_cols
            ).tolist()
        else:
            encoded_feature_names = []

        # Lock final feature order
        self.feature_names_ = self.numeric_cols + encoded_feature_names

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Transform data using learned feature space.
        """

        # Ensure all expected numeric columns exist
        for col in self.numeric_cols:
            if col not in X.columns:
                X[col] = 0

        numeric_df = X[self.numeric_cols].reset_index(drop=True)

        # Encode categorical features
        if self.categorical_cols:
            for col in self.categorical_cols:
                if col not in X.columns:
                    X[col] = "unknown"

            encoded = self.encoder.transform(X[self.categorical_cols])
            encoded_df = pd.DataFrame(
                encoded,
                columns=self.encoder.get_feature_names_out(
                    self.categorical_cols
                )
            )
        else:
            encoded_df = pd.DataFrame()

        final_df = pd.concat(
            [numeric_df, encoded_df],
            axis=1
        )

        # Enforce identical feature order
        return final_df[self.feature_names_]

    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Fit encoder and transform in one step.
        (Required for sklearn-style API compatibility)
        """
        self.fit(X)
        return self.transform(X)
