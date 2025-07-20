from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, insert, select, Table, Column, DateTime, MetaData, ForeignKey, Integer, String, SmallInteger, String
from sqlalchemy.exc import OperationalError, SQLAlchemyError, ArgumentError, IntegrityError, DataError, ProgrammingError
from datetime import datetime
from config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    url=settings.url_asyncpg,
    echo=True
)

