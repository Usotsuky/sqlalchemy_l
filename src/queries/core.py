from sqlalchemy import insert, select, text
from src.database import sync_engine
from src.models import metadata, workers_table, customers


def create_table():
    sync_engine.echo = False
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # interactive
        # stmt = """
        #    insert into worker (user_name) values
        #    ('Nurdos'),
        #    ('Erbol');"""

        # query builder
        # stmt = insert(workers_table).values(
        #     [
        #         {'user_name': 'Nurdos'},
        #         {'user_name': 'Uzair'},
        #     ]
        # )
        ins = insert(customers)
        r = conn.execute(ins,[
        {
            "first_name": "Vladimir",
            "last_name": "Belousov",
            "username": "Andescols",
            "email":"andescols@mail.com",
            "address": "Ul. Usmanova, bld. 70, appt. 223",
            "town": " Naberezhnye Chelny"
        },
        {
            "first_name": "Tatyana",
            "last_name": "Khakimova",
            "username": "Caltin1962",
            "email":"caltin1962@mail.com",
            "address": "Rossiyskaya, bld. 153, appt. 509",
            "town": "Ufa"
        },
        {
            "first_name": "Pavel",
            "last_name": "Arnautov",
            "username": "Lablen",
            "email":"lablen@mail.com",
            "address": "Krasnoyarskaya Ul., bld. 35, appt. 57",
            "town": "Irkutsk"
        },
    ])
        print(r.rowcount)
        conn.commit()


def get_data():
    with sync_engine.connect() as conn:
        s = customers.select()
        # r = conn.execute(text("""select * from customers"""))
        r = conn.execute(s)
        print(r.fetchall()[2])


def delete_data():
    with sync_engine.connect() as conn:
        s = customers.delete().where(customers.c.id == 5)
        r = conn.execute(s)
        print(r)
