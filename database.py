import sqlite3


def init_db():
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_highscore(name, score):
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO highscores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()


def get_highscores():
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM highscores ORDER BY score DESC LIMIT 5")
    scores = cursor.fetchall()
    conn.close()
    return scores