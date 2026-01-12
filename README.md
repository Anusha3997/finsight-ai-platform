📈 FinSight-AI
An AI-Powered Financial Forecasting & Risk Analytics Platform
FinSight-AI is a full-stack financial analytics system that ingests real market data, stores it in a relational database, applies machine-learning–based forecasting and risk models, and exposes the results through a modern API and interactive web UI.
This project simulates how real fintech and trading analytics platforms are built from data ingestion to decision-support visualization.

🚀 What FinSight-AI Does
FinSight-AI allows a user to enter any stock ticker (e.g., AAPL, MSFT, NVDA) and automatically:
    Ingests historical market data from a public financial data source (Stooq)
    Stores the data in PostgreSQL
    Builds a predictive model based on historical returns
    Generates future price forecasts
    Computes financial risk metrics
    Displays results in an interactive dashboard
All of this happens through a clean API-driven architecture.

Core Features
📥 Automated Data Ingestion
    Market price data is fetched from Stooq
    Data is automatically inserted into PostgreSQL
    UI auto-triggers ingestion if data is missing
📊 Price Forecasting
    Computes historical log returns
    Trains a predictive model
    Generates forward price projections
⚠️ Risk Analytics
    For each stock, FinSight-AI calculates:
    Volatility – how unstable the stock is
    Maximum Drawdown – worst historical loss
    Sharpe Ratio – risk-adjusted return
🖥️ Interactive Dashboard
    Hoverable, zoomable Plotly charts
    Clear separation between historical and predicted prices
    Live API-driven data

| Layer            | Technology            |
| ---------------- | --------------------- |
| Backend API      | FastAPI               |
| Database         | PostgreSQL            |
| ORM              | SQLAlchemy            |
| Data Source      | Stooq API             |
| Machine Learning | Python, NumPy, Pandas |
| Visualization    | Plotly                |
| Frontend         | Streamlit             |
| Deployment       | Docker                |

📈 How It Works (End-to-End)
    User enters a ticker (e.g., AAPL)
    UI calls FastAPI
    Backend checks if data exists
    If missing → auto-ingest from Stooq
    Data is saved to PostgreSQL
    Forecast model is trained on historical returns
    Risk metrics are computed
    UI renders charts and analytics
All actions happen through clean REST APIs.