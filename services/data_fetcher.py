import yfinance as yf

def fetch_stock_data(symbol, period="6mo"):
    data = yf.download(symbol, period=period)

    if data is None or len(data) < 60:
        raise ValueError("Not enough data for prediction")

    return data[['Close']]
