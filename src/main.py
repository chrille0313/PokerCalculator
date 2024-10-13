from src.util import PokerPlayer
from src.payment_strategies import PokerPaymentStrategy


class PokerConfig:
    CHIPS_PER_MONEY = 10


def main():
    players = [
        PokerPlayer("Axel", 200 * PokerConfig.CHIPS_PER_MONEY, 2690),
        PokerPlayer("Christian", 100 * PokerConfig.CHIPS_PER_MONEY, 1001),
        PokerPlayer("David", 200 * PokerConfig.CHIPS_PER_MONEY, 360),
        PokerPlayer("Robert", 100 * PokerConfig.CHIPS_PER_MONEY, 2040),
        PokerPlayer("Sebastian", 100 * PokerConfig.CHIPS_PER_MONEY, 4870),
        PokerPlayer("Edward", 300 * PokerConfig.CHIPS_PER_MONEY, 0)
    ]

    payment_strategy = PokerPaymentStrategy()

    for payment in payment_strategy.calculate_payments(players):
        print(payment)


if __name__ == '__main__':
    main()
