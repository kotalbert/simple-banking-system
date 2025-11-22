"""Credit Card module for Simple Banking System."""
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
        _balance (int): The balance of the credit card account.
    """

    def __init__(self):
        self._digits = self._generate_card_number()
        self._pin = f'{random.randint(0, 9999):04}'
        self._balance = 0

    @staticmethod
    def _generate_card_number() -> list[int]:
        """Generate a random credit card number, taking into consideration the assumptions.

        :return: A list of integers representing the credit card number.
        """

        card_number = [4, 0, 0, 0, 0, 0]  # Bank Identification Number
        # Generate 9 random digits for the customer account number
        for _ in range(9):
            card_number.append(random.randint(0, 9))
        # Generate a random digit for the checksum
        card_number.append(random.randint(0, 9))
        return card_number

    @property
    def pin(self) -> str:
        """Get the PIN of the credit card.

        :return: The PIN as a string.
        """

        return self._pin

    @property
    def balance(self) -> int:
        return self._balance

    def __repr__(self):
        return digits_to_string(self._digits)
