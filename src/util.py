class PokerPlayer:
    def __init__(self, name: str, buy_in_chips: int, total_chips: int):
        self.name = name
        self.buy_in_chips = buy_in_chips
        self.total_chips = total_chips

    def add_buy_in(self, buy_in):
        self.buy_in_chips += buy_in

    def add_chips(self, chips):
        self.total_chips += chips

    def calculate_profit(self):
        return self.total_chips - self.buy_in_chips

    def __str__(self):
        return f"{self.name}, buy in: {self.buy_in_chips}, total chips: {self.total_chips}, net: {self.calculate_profit()}"


class Payment:
    def __init__(self, from_player: PokerPlayer, to_player: PokerPlayer, amount: float):
        self.from_player = from_player
        self.to_player = to_player
        self.amount = amount

    def __str__(self):
        return f"{self.from_player.name} pays {self.to_player.name} {self.amount}"

    def __repr__(self):
        return self.__str__()