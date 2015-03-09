import logging

import asyncio
from aiohttp import web
from views import Handler

try:
    from settings_local import Config
except:
    from settings import Config


app = web.Application()

handler = Handler()
app.router.add_route('GET', '/intro', handler.handle_intro)
app.router.add_route('GET', '/greet/{name}', handler.handle_greeting)

loop = asyncio.get_event_loop()
f = loop.create_server(app.make_handler(), Config.APP_HOST, Config.APP_PORT)
srv = loop.run_until_complete(f)
logging.info('Start server {}:{}'.format(Config.APP_HOST, Config.APP_PORT))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
