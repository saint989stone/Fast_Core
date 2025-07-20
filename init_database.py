from database_old import Database
from config import Settings
import time

db = Database(*Settings.url_asyncpg)
db.create_engine()
#db.delete_tables()
#db.create_tables()
