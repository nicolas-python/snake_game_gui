import sqlite3

def init_db():
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def save_player(name):
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO players (name, score) VALUES (?, ?)",
        (name, 0)
    )

    conn.commit()
    conn.close()
