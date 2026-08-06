def add_indicators(df):
    df = df.copy()

    df["EMA20"] = ema(df["close"], 20)
    df["EMA50"] = ema(df["close"], 50)
    df["RSI"] = rsi(df["close"], 14)
    df["ATR"] = atr(df, 14)

    return df
