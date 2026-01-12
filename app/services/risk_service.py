import numpy as np
from sqlalchemy.orm import Session

from app.db.models import Price


def compute_risk_metrics(db: Session, ticker: str):
    # 1️⃣ Fetch price data
    prices = (
        db.query(Price)
        .filter(Price.ticker == ticker.upper())
        .order_by(Price.date.asc())
        .all()
    )

    if len(prices) < 2:
        raise ValueError("Not enough data to compute risk metrics")

    # 2️⃣ Extract close prices
    close_prices = np.array([p.close for p in prices])

    # 3️⃣ Compute daily returns
    returns = np.diff(close_prices) / close_prices[:-1]

    # 4️⃣ Volatility (annualized)
    volatility = np.std(returns) * np.sqrt(252)

    # 5️⃣ Maximum drawdown
    cumulative = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(cumulative)
    drawdowns = (cumulative - peak) / peak
    max_drawdown = drawdowns.min()

    # 6️⃣ Sharpe ratio (risk-free rate assumed 0)
    sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(252)

    return {
        "ticker": ticker.upper(),
        "volatility": float(volatility),
        "max_drawdown": float(max_drawdown),
        "sharpe_ratio": float(sharpe_ratio),
    }
