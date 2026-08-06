import os

# ==========================================
# DELTA EXCHANGE SETTINGS
# ==========================================

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# True = Testnet
# False = Live Trading
TESTNET = True

# ==========================================
# TELEGRAM SETTINGS
# ==========================================

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ==========================================
# TRADING SYMBOLS
# ==========================================

SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT"
]

# ==========================================
# TIMEFRAMES
# ==========================================

TREND_TIMEFRAME = "1h"
ENTRY_TIMEFRAME = "15m"

# ==========================================
# RISK MANAGEMENT
# ==========================================

LEVERAGE = 10

RISK_PER_TRADE = 1.0      # %
MAX_DAILY_LOSS = 3.0      # %

MAX_OPEN_TRADES = 1

# ==========================================
# TAKE PROFIT / STOP LOSS
# ==========================================

ATR_PERIOD = 14

ATR_SL_MULTIPLIER = 2.0
ATR_TP_MULTIPLIER = 3.0
ATR_TRAIL_MULTIPLIER = 1.5

# ==========================================
# EMA SETTINGS
# ==========================================

EMA_FAST = 20
EMA_SLOW = 50

# ==========================================
# RSI SETTINGS
# ==========================================

RSI_PERIOD = 14

RSI_BUY = 55
RSI_SELL = 45

# ==========================================
# BOT SETTINGS
# ==========================================

CANDLE_LIMIT = 300

CHECK_INTERVAL = 60

LOG_LEVEL = "INFO"
