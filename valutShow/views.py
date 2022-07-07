import psycopg2
from config import host, user, password, db_name
from scriptss.models import data_key_usd, data_value_usd, data_key_eur, data_value_eur

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

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE  valuta(
    #             id serial  PRIMARY KEY,
    #             name_valuta varchar(10) NOT NULL,
    #             cost_rubles varchar(10) NOT NULL)"""
    #     )

    # print("[INFO] Table created successfully ")

    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO valuta (name_valuta, cost_rubles) 
                  VALUES  ('{data_key_usd}', '{data_value_usd}')"""
        )

        print("[INFO] Data was successfully inserted")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
