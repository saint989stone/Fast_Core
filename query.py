from orm import AsyncORM
import asyncio

asyncio.run(AsyncORM.select_data_territory("KRDR"))