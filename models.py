from database import get_connection


def insert_log(
    api_name,
    status,
    severity,
    response_time
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO logs
        (
            api_name,
            status,
            severity,
            response_time
        )

        VALUES (?, ?, ?, ?)

    """, (
        api_name,
        status,
        severity,
        response_time
    ))

    conn.commit()

    conn.close()


def fetch_logs():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *
        FROM logs
        ORDER BY timestamp DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]