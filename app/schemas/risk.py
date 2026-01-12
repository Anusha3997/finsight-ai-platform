from pydantic import BaseModel


class RiskOut(BaseModel):
    ticker: str
    volatility: float
    max_drawdown: float
    sharpe_ratio: float
