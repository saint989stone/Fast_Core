from sqlalchemy import text
from database import engine
from models import Base
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

# async def insert_data():
#     async with async_session_factory

session = async_sessionmaker(engine)

asyncio.run(create_tables())