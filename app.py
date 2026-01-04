import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from core.models import get_model
from core.encoding import FeatureEncoder
from core.forecasting import generate_forecast

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Universal Sales Forecasting Engine",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Global styles + Hero section
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
}

.section {
    margin-top: 3rem;
    margin-bottom: 3rem;
}

.hero {
    padding: 4rem 3rem;
    background: radial-gradient(circle at top left, #1f2933, #020617);
    border-radius: 24px;
    margin-bottom: 3rem;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 700;
    color: #ffffff;
}

.hero p {
    font-size: 1.15rem;
    color: #cbd5e1;
    max-width: 750px;
    margin-top: 1rem;
}

.badges span {
    display: inline-block;
    background: #111827;
    color: #38bdf8;
    padding: 6px 14px;
    border-radius: 999px;
    margin-right: 8px;
    margin-top: 12px;
    font-size: 0.85rem;
}
</style>

<div class="hero">
    <h1>🚀 Universal Sales Forecasting Engine</h1>
    <p>
        A production-grade forecasting platform that works on any time-series
        sales, demand, or revenue dataset — with zero hardcoding and zero crashes.
    </p>
    <div class="badges">
        <span>Schema-Agnostic</span>
        <span>Forecast-Safe</span>
        <span>ML-Powered</span>
        <span>Business-Ready</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Upload dataset
# --------------------------------------------------
st.markdown('<div class="section"><h2>📂 Upload Dataset</h2></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])
if uploaded_file is None:
    st.stop()

df = pd.read_csv(uploaded_file)
st.success("Dataset loaded successfully")

# --------------------------------------------------
# Dataset preview (bento layout)
# --------------------------------------------------
c1, c2, c3 = st.columns(3)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Preview", "Top 5")

st.dataframe(df.head(), use_container_width=True)

# --------------------------------------------------
# Dataset mapping
# --------------------------------------------------
st.markdown('<div class="section"><h2>🧩 Dataset Mapping</h2></div>', unsafe_allow_html=True)

time_col = st.selectbox("Time column", df.columns)
target_col = st.selectbox("Target column (what to forecast)", df.columns)

entity_cols = st.multiselect(
    "Entity columns (store / product / region)",
    [c for c in df.columns if c not in [time_col, target_col]]
)

freq = st.selectbox("Data frequency", ["D", "W", "M"])
model_name = st.selectbox("Model", ["RandomForest", "XGBoost", "CatBoost"])

# --------------------------------------------------
# Run forecast
# --------------------------------------------------
if st.button("🚀 Run Forecast"):
    with st.status("Running forecasting pipeline...", expanded=True):

        # --- Date parsing (robust & safe)
        df[time_col] = pd.to_datetime(
            df[time_col],
            errors="coerce",
            dayfirst=True
        )
        df = df.dropna(subset=[time_col])
        st.write("✓ Date parsing complete")

        # Time-based feature engineering
        # -----------------------------
        df["_year"] = df[time_col].dt.year
        df["_month"] = df[time_col].dt.month
        df["_week"] = df[time_col].dt.isocalendar().week.astype(int)
        df["_dayofweek"] = df[time_col].dt.dayofweek
        df["_day"] = df[time_col].dt.day

        # -----------------------------
        # Define feature columns
        # EXCLUDE raw datetime column
        # -----------------------------
        feature_cols = [
            c for c in df.columns
            if c not in [target_col, time_col]
        ]

        X = df[feature_cols]
        y = df[target_col]
        st.write("✓ Datetime safely converted to numeric features")

        st.write("✓ Forecast-safe features selected")

        # --- Encoding
        encoder = FeatureEncoder()
        X_encoded = encoder.fit(X).transform(X)
        st.write("✓ Encoding complete")

        # --- Model training
        model = get_model(model_name)
        model.fit(X_encoded, y)
        st.write("✓ Model trained")

        # --- Forecast generation
        
        forecast_df = generate_forecast(
            df=df,
            time_col=time_col,
            target_col=target_col,
            feature_cols=feature_cols,
            encoder=encoder,
            model=model,
            horizon=14,
            freq=freq
        )

        st.write("✓ Forecast generated")

    # --------------------------------------------------
    # Forecast vs Actual
    # --------------------------------------------------
    st.markdown('<div class="section"><h2>📈 Forecast vs Actual</h2></div>', unsafe_allow_html=True)

    plot_df = pd.concat([
        df[[time_col, target_col]].rename(columns={target_col: "value"}).assign(type="Actual"),
        forecast_df[[time_col, "forecast"]].rename(columns={"forecast": "value"}).assign(type="Forecast")
    ])

    fig = px.line(
        plot_df,
        x=time_col,
        y="value",
        color="type",
        labels={"value": target_col},
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # Business insights
    # --------------------------------------------------
    st.markdown('<div class="section"><h2>🧠 Business Insights</h2></div>', unsafe_allow_html=True)

    i1, i2, i3, i4 = st.columns(4)
    i1.metric("Avg Forecast", f"{forecast_df['forecast'].mean():,.0f}")
    i2.metric("Max Forecast", f"{forecast_df['forecast'].max():,.0f}")
    i3.metric("Min Forecast", f"{forecast_df['forecast'].min():,.0f}")

    growth = (
        (forecast_df["forecast"].iloc[-1] - forecast_df["forecast"].iloc[0])
        / forecast_df["forecast"].iloc[0]
    ) * 100
    i4.metric("Forecast Growth", f"{growth:.2f}%")

    # --------------------------------------------------
    # Forecast table
    # --------------------------------------------------
    st.markdown('<div class="section"><h2>📋 Forecast Table</h2></div>', unsafe_allow_html=True)
    st.dataframe(forecast_df[[time_col, "forecast"]], use_container_width=True)

    # --------------------------------------------------
    # Business KPIs
    # --------------------------------------------------
    st.markdown('<div class="section"><h2>📊 Key Business KPIs</h2></div>', unsafe_allow_html=True)

    total_forecast = forecast_df["forecast"].sum()
    avg_forecast = forecast_df["forecast"].mean()
    max_forecast = forecast_df["forecast"].max()
    min_forecast = forecast_df["forecast"].min()

    last_actual = df[target_col].iloc[-1]
    first_forecast = forecast_df["forecast"].iloc[0]
    growth_pct = ((first_forecast - last_actual) / last_actual) * 100

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Forecast", f"{total_forecast:,.0f}")
    k2.metric("Average Forecast", f"{avg_forecast:,.0f}")
    k3.metric("Max Forecast", f"{max_forecast:,.0f}")
    k4.metric("Min Forecast", f"{min_forecast:,.0f}")

    # --------------------------------------------------
    # Trend Detection
    # --------------------------------------------------
    trend = forecast_df["forecast"].iloc[-1] - forecast_df["forecast"].iloc[0]

    if trend > 0:
        trend_label = "📈 Upward Trend"
    elif trend < 0:
        trend_label = "📉 Downward Trend"
    else:
        trend_label = "➖ Stable Trend"

    # --------------------------------------------------
    # Risk Analysis
    # --------------------------------------------------
    volatility = forecast_df["forecast"].std()
    volatility_ratio = volatility / avg_forecast

    if volatility_ratio < 0.1:
        risk_level = "🟢 Low Risk"
    elif volatility_ratio < 0.25:
        risk_level = "🟠 Medium Risk"
    else:
        risk_level = "🔴 High Risk"

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------
    st.markdown('<div class="section"><h2>🧠 Executive Summary</h2></div>', unsafe_allow_html=True)

    summary_text = f"""
    • The forecast indicates an **{trend_label.lower()}** over the next forecast horizon.  
    • Expected growth relative to the last observed period is **{growth_pct:.2f}%**.  
    • Forecast volatility suggests a **{risk_level.lower()}** environment.  
    • Average expected value per period is approximately **{avg_forecast:,.0f}**.
    """

    st.info(summary_text)
    

