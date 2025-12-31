# app.py

import streamlit as st
import pandas as pd
from core.schema_inference import infer_schema
from core.validator import validate_data
from core.features import create_features
from core.models import EnsembleModel
from core.forecasting import generate_forecast
from core.insights import generate_insights

st.title("Universal Sales Forecasting Engine")

file = st.file_uploader("Upload dataset")

if file:
    df = pd.read_csv(file)
    schema = infer_schema(df)

    validation = validate_data(df, schema)
    if not validation["is_valid"]:
        st.error(validation["errors"])
        st.stop()

    df_feat = create_features(df, schema)

    X = df_feat.drop(columns=[schema.target_col, schema.time_col])
    y = df_feat[schema.target_col]

    model = EnsembleModel()
    model.fit(X, y)

    forecast = generate_forecast(df_feat, schema, model, horizon=8)
    insights = generate_insights(df, forecast, schema)

    st.dataframe(forecast)
    st.json(insights)
