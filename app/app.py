from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():

        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD")
        )
        return conn


@app.route('/')
def index():
    conn = get_db_connection()
    if isinstance(conn, str):
        return conn  
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Database connected: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5030)
