import sqlite3

def connect():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

def execute_query(query, params=()):
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows
