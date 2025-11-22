"""Simple Banking System"""


def display_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')


def handle_command(command):
    match command:
        case 1:
            pass
        case 2:
            pass
        case 0:
            pass
        case _:
            pass


def main():
    while True:
        display_menu()
        command = input()
        handle_command(command)


if __name__ == "__main__":
    main()
