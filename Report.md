# M5 Enhanced Forecasting System

## 1. Project Background
The M5 Forecasting Challenge aims to promote high-accuracy retail sales forecasting. The challenge is to predict daily sales of Walmart products across several U.S. states for the next 28 days. Traditional forecasting methods often provide only point estimates, ignoring uncertainty and explainability.

This project delivers an interactive dashboard with business-awareness, enhancing not only predictive accuracy but also interpretability and decision support.

---

## 2. Data Sources and Preprocessing
- Source: Kaggle M5 Forecasting Challenge
- Includes: store, product, price, events, calendar, and sales data
- Feature engineering: lag features, rolling means, promo effects, holiday flags
- Processed outputs: `processed_sales_data.pkl` and `bi_dashboard_summary.csv`

---

## 3. Method Summary
### 🔢 Forecasting Model
- Quantile regression with LightGBM:
  - `0.1` → lower bound prediction
  - `0.5` → median prediction (main output)
  - `0.9` → upper bound prediction
- Daily prediction intervals `[Q10, Q90]` generated
- Data points outside intervals flagged for inventory alert

### 🧠 Model Explainability
- SHAP used to explain feature contributions to the median model
- Top features: `sales_lag_7`, `rolling_mean_7`, `price_change`

### 📉 Error Analysis
- Mean absolute error (MAE) per `item_id` and `store_id`
- Top-N error contributors visualized to guide model improvement

---

## 4. Streamlit Dashboard
```bash
streamlit run m5_streamlit_dashboard.py
```
Dashboard features:

| Module | Description |
|--------|-------------|
| 📈 Sales Trend Plot | Shows median prediction, confidence interval, and actual sales |
| 🎯 Accuracy Panel   | Displays RMSE, MAE, WAPE |
| 🚨 Inventory Alerts | Marks dates at risk of understock or overstock |
| 🧭 Filter Panel     | Select by product and store |

---

## 5. Evaluation Metrics
| Metric | Description | Example Value |
|--------|-------------|----------------|
| RMSE   | Root Mean Square Error | ~2.31 |
| MAE    | Mean Absolute Error    | ~1.83 |
| WAPE   | Weighted Absolute Percentage Error | ~13.2% |

---

## 6. Business Recommendations
| Scenario | Suggested Action |
|----------|------------------|
| Product A in Store B exceeds upper bound repeatedly | Consider pre-replenishment |
| Product C in Store D stays below lower bound often  | Consider promotion or reduce order quantity |
| Store E shows high forecast errors | Retrain with customized local model |

---

## 7. Future Work
- Enable multi-day rolling forecasts (e.g. 28-day horizon)
- Integrate inventory and price simulation for replenishment planning
- Connect with Tableau / Power BI for automated reporting
- Explore deep time-series models (e.g. Temporal Fusion Transformer)

---

## 8. Appendix
- `bi_dashboard_summary.csv` → BI-friendly prediction dataset
- `quantile_prediction_intervals.png` → Forecast interval visualization
- `shap_summary_median_model.png` → SHAP feature importance plot
- `top10_item_errors.png` / `top10_store_errors.png` → High-error entities
- `m5_streamlit_dashboard.py` → Main Streamlit app file


