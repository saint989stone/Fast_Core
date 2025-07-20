from sqlalchemy.ext.asyncio import create_async_engine, async_session, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text, insert, select, Table, Column, DateTime, MetaData, ForeignKey, Integer, String, SmallInteger, String
from sqlalchemy.exc import OperationalError, SQLAlchemyError, ArgumentError, IntegrityError, DataError, ProgrammingError
from datetime import datetime

class Database:
    '''
    Класс создания подключения к базе данных и методов работы с ней

    Attributes:
        dsn (str): адрес для подключения к базе данных
    '''
    def __init__(self, dsn: str, db_name: str, ) -> None:
        '''
        Функция инициализации объекта базы данных

        Args:
            dsn (str): адрес для подключения к базе данных
        '''
        self.dsn = dsn          #адрес подключения к базе данных
        self.db_name = db_name          #имя базы данных
        self.engine = None          #объект подключения к базе данных
        self.metadata = MetaData()          #объект содержащий структуру базы данных
        self.define_tables()            #запуск функции инициализации базы данных

    async def create_engine(self)-> bool:
        '''
        Функция создания движка базы данных и проверки подключения к базе данных
        '''
        result = False
        try:
            self.engine = create_engine(
            url=self.dsn,
            echo = True,            #Посылает SQL запросы в консоль
            pool_size=5,            #Количество соединений к БД
            max_overflow=10         #Количество дополнительных соединений к БД
            )
            print(f'Создание движка подключения к базе данных {self.db_name} прошло успешно')       #LOG
        except (OperationalError, SQLAlchemyError) as error:
            result = False
            print(f'При создании движка подключения к базе данных {self.db_name} произошла ошибка {error}')         #LOG
        try:
            async with self.engine.connect() as connect_engine:
                responce = await connect_engine.execute(text('SELECT VERSION()'))           #для проверки доступности базы данных делаем запрос на получение версии базы данных. Типы запросов .scalar() — если запрос возвращает одно значение; .fetchone() — получить первую строку в виде кортежа; .fetchall() - получить все строки
                if 'PostgreSQL' in responce.scalar():
                    result = True
                    print (f'Подключение к базе данных {self.db_name} {responce} прошло успешно')          #LOG
        except (OperationalError, SQLAlchemyError) as error:
            result = False
            print(f'Подключение к базе данных {self.db_name} прошло с ошибкой {error}')         #LOG
        return result