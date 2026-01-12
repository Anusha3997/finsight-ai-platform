from __future__ import annotations

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.db.models import Price
from app.data_pipeline.stooq_client import fetch_stooq_daily_prices


def ingest_ticker_prices(db: Session, ticker: str, start: str | None = None, end: str | None = None) -> int:
    df = fetch_stooq_daily_prices(ticker)

    # Optional date filtering
    if start:
        start_dt = datetime.fromisoformat(start).date()
        df = df[df["date"] >= str(start_dt)]
    if end:
        end_dt = datetime.fromisoformat(end).date()
        df = df[df["date"] <= str(end_dt)]

    # Convert date strings -> date
    df["date"] = df["date"].apply(lambda x: datetime.fromisoformat(str(x)).date())

    rows = []
    for r in df.to_dict(orient="records"):
        rows.append(
            dict(
                ticker=ticker.upper(),
                date=r["date"],
                open=float(r["open"]),
                high=float(r["high"]),
                low=float(r["low"]),
                close=float(r["close"]),
                volume=float(r.get("volume", 0.0) or 0.0),
            )
        )

    if not rows:
        return 0

    stmt = insert(Price).values(rows)
    # Upsert behavior: ignore duplicates based on unique constraint
    stmt = stmt.on_conflict_do_nothing(index_elements=["ticker", "date"])
    result = db.execute(stmt)
    db.commit()

    # rowcount is not always reliable for DO NOTHING in some cases;
    # we'll return len(rows) as "attempted", later we can compute inserted count.
    return len(rows)
