import os
import psycopg2
from retrying import retry

conn = None

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")


@retry(
    wait_exponential_multiplier=1000,
    wait_exponential_max=10 * 1000,
    stop_max_attempt_number=15,
)
def setup_connection():
    global conn

    if not conn:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB,
        )

    return conn


def close_connection():
    conn.close()
