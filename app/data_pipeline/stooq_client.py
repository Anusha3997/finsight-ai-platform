from __future__ import annotations

import io
import requests
import pandas as pd


def fetch_stooq_daily_prices(ticker: str) -> pd.DataFrame:
    """
    Stooq provides free daily price CSV.
    Example endpoint: https://stooq.com/q/d/l/?s=aapl.us&i=d
    """
    t = ticker.strip().lower()

    # US stocks often use ".us" on stooq
    if "." not in t:
        t = f"{t}.us"

    url = f"https://stooq.com/q/d/l/?s={t}&i=d"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    df = pd.read_csv(io.StringIO(resp.text))
    if df.empty:
        raise ValueError(f"No data returned for ticker={ticker}")

    # Normalize columns
    df.columns = [c.strip().lower() for c in df.columns]
    # expected: date, open, high, low, close, volume
    return df
