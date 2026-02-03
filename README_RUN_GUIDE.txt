STOCK MARKET PREDICTOR – QUICK RUN GUIDE

1) REQUIREMENTS
- Python 3.10 or 3.11 (recommended)
- Internet connection
- Windows / macOS / Linux

2) BACKEND SETUP
- Open terminal in backend folder
- Create virtual environment:
  python -m venv venv
- Activate:
  venv\Scripts\activate   (Windows)
  source venv/bin/activate (Mac/Linux)
- Install dependencies:
  pip install fastapi uvicorn yfinance pandas numpy scikit-learn tensorflow
- Start backend server:
  uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

3) FRONTEND SETUP
- Open NEW terminal in frontend folder
- Create virtual environment:
  python -m venv venv
- Activate:
  venv\Scripts\activate   (Windows)
  source venv/bin/activate (Mac/Linux)
- Install dependencies:
  pip install streamlit yfinance plotly pandas requests
- Run frontend:
  streamlit run app.py

Frontend runs at:
http://localhost:8501

4) USING THE APP
- Enter stock symbol (examples):
  AAPL, TSLA, MSFT, INFY.NS, RELIANCE.NS
- View:
  - Current price
  - AI prediction
  - Interactive price chart
  - Recent data table

5) IMPORTANT NOTES
- Backend MUST be running before frontend
- If uvicorn/streamlit not found, reinstall in active venv
- This project is for educational use only

END
