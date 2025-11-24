"""Credit Card module for Simple Banking System."""
from __future__ import annotations

import random

from utils import digits_to_string


class CreditCard:
    """A simple Credit Card class.

    Assumptions about credit card number:
    - It is a 16-digit number.
    - The first 6 digits (Bank Identification Number) are to be 400000
    - Seventh digit to fifteenth digits are the customer account number, can be random
    - The last digit is a checksum, but for now can be random

    Attributes:
        _digits (List[int]): The credit card number, represented as array of integers.
        balance (int): The balance of the credit card account.
    """

    def __init__(self):
        self._digits = self._generate_card_number()
        self._pin = f'{random.randint(0, 9999):04}'
        self.balance = 0

    @staticmethod
    def _generate_card_number() -> list[int]:
        """Generate a random credit card number, taking into consideration the assumptions.

        :return: A list of integers representing the credit card number.
        """

        card_number = [4, 0, 0, 0, 0, 0]  # Bank Identification Number
        # Generate 9 random digits for the customer account number
        for _ in range(9):
            card_number.append(random.randint(0, 9))
        #  calculate checksum digit for firs 15 digits (Luhn algorithm can be implemented later)
        checksum = CreditCard._calculate_checksum(card_number)
        card_number.append(checksum)

        return card_number

    @property
    def card_number(self) -> str:
        """Get the credit card number as a string.

        :return: The credit card number as a string.
        """

        return digits_to_string(self._digits)

    @property
    def pin(self) -> str:
        """Get the PIN of the credit card.

        :return: The PIN as a string.
        """

        return self._pin

    def __repr__(self):
        return digits_to_string(self._digits)

    @staticmethod
    def _calculate_checksum(card_number: list[int]) -> int:
        """Calculate the checksum digit for the credit card number using Luhn algorithm.

        :param card_number: The first 15 digits of the credit card number.
        :return: The checksum digit.
        """

        def luhn_double(n: int) -> int:
            n *= 2
            if n > 9:
                n -= 9
            return n

        total = 0
        for i, digit in enumerate(card_number):
            if i % 2 == 0:
                total += luhn_double(digit)
            else:
                total += digit

        checksum = (10 - (total % 10)) % 10
        return checksum

    @staticmethod
    def verify_luhn(card_number: str) -> bool:
        """Verify if the credit card number is valid using Luhn algorithm.

        :param card_number: The credit card number as a string.
        :return: True if the card number is valid, False otherwise.
        """

        digits = [int(d) for d in card_number]
        checksum_digit = digits.pop()  # Remove the last digit (checksum)
        calculated_checksum = CreditCard._calculate_checksum(digits)
        return checksum_digit == calculated_checksum

    @staticmethod
    def from_db(number: str, pin: str, balance: int) -> CreditCard:
        # this will init a new card number and pin, but I need to override them
        card = CreditCard()
        card._digits = [int(d) for d in number]  # unpack string to list of digits
        card._pin = pin
        card.balance = balance
        return card

    def add_income(self, amount: int):
        self.balance += amount
