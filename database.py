import asyncio
from aiomysql.sa import create_engine

try:
    from settings_local import Config
except:
    from settings import Config


@asyncio.coroutine
def init_engine():
    result = yield from create_engine(**Config.DB_CONFIG)
    return result
