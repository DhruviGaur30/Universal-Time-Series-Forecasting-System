# core/models.py
# Purpose: reusable ensemble model, 
# Target-agnostic and Entity-agnostic

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import numpy as np

class EnsembleModel:
    def __init__(self):
        self.models = {
            "rf": RandomForestRegressor(n_estimators=100),
            "xgb": XGBRegressor(n_estimators=200)
        }
        self.weights = {}

    def fit(self, X, y):
        scores = {}
        for name, model in self.models.items():
            model.fit(X, y)
            scores[name] = np.var(model.predict(X))

        total = sum(scores.values())
        self.weights = {k: v / total for k, v in scores.items()}

    def predict(self, X):
        preds = [
            self.models[k].predict(X) * self.weights[k]
            for k in self.models
        ]
        return np.sum(preds, axis=0)
