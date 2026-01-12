from pydantic import BaseModel
from datetime import date
from typing import List

class ForecastPoint(BaseModel):
    date: date
    predicted: float


class ForecastOut(BaseModel):
    ticker: str
    days: int
    forecast: List[ForecastPoint]

    class Config:
        from_attributes = True
