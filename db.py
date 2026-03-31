import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="testdb",
        user="postgres",
        password="postgres",
        port="5433"
    )
    return conn

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print("Error:", e)