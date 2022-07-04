from typing import Union

import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect("")
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        pssword=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchnone()}")
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if  connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
