import pandas as pd


# ==========================================
# EMA
# ==========================================

def ema(series, period):
    series = pd.to_numeric(series, errors="coerce")

    return series.ewm(
        span=period,
        adjust=False,
        min_periods=period
    ).mean()


# ==========================================
# RSI
# ==========================================

def rsi(series, period=14):
    series = pd.to_numeric(series, errors="coerce")

    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(
        window=period,
        min_periods=period
    ).mean()

    avg_loss = loss.rolling(
        window=period,
        min_periods=period
    ).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


# ==========================================
# ATR
# ==========================================

def atr(df, period=14):

    high = pd.to_numeric(
        df["high"],
        errors="coerce"
    )

    low = pd.to_numeric(
        df["low"],
        errors="coerce"
    )

    close = pd.to_numeric(
        df["close"],
        errors="coerce"
    )

    previous_close = close.shift(1)

    tr1 = high - low
    tr2 = (high - previous_close).abs()
    tr3 = (low - previous_close).abs()

    true_range = pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)

    return true_range.rolling(
        window=period,
        min_periods=period
    ).mean()


# ==========================================
# ADD ALL INDICATORS
# ==========================================

def add_indicators(df):

    # Always create a completely independent DataFrame
    data = df.copy(deep=True)

    # Make OHLCV numeric
    for column in [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]:
        if column in data.columns:
            data.loc[:, column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    # EMA
    ema20_value = ema(
        data["close"],
        20
    )

    ema50_value = ema(
        data["close"],
        50
    )

    # RSI
    rsi_value = rsi(
        data["close"],
        14
    )

    # ATR
    atr_value = atr(
        data,
        14
    )

    # Use .loc to avoid chained-assignment warnings
    data.loc[:, "EMA20"] = ema20_value
    data.loc[:, "EMA50"] = ema50_value
    data.loc[:, "RSI"] = rsi_value
    data.loc[:, "ATR"] = atr_value

    return data
