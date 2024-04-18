from sqlalchemy import insert
from src.database import sync_engine, sync_session
from src.models import metadata, WorkerORM


def create_table():
    sync_engine.echo = False
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)
    sync_engine.echo = True

def insert_data():
    with sync_session() as session:
        worker_bobr = WorkerORM(user_name="Bobr")
        worker_volk = WorkerORM(user_name="Bobr")
        session.add_all([worker_bobr, worker_volk])
        session.commit()
