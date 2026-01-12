# FinSight-AI Platform

## 📈 Overview

**FinSight-AI** is an **AI-powered financial analytics platform** that simulates real-world fintech systems.  
It demonstrates a complete **data engineering → machine learning → backend → frontend** pipeline by:

✔ Ingesting and storing historical market data  
✔ Forecasting stock prices with an ML model  
✔ Computing key risk metrics  
✔ Presenting interactive visual analytics

This project showcases full-stack capabilities with **Python, ML models, REST API design, database integration, and UI dashboards**—skills highly relevant for data-focused and engineering roles.

---

## 🔍 Key Features

### 📊 Data Engineering
- Automatically fetches historical market data  
- Persists data efficiently in a **PostgreSQL** database  

### 🤖 Forecasting & Analytics
- Uses a **machine learning model** to forecast future price movements  
- Computes financial risk metrics such as:
  - **Volatility**
  - **Maximum Drawdown**
  - **Sharpe Ratio**

### 📟 Frontend Dashboard
- Interactive dashboard for visual analysis
- Fast insights into stock trends and risk profiles

---

## 🛠 Tech Stack

| Layer | Tools / Frameworks |
|-------|---------------------|
| Backend | Python, Flask / FastAPI (if used) |
| Database | PostgreSQL |
| Data Ingestion | Stooq API (or similar) |
| Machine Learning | Scikit-Learn / Custom modeling |
| Frontend | Streamlit / UI framework (based on project files) |
| DevOps | Docker |

📌 *100% Python-based codebase for maximum portability and scalability.* :contentReference[oaicite:0]{index=0}

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anusha3997/finsight-ai-platform.git
cd finsight-ai-platform

## 🚀 Run Locally

This project can be run locally for development or testing.

```bash
git clone https://github.com/Anusha3997/finsight-ai-platform
cd finsight-ai-platform
pip install -r requirements.txt
python app/main.py

The frontend dashboard can be launched with:
streamlit run ui/app.py
