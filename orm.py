from sqlalchemy import text, select, func, cast, Integer, and_
from database import engine, session_factory
from models import Base, Devices
from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
import asyncio

"""
session.flush() - отправляет в базу данных записи, которые уже внесены в модели, но не записывает их, запись происходит после commit()
session.expire() - отменяет все изменения проведеные в моделях ORM, до записи в базу данных
session.refresh() - позволяет обновить изменения в записи внесенной в модели, до их записи в БД. В Ответ БД возращает актуальные данные. 
"""

class AsyncORM:
    async def create_tables():
        engine.echo = True
        async with engine.begin() as connect:
            await connect.run_sync(Base.metadata.drop_all)          #в CORE данные храниятся в metadata_obj в ORM это объект класса Base
            await connect.run_sync(Base.metadata.create_all)
            #await connect.commit()
        #await engine.dispose()
        engine.echo = True

    async def get_version():
        async with engine.connect() as connect:
            responce = await connect.execute(text('SELECT VERSION()')) 
            print(responce.scalar())

    async def insert_data():
        async with session_factory() as session:
            device = Devices(
                ip_address = '192.168.0.3',
                jump_host = '12389',
                type_device = 'juniper',
                hostname = '64-SPBR-AR1',
                region = 'SZ',
                filial = 'SPBR',
                function = 'AR',
                level = 'RSPD',
                territory = 'SPBR',
                group = 'SPBR-AR',
                utc = 3,
                id_host_zabbix = 23456,
                instance_zabbix = 'rspd',
                count_ar = 0,
                count_unvail = 0
                )
            session.add_all([device])
            await session.commit()

    async def select_data_all():
        """
        Функция получения всех объектов из таблицы базы данных
        """
        async with session_factory() as session:
            stmt = select(Devices)          #выборка по которой осуществляется запрос 
            result = await session.execute(stmt)
            devices = result.scalars().all()            #scalars преобразует результат из объектов в кортежах, в список объектов
            for device in devices:
                print(f"ip_address = {device.ip_address} hostname = {device.hostname}")

    async def get_data():
        """
        Функция получения объекта из таблицы базы данных по его ID
        """
        async with session_factory() as session:
            device = await session.get(Devices, 1)
            print(device.ip_address)

    async def update_data():
        """
        Функция обновления данных в БД
        """
        async with session_factory() as session:
            device = await session.get(Devices, 2)
            device.territory = "TIM"
            await session.commit()

    async def test_select_data_terms(function: str = "AR"):
        """
        Пример функции 
        select function, avg(count_unvail)::int as avg_count
        from devices
        where function like '%AR%' and compensation > 40000
        group by function
        """
        async with session_factory() as session:
            stmt = (
                select(
                    Devices.id_host_zabbix,
                    cast(func.avg(Devices.count_unvail), Integer).label("avg_count"),           #cast приводит значение к определенному типу

                )
                .select_from(Devices)
                .filter(and_(
                    Devices.function.contains(function),
                    Devices.count_ar == 0
                ))
                .group_by(Devices.filial)
            )
            print(stmt.compile(compile_kwargs={"literal_bind": True}))         #compile применяется для постановки параметров в вывод строки

    async def select_data_territory(territory: str):
        async with session_factory() as session:
            stmt = (
                select(Devices)
                .where(Devices.territory == territory)
                )
            print(stmt.compile(compile_kwargs={"literal_bind": True}))         #compile применяется для постановки параметров в вывод строки
            result = await session.execute(stmt)
            devices = result.scalars().all()
            for device in devices:
                print (device.hostname)