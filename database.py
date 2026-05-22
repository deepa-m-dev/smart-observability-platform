import sqlite3

DB_NAME = "logs.db"


def get_connection():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            api_name TEXT NOT NULL,

            status TEXT NOT NULL,

            severity TEXT NOT NULL,

            response_time REAL NOT NULL,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()