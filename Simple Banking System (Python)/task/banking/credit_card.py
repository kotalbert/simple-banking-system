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
        #  calculate checksum digit for firs 15 digits (Luhn algorithm can be implemented later)
        checksum = CreditCard.calculate_checksum(card_number)
        card_number.append(checksum)

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

    @staticmethod
    def calculate_checksum(card_number: list[int]) -> int:
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
