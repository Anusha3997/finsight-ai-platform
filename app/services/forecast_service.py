import numpy as np
from sqlalchemy.orm import Session
from sklearn.linear_model import LinearRegression

from app.db.models import Price
from app.schemas import prices
from datetime import timedelta

def forecast_prices(db: Session, ticker: str, days: int = 7, window: int = 5):
    # 1️⃣ Fetch historical prices
    prices = (
        db.query(Price)
        .filter(Price.ticker == ticker.upper())
        .order_by(Price.date.asc())
        .all()
    )

    if len(prices) < window + 1:
        raise ValueError("Not enough data to generate forecast")

    close_prices = np.array([p.close for p in prices])

    # 2️⃣ Convert prices to returns
    returns = np.diff(close_prices) / close_prices[:-1]

    # 3️⃣ Create lagged features
    X = []
    y = []

    for i in range(window, len(returns)):
        X.append(returns[i - window : i])
        y.append(returns[i])

    X = np.array(X)
    y = np.array(y)

    # 4️⃣ Train simple regression model
    model = LinearRegression()
    model.fit(X, y)

    # 5️⃣ Forecast future returns
    last_window = returns[-window:].tolist()
    forecasted_returns = []

    for _ in range(days):
        next_return = model.predict([last_window])[0]
        forecasted_returns.append(float(next_return))
        last_window.pop(0)
        last_window.append(next_return)

    # 6️⃣ Convert returns back to prices
    last_price = close_prices[-1]
    forecasted_prices = []

    for r in forecasted_returns:
        last_price = last_price * (1 + r)
        forecasted_prices.append(float(last_price))
    

    results = []
    last_date = prices[-1].date
    start_date = last_date  # last_date must come from DB (latest price date)

    for i, price in enumerate(forecasted_prices, start=1):
        results.append({
            "date": (start_date + timedelta(days=i)).isoformat(),
            "predicted": round(price, 2)
        })
    return {
        "ticker": ticker.upper(),
        "days": days,
        "forecast": results
    }