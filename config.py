import os

# ==========================
# Delta Exchange API
# ==========================
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Live / Testnet
TESTNET = False

# ==========================
# Telegram
# ==========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ==========================
# Trading Settings
# ==========================
SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT"
]

TREND_TIMEFRAME = "1h"
ENTRY_TIMEFRAME = "15m"

LEVERAGE = 10
RISK_PER_TRADE = 1.0
MAX_DAILY_LOSS = 3.0

# ATR Settings
ATR_PERIOD = 14
ATR_SL_MULTIPLIER = 2.0
ATR_TRAIL_MULTIPLIER = 1.5

# EMA
EMA_FAST = 20
EMA_SLOW = 50

# RSI
RSI_PERIOD = 14
RSI_BUY = 55
RSI_SELL = 45
