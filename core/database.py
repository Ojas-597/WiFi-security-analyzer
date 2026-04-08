import sqlite3

def init_db():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY,
        activity TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def log_activity(activity):
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()

    c.execute("INSERT INTO logs (activity) VALUES (?)", (activity,))
    conn.commit()
    conn.close()
