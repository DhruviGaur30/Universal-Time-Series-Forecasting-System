# 📈 Universal Sales Forecasting Engine

> **A production-ready, business-first forecasting platform that automatically builds accurate time-series forecasts from any sales, demand, or revenue dataset — without hardcoded columns, feature mismatch errors, or manual ML configuration.
> Built with a modern dashboard UI, explainable business KPIs, and a robust forecasting pipeline designed for real-world datasets.** 

## 🚀 Key Highlights

- 🔁 Works with any time-series dataset (sales / demand / revenue)
- 🧠 Automatic feature engineering (time features, lags, safe predictors)
- 🔐 Forecast-safe modeling (no data leakage)
- 🔄 Model-agnostic (Random Forest, XGBoost, CatBoost support)
- 📊 Executive-level KPIs & insights
- 🖥️ Modern dashboard UI built with Streamlit
- ⚙️ No hardcoded columns. No feature mismatch. No crashes.

## 🧩 What Problem Does This Solve?

Most forecasting solutions fail in practice because they:

- Break when column names change
- Require manual feature engineering
- Produce outputs that business users don't understand
- Are hard to reuse across datasets

This project solves that by providing a **universal forecasting engine** that:

- Adapts to the dataset structure at runtime
- Automatically selects safe, future-available features
- Translates predictions into business-ready insights
- Works end-to-end from CSV upload → decision-ready outputs

## 🏗️ System Architecture

```
CSV Dataset
   ↓
Schema & Column Mapping
   ↓
Robust Date Parsing (mixed formats)
   ↓
Forecast-Safe Feature Engineering
   ↓
Categorical Encoding
   ↓
Model Training (user-selected)
   ↓
Future Data Generation
   ↓
Forecast Prediction
   ↓
Business KPIs + Executive Summary
```

## 🧠 Core Features

### 1️⃣ Universal Dataset Handling

- Automatically detects time, target, and entity columns
- Handles inconsistent date formats safely
- Works across retail, e-commerce, finance, and operations datasets

### 2️⃣ Forecast-Safe Feature Engineering

The system only uses features that are known at prediction time:

- Time features (year, month, week, day, weekday)
- Lag features (lag-1, lag-7)
- Stable categorical/entity identifiers

This prevents data leakage, a common issue in forecasting systems.

### 3️⃣ Model Flexibility

Users can switch between:

- **Random Forest** (robust baseline)
- **XGBoost** (high-performance gradient boosting)
- **CatBoost** (excellent categorical handling)

The architecture allows easy future expansion.

### 4️⃣ Business-Focused KPIs

The dashboard automatically computes:

- Total Forecast
- Average Forecast
- Maximum & Minimum Forecast
- Forecast Growth %
- Volatility-based Risk Level

These metrics speak directly to business stakeholders, not just data scientists.

### 5️⃣ Executive Summary (Auto-Generated)

The system translates raw forecasts into:

- Trend direction (upward / downward)
- Short-term growth interpretation
- Risk assessment
- Expected value per period

This allows decision-makers to understand outcomes without reading charts.

## 📊 Dashboard Preview

The application provides:

- **Forecast vs Actual** visualization
- **KPI cards** for quick insights
- **Executive summary** for decision-making
- **Forecast table** for auditability

Designed with a modern, dark, professional UI optimized for demos and recruiters.

## 🧪 Example Datasets Supported

- Walmart Store Sales
- Retail Inventory & Demand Forecasting
- E-commerce Order History
- Subscription Revenue Time Series
- Financial Transaction Volumes

## 🛠️ Tech Stack

- Python
- Pandas / NumPy
- Scikit-Learn
- XGBoost / CatBoost
- Streamlit
- Plotly

## 📂 Project Structure

```
TS-Sales-Forecast/
│
├── app.py                 # Main dashboard UI & orchestration
├── core/
│   ├── forecasting.py     # Forecast generation logic
│   ├── encoding.py        # Robust categorical encoder
│   ├── models.py          # Model factory & wrappers
│   └── features.py        # Feature engineering
│
├── requirements.txt
└── README.md
```

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Upload a CSV → Map columns → Run forecast → View insights.

## 🎯 Business Use Cases

### 🏬 Retail & E-commerce

- Sales forecasting per store/product
- Inventory planning
- Promotion impact analysis

### 📦 Supply Chain

- Demand forecasting
- Stock optimization
- Risk assessment for shortages

### 💰 Finance & Strategy

- Revenue projections
- Trend & volatility analysis
- Executive reporting

### 📈 Operations

- Capacity planning
- Resource allocation
- Scenario planning

## 🌟 Why This Project Stands Out

✔ No fragile assumptions  
✔ No dataset-specific hacks  
✔ No black-box outputs  
✔ Designed for real business decisions

**This is not a demo — it is a reusable forecasting system.**

## 🧠 Future Enhancements

- SHAP-based explainability
- Scenario simulation (best / worst case)
- Automated report export (PDF)
- Model comparison metrics
- Forecast confidence intervals

## 👩‍💻 Author

Built with a strong focus on interpretability, robustness, and business impact.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show Your Support

Give a ⭐️ if this project helped you! 