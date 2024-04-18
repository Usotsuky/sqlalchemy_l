import enum
from typing import Optional

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, DateTime, text
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


# Declarative
class WorkerORM(Base):
    __tablename__ = "worker"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumeORM(Base):
    __tabliname__ = "resume"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("worker.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('UTC', now())"))






#Interactive
metadata = MetaData()

workers_table = Table(
    "worker",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(50)),
)

customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("username", String,unique=True),
    Column("email", String),
    Column("address", String),
    Column("town", String),
    Column("created_on", DateTime, default=datetime.now),
    Column("updated_on", DateTime, default=datetime.now, onupdate=datetime.now),
)