from sqlalchemy import text
from database import engine, session_factory
from models import Base, Devices
from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
import asyncio

async def create_tables():
    engine.echo = True
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
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
            ip_address = '192.168.0.1',
            jump_host = '12389',
            type_device = 'juniper',
            hostname = '23-KRDR-AR1',
            region = 'UG',
            filial = 'KRDR',
            function = 'AR',
            level = 'RSPD',
            territory = 'KRDR',
            group = 'KRDR-AR',
            utc = 3,
            id_host_zabbix = 23456,
            instance_zabbix = 'rspd',
            count_ar = 0,
            count_unvail = 0
            )
        session.add_all([device])
        await session.commit()

asyncio.run(insert_data())