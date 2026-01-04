from sklearn.ensemble import RandomForestRegressor

# Optional models (loaded safely)
try:
    from xgboost import XGBRegressor
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False

try:
    from catboost import CatBoostRegressor
    CAT_AVAILABLE = True
except ImportError:
    CAT_AVAILABLE = False


def get_model(model_name: str):
    """
    Returns a regression model based on user selection.
    Safe defaults, no crashes.
    """

    model_name = model_name.lower()

    if model_name == "randomforest":
        return RandomForestRegressor(
            n_estimators=300,
            max_depth=12,
            random_state=42,
            n_jobs=-1
        )

    elif model_name == "xgboost":
        if not XGB_AVAILABLE:
            raise ImportError(
                "XGBoost is not installed. Install with: pip install xgboost"
            )

        return XGBRegressor(
            n_estimators=400,
            learning_rate=0.05,
            max_depth=8,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="reg:squarederror",
            random_state=42,
            n_jobs=-1
        )

    elif model_name == "catboost":
        if not CAT_AVAILABLE:
            raise ImportError(
                "CatBoost is not installed. Install with: pip install catboost"
            )

        return CatBoostRegressor(
            iterations=500,
            learning_rate=0.05,
            depth=8,
            loss_function="RMSE",
            verbose=False,
            random_seed=42
        )

    else:
        raise ValueError(
            f"Unknown model '{model_name}'. "
            "Choose from: RandomForest, XGBoost, CatBoost"
        )
