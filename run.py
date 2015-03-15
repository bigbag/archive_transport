import logging

import asyncio
from aiohttp import web
from aiomysql.sa import create_engine
from views import track

try:
    from settings_local import Config
except:
    from settings import Config


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app['db'] = yield from create_engine(**Config.DB_CONFIG)
    app['config'] = Config

    track_views = track.Track()
    app.router.add_route('POST', '/card/track/', track_views.set_card_track)
    app.router.add_route('POST', '/bus/track/', track_views.set_bus_track)

    srv = yield from loop.create_server(app.make_handler(),
                                        Config.APP_HOST,
                                        Config.APP_PORT)
    logging.info('Start server {}:{}'.format(Config.APP_HOST, Config.APP_PORT))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
