"""A database module for a simple banking system using SQLite."""
import sqlite3

def get_connection():
    """Establishes and returns a connection to the SQLite database."""

    conn = sqlite3.connect('card.s3db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database by creating the necessary tables."""

    conn = get_connection()
    cursor = conn.cursor()
    with get_connection() as conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS card
                       (
                           id INTEGER PRIMARY KEY,
                           number TEXT,
                           pin TEXT,
                           balance INTEGER DEFAULT 0
                       );
                       """)
        conn.commit()


def add_credit_card_to_db(card_number: str, pin: str):
    """Adds a new credit card to the database.

    :param card_number: The credit card number as a string.
    :param pin: The PIN associated with the credit card.
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO card (number, pin, balance)
                       VALUES (?, ?, 0);
                       """, (card_number, pin))
    conn.commit()

def fetch_all_credit_cards_from_db() -> list[sqlite3.Row]:
    """Fetches all credit cards from the database.

    :return: A list of sqlite3.Row objects representing the credit cards.
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT number, pin, balance FROM card;")
        rows = cursor.fetchall()
    return rows

def update_card_balance_in_db(card_number: str, new_balance: int):
    """Updates the balance of a credit card in the database.

    :param card_number: The credit card number as a string.
    :param new_balance: The new balance to be set.
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE card
                       SET balance = ?
                       WHERE number = ?;
                       """, (new_balance, card_number))
    conn.commit()