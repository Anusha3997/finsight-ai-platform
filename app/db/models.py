from sqlalchemy import String, Date, Float, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    date: Mapped["Date"] = mapped_column(Date, index=True)

    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        UniqueConstraint("ticker", "date", name="uq_prices_ticker_date"),
        Index("ix_prices_ticker_date", "ticker", "date"),
    )
