from abc import ABC, abstractmethod
from src.util import PokerPlayer, Payment


class PokerPaymentStrategy(ABC):
    @staticmethod
    def check_chips(players: list[PokerPlayer]) -> None:
        expected_chips = sum(player.buy_in_chips for player in players)
        total_chips = sum(player.total_chips for player in players)

        if total_chips != expected_chips:
            diff = total_chips - expected_chips

            raise ValueError(f"Chips count is incorrect! You have counted {total_chips} chips, but there should be {expected_chips}. You have "
                             f"counted {abs(diff)} too {'few' if diff < 0 else 'many'}")

    @abstractmethod
    def calculate_payments(self, players) -> list[Payment]:
        ...

    def get_payments(self, players: list[PokerPlayer]) -> list[Payment]:
        self.check_chips(players)
        return self.calculate_payments(players)
