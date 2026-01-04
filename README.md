# 🚀 Universal Sales Forecasting Engine

A **production-ready, universal time-series forecasting platform** that works on **any sales, demand, or revenue dataset** — without hardcoded columns, fragile pipelines, or feature mismatches.

Built with **Streamlit + Python**, this system automatically understands datasets, engineers forecast-safe features, trains advanced ML models, and delivers business-ready insights through an interactive dashboard.

---

## ✨ Why This Project Exists

Most forecasting projects:
- Break when column names change  
- Assume fixed schemas  
- Fail during inference due to feature mismatch  
- Are unusable by non-technical stakeholders  

**This engine solves all of that.**

You upload **any time-series dataset**, map columns visually, and the system handles everything else — **robustly and safely**.

---

## 🧠 What This Engine Does

✔ Works with **any CSV time-series dataset**  
✔ No hardcoded feature names  
✔ Automatic schema understanding  
✔ Forecast-safe feature engineering  
✔ Multiple model choices  
✔ Interactive visual dashboard  
✔ Business-friendly insights  

---

## 🔄 End-to-End Pipeline

### 1. Dataset Understanding
- Automatically reads dataset structure
- Displays row count, column count, and preview
- Supports mixed date formats safely

### 2. Schema Mapping (User-Driven)
- Select:
  - Time column (date)
  - Target column (sales / demand / revenue)
  - Entity columns (store, product, region, etc.)
  - Data frequency (daily / weekly / monthly)
- No assumptions — everything is explicit and safe

### 3. Forecast-Safe Feature Engineering
- Calendar features (year, month, week, day)
- Lag features (lag-1, lag-7)
- Removes leakage-prone future features
- Ensures **train & inference feature parity**

### 4. Robust Encoding
- Handles categorical & numeric features
- Guarantees identical feature sets during training & forecasting
- Prevents missing-column crashes

### 5. Model Training (User Selectable)
Supported models:
- **Random Forest**
- **XGBoost**
- **CatBoost**

Each model uses tuned defaults for speed and accuracy.

### 6. Forecast Generation
- Future date creation based on frequency
- Predicts future values safely
- Zero feature mismatch errors

### 7. Visualization & Business Insights
- Forecast vs Actual plot
- KPI cards (Avg / Max / Min / Growth)
- Downloadable forecast table

---

## 📊 Dashboard Preview

Features:
- Forecast vs Actual line chart
- Business KPI summary
- Interactive forecast table
- Dark, modern, professional UI

---

## 🧪 Example Datasets Supported

- Walmart sales datasets
- Retail inventory data
- Revenue tracking data
- Demand forecasting datasets
- Any structured time-series CSV

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **ML:** Scikit-learn, XGBoost, CatBoost
- **Data:** Pandas, NumPy
- **Visualization:** Plotly
- **Architecture:** Modular, schema-agnostic pipeline

---

## ▶ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
