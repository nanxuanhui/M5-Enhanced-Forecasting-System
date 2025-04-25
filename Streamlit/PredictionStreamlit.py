{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "573853e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0eebd128",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-24 21:21:07.351 No runtime found, using MemoryCacheStorageManager\n",
      "2025-04-24 21:21:07.575 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.606 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.607 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.609 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.609 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.610 Session state does not function when running a script without `streamlit run`\n",
      "2025-04-24 21:21:07.610 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.610 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.640 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.640 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.641 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.643 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.644 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.644 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.656 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.657 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.669 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.766 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.766 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.766 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-24 21:21:07.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Load precomputed summary data\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    return pd.read_csv(\"/Users/nanxuan/Desktop/M5 Enhanced Forecasting System/Model_Prediction/bi_dashboard_summary.csv\")\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "st.title(\"M5 Forecasting Dashboard with Uncertainty and Explainability\")\n",
    "\n",
    "# Sidebar: Filters\n",
    "st.sidebar.header(\"Filter Options\")\n",
    "selected_store = st.sidebar.selectbox(\"Select Store\", df[\"store_id\"].unique())\n",
    "selected_item = st.sidebar.selectbox(\"Select Item\", df[\"item_id\"].unique())\n",
    "\n",
    "# Filtered view\n",
    "df_filtered = df[(df[\"store_id\"] == selected_store) & (df[\"item_id\"] == selected_item)]\n",
    "\n",
    "st.subheader(\"Forecast Confidence Interval\")\n",
    "fig, ax = plt.subplots(figsize=(10, 4))\n",
    "ax.plot(df_filtered[\"pred_50\"].values, label=\"Predicted Median\", color=\"blue\")\n",
    "ax.fill_between(df_filtered.index, df_filtered[\"pred_10\"], df_filtered[\"pred_90\"], alpha=0.3, label=\"80% Interval\")\n",
    "ax.plot(df_filtered[\"actual\"].values, label=\"Actual\", color=\"black\", linestyle=\"--\")\n",
    "ax.legend()\n",
    "st.pyplot(fig)\n",
    "\n",
    "# Accuracy metrics\n",
    "st.subheader(\"Forecast Accuracy\")\n",
    "st.metric(\"RMSE\", f\"{df_filtered['rmse'].mean():.2f}\")\n",
    "st.metric(\"MAE\", f\"{df_filtered['mae'].mean():.2f}\")\n",
    "st.metric(\"WAPE\", f\"{df_filtered['wape'].mean() * 100:.2f}%\")\n",
    "\n",
    "# Alert System\n",
    "st.subheader(\"Inventory Alert Signals\")\n",
    "alert_counts = df_filtered[[\"overstock_flag\", \"understock_flag\"]].sum()\n",
    "st.write(\"Overstock Alerts:\", int(alert_counts[\"overstock_flag\"]))\n",
    "st.write(\"Understock Alerts:\", int(alert_counts[\"understock_flag\"]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4b2c3dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run m5_streamlit_dashboard.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "m5",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
