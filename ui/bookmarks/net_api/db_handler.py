"""
db_handler.py
Keyword: net_api_db

Zapisywanie danych w SQLite lub PostgreSQL.
Uproszczony przykład SQLite z modułem `sqlite3`.
"""

import sqlite3
import os

DB_FILE = "promo_data.db"

def init_db():
    """
    Tworzy tabelę 'history' jeśli nie istnieje.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_link_to_db(url):
    """
    Zapisuje pojedynczy URL do tabeli 'history'.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO history (url) VALUES (?)", (url,))
    conn.commit()
    conn.close()

def load_history_from_db():
    """
    Pobiera historię z bazy.
    Zwraca listę krotek (id, url, date).
    """
    if not os.path.exists(DB_FILE):
        return []
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, url, date FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows
