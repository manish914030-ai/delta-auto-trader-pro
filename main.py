import time
import pandas as pd

from config import SYMBOLS, ENTRY_TIMEFRAME
from exchange import get_exchange
from strategy import check_signal
from trade_manager import TradeManager
from telegram_bot import send_message
from risk_manager import RiskManager

exchange = get_exchange()
trade_manager = TradeManager()
risk_manager = RiskManager()


def get_candles(symbol, timeframe, limit=200):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

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

    return df


def run():

    send_message("🤖 Delta Auto Trader Started")

    while True:

        try:

            balance = exchange.fetch_balance()

            usdt_balance = balance["USDT"]["free"]

            if not risk_manager.can_trade(usdt_balance):
                send_message("❌ Daily Loss Limit Reached")
                break

            for symbol in SYMBOLS:

                try:

                    df = get_candles(symbol, ENTRY_TIMEFRAME)

                    signal = check_signal(df)

                    print(symbol, signal)

                    if signal == "WAIT":
                        continue

                    price = df.iloc[-1]["close"]
                    atr = df.iloc[-1]["ATR"]

                    stop_distance = atr * 2

                    qty = risk_manager.calculate_position_size(
                        usdt_balance,
                        price,
                        price - stop_distance if signal == "BUY" else price + stop_distance
                    )

                    if qty <= 0:
                        continue

                    if signal == "BUY":

                        trade_manager.buy(symbol, qty)

                    elif signal == "SELL":

                        trade_manager.sell(symbol, qty)

                    send_message(
                        f"""
<b>{signal} EXECUTED</b>

Symbol : {symbol}
Price : {price}
Qty : {qty}
"""
                    )

                except Exception as e:

                    print(symbol, e)

            time.sleep(60)

        except Exception as e:

            print(e)

            send_message(f"Bot Error\n{e}")

            time.sleep(60)


if __name__ == "__main__":
    run()
