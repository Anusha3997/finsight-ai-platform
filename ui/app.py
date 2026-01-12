import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# Config
# -----------------------------
API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="FinSight AI",
    layout="wide"
)

# -----------------------------
# Global CSS (Times New Roman)
# -----------------------------
st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-family: 'Times New Roman', serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Helpers
# -----------------------------
def auto_ingest_if_needed(ticker: str):
    """
    Idempotent ingest.
    Safe to call multiple times.
    """
    r = requests.post(f"{API_BASE_URL}/ingest/{ticker}")
    if r.status_code not in (200, 201):
        raise Exception("Auto-ingest failed")

def fetch_prices(ticker: str):
    r = requests.get(f"{API_BASE_URL}/prices/{ticker}")
    r.raise_for_status()
    return r.json()

def fetch_forecast(ticker: str):
    r = requests.get(f"{API_BASE_URL}/forecast/{ticker}")
    r.raise_for_status()
    return r.json()

def fetch_risk(ticker: str):
    r = requests.get(f"{API_BASE_URL}/risk/{ticker}")
    r.raise_for_status()
    return r.json()

# -----------------------------
# Header
# -----------------------------
st.markdown("## 📈 **FinSight AI**")
st.markdown("### Stock Forecasting & Risk Analytics Platform")
st.divider()

# -----------------------------
# Input
# -----------------------------
ticker = st.text_input("Enter Stock Ticker", value="AAPL").upper().strip()

col_btn1, col_btn2 = st.columns([1, 1])
forecast_btn = col_btn1.button("📊 Generate Forecast")
risk_btn = col_btn2.button("⚠️ Compute Risk")

st.divider()

# -----------------------------
# Forecast Section
# -----------------------------
if forecast_btn:
    try:
        auto_ingest_if_needed(ticker)

        prices = fetch_prices(ticker)
        forecast = fetch_forecast(ticker)

        hist_df = pd.DataFrame(prices)
        hist_df["date"] = pd.to_datetime(hist_df["date"])

        pred_df = pd.DataFrame(forecast["forecast"])
        pred_df["date"] = pd.to_datetime(pred_df["date"])

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=hist_df["date"],
            y=hist_df["close"],
            mode="lines",
            name="Historical",
            line=dict(color="#1f77b4", width=2)
        ))

        fig.add_trace(go.Scatter(
            x=pred_df["date"],
            y=pred_df["predicted"],
            mode="lines+markers",
            name="Forecast",
            line=dict(color="#d62728", width=2, dash="dash")
        ))

        fig.update_layout(
            title=f"Price Forecast — {ticker}",
            xaxis_title="Date",
            yaxis_title="Price",
            hovermode="x unified",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)
        st.success("Forecast generated successfully")

    except Exception as e:
        st.error(f"Forecast error: {e}")

# -----------------------------
# Risk Section (Side-by-Side)
# -----------------------------
if risk_btn:
    try:
        auto_ingest_if_needed(ticker)
        risk = fetch_risk(ticker)

        st.markdown("## ⚠️ Risk Metrics")

        c1, c2, c3 = st.columns(3)
        c1.metric("Volatility", f"{risk['volatility']:.4f}")
        c2.metric("Max Drawdown", f"{risk['max_drawdown']:.4f}")
        c3.metric("Sharpe Ratio", f"{risk['sharpe_ratio']:.4f}")

        st.success("Risk metrics computed successfully")

    except Exception as e:
        st.error(f"Risk error: {e}")
