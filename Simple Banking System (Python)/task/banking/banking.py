"""Simple Banking System"""
import sys

from credit_card import CreditCard


def display_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')


def create_account():
    card = CreditCard()
    print('Your card has been created')
    print('Your card number:')
    print(card)
    print('Your card PIN:')
    print(card.pin)


def handle_command(command):
    match command:
        case '1':
            create_account()
        case '2':
            pass
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
