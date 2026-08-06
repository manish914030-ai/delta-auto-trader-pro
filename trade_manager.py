from exchange import get_exchange


class TradeManager:

    def __init__(self):
        self.exchange = get_exchange()

    def buy(self, symbol, quantity):
        try:
            order = self.exchange.create_market_buy_order(
                symbol,
                quantity
            )
            print(f"BUY Order Executed: {order}")
            return order

        except Exception as e:
            print(f"BUY Error: {e}")
            return None

    def sell(self, symbol, quantity):
        try:
            order = self.exchange.create_market_sell_order(
                symbol,
                quantity
            )
            print(f"SELL Order Executed: {order}")
            return order

        except Exception as e:
            print(f"SELL Error: {e}")
            return None
