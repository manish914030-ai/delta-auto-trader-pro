from config import (
    EMA_FAST,
    EMA_SLOW,
    RSI_BUY,
    RSI_SELL
)

from indicators import add_indicators


def check_signal(df):

    df = add_indicators(df)

    if len(df) < 60:
        return "WAIT"

    last = df.iloc[-1]
    prev = df.iloc[-2]

    volume_ok = last["volume"] > df["volume"].rolling(20).mean().iloc[-1]

    buy = (
        prev["EMA20"] <= prev["EMA50"]
        and last["EMA20"] > last["EMA50"]
        and last["RSI"] > RSI_BUY
        and last["close"] > last["EMA20"]
        and volume_ok
    )

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
