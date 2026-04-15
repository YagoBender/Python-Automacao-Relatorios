import sqlite3

def connect():
    return sqlite3.connect("dados.db")

def save_data(data):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER,
        title TEXT
    )
    """)

    for item in data:
        cursor.execute("INSERT INTO posts VALUES (?, ?)",
                       (item['id'], item['title']))

    conn.commit()
    conn.close()

def fetch_data():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts LIMIT 10")
    result = cursor.fetchall()

    conn.close()
    return result
