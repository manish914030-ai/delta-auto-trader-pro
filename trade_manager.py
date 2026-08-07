from risk_manager import risk_manager


class TradeManager:

    def __init__(self):
        self.active_trade = None

    def has_open_trade(self):
        return self.active_trade is not None

    def open_trade(
        self,
        symbol,
        side,
        balance,
        entry_price,
        stop_loss,
    ):

        if self.has_open_trade():
            return None

        qty = risk_manager.calculate_position_size(
            balance,
            entry_price,
            stop_loss,
        )

        if qty <= 0:
            return None

        self.active_trade = {
            "symbol": symbol,
            "side": side,
            "entry": entry_price,
            "stop_loss": stop_loss,
            "qty": qty,
        }

        return self.active_trade

    def close_trade(self):

        self.active_trade = None

    def get_trade(self):

        return self.active_trade


trade_manager = TradeManager()
