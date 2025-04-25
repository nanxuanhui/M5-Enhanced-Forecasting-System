# M5 Enhanced Forecasting System

This project presents an advanced forecasting dashboard for the M5 Forecasting Challenge, integrating deep learning, quantile regression, model explainability (SHAP), and business intelligence components.

## 📌 Project Overview

- **Goal**: Predict daily sales at Walmart stores across the U.S. with uncertainty estimation and actionable insights.
- **Challenge Source**: [M5 Forecasting - Accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy)
- **Tech Stack**: Python, LightGBM, Streamlit, SHAP, Pandas, Seaborn, Matplotlib

---

## 📊 Data Pipeline

- `processed_sales_data.pkl`: Cleaned and feature-enriched version of M5 sales data.
- `bi_dashboard_summary.csv`: Aggregated output with prediction intervals and error metrics for BI consumption.

---

## 🔍 Forecasting Methods

- **LightGBM Quantile Regression**  
  Trained 3 separate models to predict lower (10%), median (50%), and upper (90%) sales bounds.
- **Uncertainty Estimation**  
  Prediction intervals plotted to capture demand volatility.
- **Accuracy Metrics**  
  - RMSE (Root Mean Square Error)  
  - MAE (Mean Absolute Error)  
  - WAPE (Weighted Absolute Percentage Error)

---

## 🔎 Explainability

- **SHAP (SHapley Additive exPlanations)**  
  Interprets the median model to reveal feature contributions.
- **Top-N Error Diagnostics**  
  Highlights item-store combinations with highest forecasting error.

---

## 📈 Streamlit Dashboard Features

Launch via:
```bash
streamlit run PredictionStreamlit.py
