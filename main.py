from flask import Flask
import threading
import time
import os
import pandas as pd

from exchange import get_exchange
from strategy import check_signal
from telegram_bot import send_message

app = Flask(__name__)


@app.route("/")
def home():
    return "Delta Auto Trader Pro Running ✅"


def bot_loop():
    exchange = get_exchange()

    symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT"
    ]

    timeframe = "5m"

    while True:
        try:
            for symbol in symbols:
                try:
                    ohlcv = exchange.fetch_ohlcv(
                        symbol,
                        timeframe=timeframe,
                        limit=200
                    )

                    df = pd.DataFrame(
                        ohlcv,
                        columns=[
                            "timestamp",
                            "open",
                            "high",
                            "low",
                            "close",
                            "volume"
                        ]
                    )

                    signal = check_signal(df)

                    print(f"{symbol} -> {signal}")

                    if signal != "WAIT":
                        send_message(
                            f"📢 <b>{symbol}</b>\n"
                            f"Signal : <b>{signal}</b>"
                        )

                except Exception as e:
                    print(f"{symbol} Error: {e}")

            time.sleep(60)

        except Exception as e:
            print(f"Bot Error: {e}")
            time.sleep(60)


threading.Thread(target=bot_loop, daemon=True).start()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
