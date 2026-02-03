import streamlit as st
import requests
import pandas as pd
import yfinance as yf
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Stock Dashboard", layout="wide")

st.title("📈 AI Stock Market Prediction System")
st.caption("Examples: AAPL, TSLA, MSFT, RELIANCE.NS, INFY.NS")

# ---------------- USER INPUT ----------------
symbol = st.text_input("🔍 Enter Stock Symbol", "AAPL").upper()

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data(symbol):
    df = yf.download(symbol, period="1y", interval="1d", auto_adjust=True)

    # 🔑 FIX: Flatten MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    df = df.reset_index()
    return df

df = load_data(symbol)

if df.empty:
    st.error("❌ No data found. Check the stock symbol.")
    st.stop()

# ---------------- CURRENT PRICE ----------------
current_price = float(df["Close"].iloc[-1])

# ---------------- BACKEND PREDICTION ----------------
prediction = "N/A"
try:
    res = requests.get(f"http://127.0.0.1:8000/predict/{symbol}", timeout=5)
    if res.status_code == 200:
        prediction = res.json().get("prediction", "N/A")
except:
    prediction = "Backend not running"

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("💰 Current Price", f"${current_price:.2f}")
c2.metric("📊 Records", len(df))
c3.metric("🤖 AI Prediction", prediction)

# ---------------- GRAPH (FIXED) ----------------
st.subheader("📊 Price Trend (1 Year)")

fig = px.line(
    df,
    x="Date",
    y="Close",
    title=f"{symbol} Closing Price (1Y)"
)

fig.update_layout(
    height=500,
    xaxis_title="Date",
    yaxis_title="Price",
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- DATA TABLE ----------------
st.subheader("📋 Recent Stock Data")
st.dataframe(df.tail(20), use_container_width=True)

st.caption("⚠️ Educational project only. Not financial advice.")
