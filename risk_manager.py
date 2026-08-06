from config import RISK_PER_TRADE, MAX_DAILY_LOSS


class RiskManager:
    def __init__(self):
        self.daily_loss = 0.0

    def calculate_position_size(self, balance, entry_price, stop_loss_price):
        risk_amount = balance * RISK_PER_TRADE

        stop_distance = abs(entry_price - stop_loss_price)

        if stop_distance <= 0:
            return 0

        quantity = risk_amount / stop_distance
        return round(quantity, 6)

    def can_trade(self, balance):
        max_loss = balance * MAX_DAILY_LOSS

        if self.daily_loss >= max_loss:
            return False

        return True

    def add_loss(self, loss_amount):
        self.daily_loss += abs(loss_amount)

    def reset_daily_loss(self):
        self.daily_loss = 0.0
