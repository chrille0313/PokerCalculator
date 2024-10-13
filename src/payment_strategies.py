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


class GreedyPokerPaymentStrategy(PokerPaymentStrategy):
    @staticmethod
    def is_payer(player: PokerPlayer) -> bool:
        return player.calculate_profit() < 0

    @staticmethod
    def is_receiver(player: PokerPlayer) -> bool:
        return player.calculate_profit() > 0

    def calculate_payments(self, players: list[PokerPlayer]) -> list[Payment]:
        payers = sorted((player for player in players if self.is_payer(player)), key=lambda player: player.calculate_profit())
        receivers = sorted((player for player in players if self.is_receiver(player)), key=lambda player: player.calculate_profit(), reverse=True)
        total_remaining_debt = sum(abs(player.calculate_profit()) for player in payers)

        payments = []

        current_receiver = receivers.pop(0)
        current_receiver_debt = current_receiver.calculate_profit()

        for payer in payers:
            remaining_payer_debt = abs(payer.calculate_profit())

            while remaining_payer_debt > 0:
                pay_amount = min(remaining_payer_debt, current_receiver_debt)
                payments.append(Payment(payer, current_receiver, pay_amount))

                remaining_payer_debt -= pay_amount
                current_receiver_debt -= pay_amount
                total_remaining_debt -= pay_amount

                if current_receiver_debt == 0 and total_remaining_debt > 0:
                    if len(receivers) == 0:
                        raise ValueError(f"Not enough receivers to pay off all debts")

                    current_receiver = receivers.pop(0)
                    current_receiver_debt = current_receiver.calculate_profit()

        if len(receivers) > 0:
            raise ValueError(f"Not all debts could be paid off (too many receivers)")

        return payments
