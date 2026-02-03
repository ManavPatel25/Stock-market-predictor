from fastapi import FastAPI
import yfinance as yf
import numpy as np

app = FastAPI()

@app.get("/predict/{symbol}")
def predict_stock(symbol: str):
    df = yf.download(symbol, period="6mo", interval="1d")

    if df.empty:
        return {"prediction": "No data"}

    close = df["Close"].values

    # Simple trend-based prediction
    recent_mean = np.mean(close[-5:])
    previous_mean = np.mean(close[-10:-5])

    if recent_mean > previous_mean:
        prediction = "📈 Uptrend Expected"
    elif recent_mean < previous_mean:
        prediction = "📉 Downtrend Expected"
    else:
        prediction = "➡️ Sideways Movement"

    return {
        "symbol": symbol,
        "prediction": prediction,
        "latest_price": float(close[-1])
    }
