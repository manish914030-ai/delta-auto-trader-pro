from config import EMA_FAST, EMA_SLOW, RSI_BUY, RSI_SELL
from indicators import add_indicators


def check_signal(df):
    """
    Returns:
        BUY, SELL or WAIT
    """

    df = add_indicators(df)

    if len(df) < 60:
        return "WAIT"

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # BUY Conditions
    buy = (
        prev["EMA20"] <= prev["EMA50"] and
        last["EMA20"] > last["EMA50"] and
        last["RSI"] > RSI_BUY and
        last["close"] > last["EMA20"]
    )

    # SELL Conditions
    sell = (
        prev["EMA20"] >= prev["EMA50"] and
        last["EMA20"] < last["EMA50"] and
        last["RSI"] < RSI_SELL and
        last["close"] < last["EMA20"]
    )

    if buy:
        return "BUY"

    if sell:
        return "SELL"

    return "WAIT"
