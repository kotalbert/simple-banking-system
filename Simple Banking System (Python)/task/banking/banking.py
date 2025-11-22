"""Simple Banking System"""
import sys

from bank import Bank, LoginStatus
from credit_card import CreditCard

bank = Bank()

def display_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')


def create_account():
    card = CreditCard()
    bank.add_credit_card(card)
    print('Your card has been created')
    print('Your card number:')
    print(card)
    print('Your card PIN:')
    print(card.pin)


def handle_successful_login(credit_card_number: str):
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    card = bank.get_credit_card(credit_card_number)
    while True:
        command = input()
        match command:
            case '1':
                print(f'Balance: {card.balance}')
            case '2':
                print('You have successfully logged out!')
                return
            case '0':
                sys.exit(0)
            case _:
                pass


def handle_login():
    card_number = input('Enter your card number:')
    pin = input('Enter your PIN:')
    login_status = bank.login_action(card_number, pin)
    match login_status:
        case LoginStatus.SUCCESS:
            print('You have successfully logged in!')
            handle_successful_login(card_number)
        case LoginStatus.WRONG_CARD_NUMBER:
            print('Wrong card number or PIN!')
        case LoginStatus.WRONG_PIN:
            print('Wrong card number or PIN!')
        case LoginStatus.NO_SUCH_ACCOUNT:
            print('No such account!')


def handle_command(command):
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
