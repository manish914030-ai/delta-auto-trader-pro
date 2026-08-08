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

    rsi_value = 100 - (
        100 / (1 + rs)
    )

    return rsi_value


# ==========================================
# ATR
# ==========================================

def atr(df, period=14):

    data = df.copy()

    high = pd.to_numeric(
        data["high"],
        errors="coerce"
    )

    low = pd.to_numeric(
        data["low"],
        errors="coerce"
    )

    close = pd.to_numeric(
        data["close"],
        errors="coerce"
    )

    previous_close = close.shift(1)

    high_low = high - low

    high_close = (
        high - previous_close
    ).abs()

    low_close = (
        low - previous_close
    ).abs()

    true_range = pd.concat(
        [
            high_low,
            high_close,
            low_close
        ],
        axis=1
    ).max(axis=1)

    atr_value = true_range.rolling(
        window=period,
        min_periods=period
    ).mean()

    return atr_value


# ==========================================
# ADD ALL INDICATORS
# ==========================================

def add_indicators(df):

    data = df.copy()

    # Make sure price columns are numeric
    for column in [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]:
        if column in data.columns:
            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    # EMA
    data["EMA20"] = ema(
        data["close"],
        20
    )

    data["EMA50"] = ema(
        data["close"],
        50
    )

    # RSI
    data["RSI"] = rsi(
        data["close"],
        14
    )

    # ATR
    data["ATR"] = atr(
        data,
        14
    )

    return data
