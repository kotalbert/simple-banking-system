"""Simple Banking System"""
import sys

from bank import Bank, LoginStatus
from credit_card import CreditCard
from db import init_db

init_db()
bank = Bank()


def display_menu() -> None:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')


def create_account() -> None:
    card = CreditCard()
    bank.add_credit_card(card)
    print('Your card has been created')
    print('Your card number:')
    print(card)
    print('Your card PIN:')
    print(card.pin)


def display_account_menu() -> None:
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')


def handle_add_income(card: CreditCard) -> None:
    print('Enter income:')
    income = int(input())
    bank.add_income_to_card(card.card_number, income)
    print('Income was added!')
    print()


def handle_transfer(card) -> None:
    """Handle money transfer from one card to another.

    This function validate if card exists, if the card number is valid.
    Check if there are enough funds to make the transfer.
    Prompt user for necessary inputs and display appropriate messages.

    :param card:
    :return:
    """
    print('Transfer')
    print('Enter card number:')
    to_card_number = input()

    if not bank.validate_card_number(to_card_number):
        print('Probably you made a mistake in the card number. Please try again!')
        print()
        return

    if to_card_number == card.card_number:
        print("You can't transfer money to the same account!")
        print()
        return

    if not bank.card_exists(to_card_number):
        print('Such a card does not exist.')
        print()
        return

    print('Enter how much money you want to transfer:')
    amount = int(input())

    if amount > card.balance:
        print('Not enough money!')
        print()
        return

    bank.do_transfer(card.card_number, to_card_number, amount)
    print('Success!')
    print()


def handle_close_account(card: CreditCard) -> None:
    bank.close_account(card.card_number)
    print('The account has been closed!')


def handle_successful_login(credit_card_number: str) -> None:
    card = bank.get_credit_card(credit_card_number)
    while True:
        display_account_menu()
        command = input()
        match command:
            case '1':
                handle_show_balance(card)
            case '2':
                handle_add_income(card)
            case '3':
                handle_transfer(card)
            case '4':
                handle_close_account(card)
                print('You have successfully logged out!')
                return
            case '0':
                sys.exit(0)
            case _:
                pass


def handle_show_balance(card: CreditCard) -> None:
    print(f'Balance: {card.balance}')
    print()


def handle_login() -> None:
    card_number = input('Enter your card number: ')
    pin = input('Enter your PIN: ')
    login_status = bank.login_action(card_number, pin)
    match login_status:
        case LoginStatus.SUCCESS:
            print('You have successfully logged in!')
            handle_successful_login(card_number)
        case _:
            print('Wrong card number or PIN!')


def handle_command(command) -> None:
    match command:
        case '1':
            create_account()
        case '2':
            handle_login()
        case '0':
            sys.exit(0)
        case _:
            pass


def main():
    while True:
        display_menu()
        command = input()
        handle_command(command)


if __name__ == "__main__":
    main()
