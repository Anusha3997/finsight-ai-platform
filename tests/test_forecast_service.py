from sqlalchemy.orm import Session
from app.services.forecast_service import forecast_prices
from app.db.models import Price
from datetime import date

def test_forecast_prices_basic(db_session: Session):
    prices = [
        Price(ticker="TEST",date=date(2024, 1, 1),open=100.0,high=105.0,low=95.0,close=102.0,volume=1_000_000),
        Price(ticker="TEST",date=date(2024, 1, 2),open=102.0,high=106.0,low=101.0,close=104.0,volume=1_100_000),
        Price(ticker="TEST",date=date(2024, 1, 3),open=104.0,high=108.0,low=103.0,close=107.0,volume=1_200_000),
        Price(ticker="TEST",date=date(2024, 1, 4),open=107.0,high=110.0,low=106.0,close=109.0,volume=1_300_000),
        Price(ticker="TEST",date=date(2024, 1, 5),open=109.0,high=112.0,low=108.0,close=111.0,volume=1_400_000),
        Price(ticker="TEST",date=date(2024, 1, 6),open=111.0,high=115.0,low=110.0,close=114.0,volume=1_500_000),
        Price(ticker="TEST",date=date(2024, 1, 7),open=114.0,high=118.0,low=113.0,close=117.0,volume=1_600_000),
    ]


    for p in prices:
        db_session.add(p)
    db_session.commit()

    result = forecast_prices(db_session, "TEST", days=3, window=3)

    assert result["ticker"] == "TEST"
    assert len(result["forecast"]) == 3
