from config import (
    EMA_FAST,
    EMA_SLOW,
    RSI_BUY,
    RSI_SELL
)

from indicators import add_indicators


def check_signal(df):

    # Add indicators safely
    df = add_indicators(df)

    # Not enough candles
    if len(df) < 60:
        return "WAIT"

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # Required values must exist
    required = [
        "EMA20",
        "EMA50",
        "RSI",
        "ATR",
        "close",
        "volume"
    ]

    for column in required:
        if column not in df.columns:
            return "WAIT"

    # Avoid incomplete indicator values
    if (
        pd_is_na(last["EMA20"])
        or pd_is_na(last["EMA50"])
        or pd_is_na(last["RSI"])
        or pd_is_na(last["ATR"])
    ):
        return "WAIT"

    # Volume confirmation
    volume_average = df["volume"].rolling(
        window=20,
        min_periods=20
    ).mean().iloc[-1]

    if pd_is_na(volume_average):
        return "WAIT"

    volume_ok = last["volume"] > volume_average

    # BUY condition
    buy = (
        prev["EMA20"] <= prev["EMA50"]
        and last["EMA20"] > last["EMA50"]
        and last["RSI"] > RSI_BUY
        and last["close"] > last["EMA20"]
        and volume_ok
    )

    # SELL condition
    sell = (
        prev["EMA20"] >= prev["EMA50"]
        and last["EMA20"] < last["EMA50"]
        and last["RSI"] < RSI_SELL
        and last["close"] < last["EMA20"]
        and volume_ok
    )

    if buy:
        return "BUY"

    if sell:
        return "SELL"

    return "WAIT"


def pd_is_na(value):
    try:
        return value != value
    except Exception:
        return True
