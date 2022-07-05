import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE  valuta(
                id serial  PRIMARY KEY,
                name_valuta varchar(10) NOT NULL,
                cost_rubles varchar(10) NOT NULL)"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO valuta(name_valuta, cost_rubles) VALUES
            () """
        )

        print("[INFO] Table created successfully ")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
