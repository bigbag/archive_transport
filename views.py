import logging

import asyncio
from aiohttp import web
from database import init_engine
from models.bus_track import BusTrack
from models.map_point import MapPoint


@asyncio.coroutine
def go(request):
    engine = yield from init_engine()

    with (yield from engine) as conn:
        map_point = MapPoint.table
        res = yield from conn.execute(
            map_point.select().where(
                map_point.c.hard_id == '000000000106'
            ))
        for row in res:
            return(row.code128, row.lon)


class Handler:

    def __init__(self):
        pass

    def handle_intro(self, request):
        return web.Response(body=b"Hello, world")

    @asyncio.coroutine
    def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        result = yield from go(request)
        logging.warning("%s" % result[0])
        txt = "Hello, " + name + result[0]

        return web.Response(text=txt, content_type='application/json')
