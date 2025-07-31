from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, text, insert, select, Table, Column, DateTime, MetaData, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.exc import OperationalError, SQLAlchemyError, ArgumentError, IntegrityError, DataError, ProgrammingError
from datetime import datetime
from config import settings
from typing import Annotated

str_256 = Annotated[str,256]

class Base(DeclarativeBase):
    '''
    Класс наследуемые от ORM SQL Alchemy для создания моделей
    '''                   
    type_annotation_map = {
        str_256: String(256)            #создание кастомных типов данных в моделях
    }
    pass

engine = create_async_engine(
    url=settings.url_asyncpg,
    echo=True
)

session_factory = async_sessionmaker(engine)            #фабрика создания сессий для подлючения к базе данных