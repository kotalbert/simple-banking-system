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
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS card
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY,
                       number
                       TEXT,
                       pin
                       TEXT,
                       balance
                       INTEGER
                       DEFAULT
                       0
                   );
                   ''')
    conn.commit()
    conn.close()
