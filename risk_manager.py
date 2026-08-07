from config import (
    RISK_PER_TRADE,
    MAX_DAILY_LOSS,
    LEVERAGE
)


class RiskManager:

    def __init__(self):
        self.daily_loss = 0

    def can_trade(self):

        if self.daily_loss >= MAX_DAILY_LOSS:
            return False

        return True

    def calculate_position_size(
        self,
        balance,
        entry_price,
        stop_loss_price
    ):

        risk_amount = balance * (RISK_PER_TRADE / 100)

        stop_distance = abs(entry_price - stop_loss_price)

        if stop_distance <= 0:
            return 0

        qty = risk_amount / stop_distance

        qty = qty * LEVERAGE

        return round(qty, 4)

    def update_daily_loss(self, loss):

        self.daily_loss += loss

    def reset_daily_loss(self):

        self.daily_loss = 0


risk_manager = RiskManager()
