import time
from ddtrace import patch_all, tracer

from db import setup_connection, close_connection
from log import logger

# tracer.configure(hostname="datadog-agent", port="8126")


def insert_row(db_conn, text):
    with db_conn.cursor() as curs:
        curs.execute(
            """
            insert into test_table (text) values (%s);
            """,
            (text,),
        )


# @tracer.wrap(service="consumer-proc")
def consume(db_conn):
    logger.info("Waiting for data image...")

    while True:
        logger.info("Inserting message...")

        insert_row(db_conn, "Hello World")

        logger.info("Done. Sleeping...")
        time.sleep(3)


# Setup connection to db
db_conn = setup_connection()

try:
    consume(db_conn)
except Exception as e:
    logger.exception("Consuming process has failed")
finally:
    # Close our DB connection
    close_connection()
