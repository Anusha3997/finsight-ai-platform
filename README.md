# FinSight-AI Platform

FinSight-AI is an AI-powered financial analytics platform that uses historical stock market data to generate forecasts, calculate risk metrics, and visualize insights through an interactive dashboard.

This project demonstrates how real-world fintech systems combine data engineering, machine learning, and backend services into a single production-style application.

---

## What This Project Does

FinSight-AI allows users to:

- Load historical stock market data  
- Predict future prices using machine learning  
- Calculate financial risk metrics  
- Visualize trends and forecasts in a dashboard  

This simulates how financial analytics platforms are built in investment, trading, and fintech companies.

---

## Application Preview

![Dashboard](screenshots/Architecture.png)
![Dashboard](screenshots/Dashboard.png)  
![Forecast](screenshots/Forecast.png)  
![Risk Metrics](screenshots/Risk.png)

---

## Key Features

- Historical stock data ingestion  
- Machine learning-based forecasting  
- Risk metrics (volatility, drawdown, performance)  
- Backend data processing  
- Interactive visualization dashboard  

---

## Technology Stack

| Layer | Tools |
|------|-------|
| Programming | Python |
| Machine Learning | scikit-learn, pandas |
| Backend | Python API |
| Frontend | Streamlit |
| Data | CSV / PostgreSQL |
| Visualization | Plotly, charts |


---

## Future Improvements
Live market data integration
Online deployment
Portfolio analysis features
Advanced forecasting models

---


## Run Locally

```bash
git clone https://github.com/Anusha3997/finsight-ai-platform
cd finsight-ai-platform
pip install -r requirements.txt
python app/main.py
streamlit run ui/app.py



