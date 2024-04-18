from config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase


sync_engine = create_engine(
    url=settings.db_url_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

async_engine = create_async_engine(
    url= settings.db_url_asyncpg,
    echo=False
)

# это фабрика сессий, которая используется для создания новых сессий базы данных.
# Эта фабрика определяет параметры соединения и конфигурации сессии,
# которые будут использоваться при создании новой сессии
# In order to interact with the database, we need to obtain its handle.
# A session object is the handle to database. Session class is defined using sessionmaker()
# – a configurable session factory method which is bound to the engine object created earlier.
sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    """ для определения моделей данных, которые представляют таблицы в базе данных
        A base class stores a catlog of classes and mapped tables in the Declarative system.
        This is called as the declarative base class. There will be usually just one
        instance of this base in a commonly imported module.
    """
    pass
