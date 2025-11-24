"""A module representing a bank in a simple banking system."""
from enum import Enum

from credit_card import CreditCard
from db import add_credit_card_to_db, fetch_all_credit_cards_from_db, update_card_balance_in_db, do_transfer


class LoginStatus(Enum):
    SUCCESS = 1
    WRONG_PIN = 2
    WRONG_CARD_NUMBER = 3
    NO_SUCH_ACCOUNT = 4


class Bank:
    """A simple Bank class.

    The purpose is to represent a bank that can hold multiple credit card accounts."""

    def __init__(self):
        self._accounts: dict[str, CreditCard] = {}
        self._populate_accounts()

    def add_credit_card(self, credit_card: CreditCard):
        """Add a credit card account to the bank.

        Write card to the database.

        :param credit_card: An instance of CreditCard to be added to the bank.
        """

        self._accounts[str(credit_card)] = credit_card
        add_credit_card_to_db(credit_card.card_number, credit_card.pin)

    def login_action(self, card_number, pin: str) -> LoginStatus:
        """Attempt to log into a credit card.

        :param card_number: The credit card number as a string.
        :param pin: The PIN associated with the credit card.
        :return: LoginStatus indicating the result of the login attempt.
        """
        if not self.validate_card_number(card_number):
            return LoginStatus.WRONG_CARD_NUMBER
        if not self.card_exists(card_number, pin):
            return LoginStatus.NO_SUCH_ACCOUNT
        if not self.validate_pin(card_number, pin):
            return LoginStatus.WRONG_PIN
        return LoginStatus.SUCCESS

    def get_credit_card(self, card_number) -> CreditCard:
        """Retrieve the credit card associated with the given card number.

        :param card_number: The credit card number as a string.
        :return: The CreditCard instance if found, else None.
        """

        return self._accounts[card_number]

    @staticmethod
    def validate_card_number(card_number) -> bool:
        """Check if passed card number is valid.

        For now just checks if it is a string of length 16.

        :param card_number: The credit card number as a string.
        """

        return isinstance(card_number, str) and len(card_number) == 16

    def card_exists(self, card_number, pin) -> bool:
        """Check if account exists in a bank"""

        return card_number in self._accounts

    def validate_pin(self, card_number, pin) -> bool:
        """Check if the PIN is correct for the given card number."""

        try:
            credit_card = self._accounts[card_number]
            if credit_card:
                return credit_card.pin == pin
        except ValueError:
            return False
        return False

    def _populate_accounts(self) -> None:
        """Read card from database and add to class"""
        credit_card_rows = fetch_all_credit_cards_from_db()
        for row in credit_card_rows:
            card = CreditCard.from_db(row['number'], row['pin'], row['balance'])
            self._accounts[row['number']] = card

    def add_income_to_card(self, card_number: str, amount: int) -> None:
        """Add income to the credit card account.

        :param card_number: The credit card number as a string.
        :param amount: The amount to be added to the account balance.
        """

        card = self.get_credit_card(card_number)
        card.add_income(amount)
        update_card_balance_in_db(card_number, card.balance)

    def do_transfer(self, from_card_number: str, to_card_number: str, amount: int) -> bool:
        """Transfer amount from one credit card to another.

        :param from_card_number: The credit card number to transfer from.
        :param to_card_number: The credit card number to transfer to.
        :param amount: The amount to be transferred.
        :return: True if the transfer was successful, False otherwise.
        """

        from_card = self.get_credit_card(from_card_number)
        to_card = self.get_credit_card(to_card_number)

        if from_card.balance < amount:
            return False

        from_card.balance -= amount
        to_card.balance += amount

        do_transfer(from_card_number, to_card_number, amount)

        return True