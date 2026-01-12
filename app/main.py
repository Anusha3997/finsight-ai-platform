from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import setup_logging
from app.db.session import get_db, engine
from app.db.base import Base
from app.db.models import Price
from app.schemas.prices import PriceOut
from app.services.ingest_service import ingest_ticker_prices

from app.schemas.risk import RiskOut
from app.services.risk_service import compute_risk_metrics

from app.schemas.forecast import ForecastOut
from app.services.forecast_service import forecast_prices

setup_logging()

app = FastAPI(title=settings.APP_NAME)

# TEMP for Week 1: create tables on startup (we'll switch to Alembic later)
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.APP_NAME}


@app.post("/ingest/{ticker}")
def ingest(
    ticker: str,
    start: str | None = Query(default=None, description="YYYY-MM-DD"),
    end: str | None = Query(default=None, description="YYYY-MM-DD"),
    db: Session = Depends(get_db),
):
    try:
        attempted = ingest_ticker_prices(db, ticker=ticker, start=start, end=end)
        return {"ticker": ticker.upper(), "attempted_rows": attempted}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ingest failed: {e}")


@app.get("/prices/{ticker}", response_model=list[PriceOut])
def get_prices(
    ticker: str,
    limit: int = Query(default=200, ge=1, le=5000),
    db: Session = Depends(get_db),
):
    rows = (
        db.query(Price)
        .filter(Price.ticker == ticker.upper())
        .order_by(Price.date.desc())
        .limit(limit)
        .all()
    )
    return rows

@app.get("/risk/{ticker}", response_model=RiskOut)
def get_risk_metrics(
    ticker: str,
    db: Session = Depends(get_db),
):
    try:
        return compute_risk_metrics(db, ticker)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/forecast/{ticker}")
def get_forecast(
    ticker: str,
    days: int = 7,
    db: Session = Depends(get_db),
):

    try:
        return forecast_prices(db, ticker, days)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
