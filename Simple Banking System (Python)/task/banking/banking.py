"""Simple Banking System"""
import sys

from bank import Bank, LoginStatus
from credit_card import CreditCard
from db import init_db

init_db()
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

def display_account_menu():
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')

def handle_successful_login(credit_card_number: str):
    display_account_menu()
    card = bank.get_credit_card(credit_card_number)
    while True:
        command = input()
        match command:
            case '1':
                print(f'Balance: {card.balance}')
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                print('You have successfully logged out!')
                return
            case '0':
                sys.exit(0)
            case _:
                pass


def handle_login():
    card_number = input('Enter your card number: ')
    pin = input('Enter your PIN: ')
    login_status = bank.login_action(card_number, pin)
    match login_status:
        case LoginStatus.SUCCESS:
            print('You have successfully logged in!')
            handle_successful_login(card_number)
        case _:
            print('Wrong card number or PIN!')


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
