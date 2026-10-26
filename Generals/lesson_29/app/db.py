import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "homework_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        value TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_result(name, value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO results (name, value) VALUES (%s, %s) RETURNING id",
        (name, value),
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id

def update_result(result_id, new_value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE results SET value = %s WHERE id = %s", (new_value, result_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_result(result_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM results WHERE id = %s", (result_id,))
    conn.commit()
    cur.close()
    conn.close()

def get_result(result_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, value FROM results WHERE id = %s", (result_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row