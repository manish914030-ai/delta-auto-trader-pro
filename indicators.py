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

    high_low = high - low
    high_close = (high - previous_close).abs()
    low_close = (low - previous_close).abs()

    true_range = pd.concat(
        [
            high_low,
            high_close,
            low_close
        ],
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

    # Deep copy — prevents chained-assignment problems
    data = df.copy(deep=True)

    # Clean numeric columns
    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    for column in numeric_columns:
        if column in data.columns:
            data.loc[:, column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    # Calculate indicators first
    ema20_value = ema(
        data["close"],
        20
    )

    ema50_value = ema(
        data["close"],
        50
    )

    rsi_value = rsi(
        data["close"],
        14
    )

    atr_value = atr(
        data,
        14
    )

    # Add columns using assign
    data = data.assign(
        EMA20=ema20_value,
        EMA50=ema50_value,
        RSI=rsi_value,
        ATR=atr_value
    )

    return data
