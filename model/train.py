import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1️⃣ Download stock data
symbol = "AAPL"
data = yf.download(symbol, start="2018-01-01", end="2024-01-01")

# Use only Close prices
close_prices = data[['Close']]

# 2️⃣ Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(close_prices)

# 3️⃣ Create training dataset
X = []
y = []

for i in range(60, len(scaled)):
    X.append(scaled[i-60:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

# 4️⃣ Build LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(60, 1)))
model.add(LSTM(50))
model.add(Dense(1))

# 5️⃣ Compile and train
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=20, batch_size=32)

# 6️⃣ Save model
model.save("stock_model.h5")

print("✅ Model trained and saved as stock_model.h5")
