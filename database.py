import sqlite3

def init_db():
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER DEFAULT 0,
        time INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def get_players():
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM players")
    players = cursor.fetchall()

    conn.close()

    return players

def save_player(name):
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO players (name, score) VALUES (?, ?)",
        (name, 0)
    )

    conn.commit()
    conn.close()

def delete_player(name):
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM players WHERE name = ?", (name,))

    conn.commit()
    conn.close()

def get_scores():
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, score, time FROM players ORDER BY score DESC")
    scores = cursor.fetchall()

    conn.close()
    return scores

def save_score(name,score, time):
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE players SET score = ?, time = ? WHERE name = ?",(score, time, name))

    conn.commit()
    conn.close()

def get_highscores():
    conn = sqlite3.connect("snake.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, score, time
        FROM players
        ORDER BY score DESC
        LIMIT 3
    """)

    return cursor.fetchall()