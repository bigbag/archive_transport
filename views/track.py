import logging
import json
import asyncio

from aiohttp import web

from helpers.http_helper import is_json
from models.bus_track import BusTrack
from models.card_track import CardTrack
from models.map_point import MapPoint
from forms.track import CardTrackForm, BusTrackForm


class Track:

    def __init__(self):
        pass

    @asyncio.coroutine
    def set_card_track(self, request):

        data = yield from is_json(request)
        form = CardTrackForm.from_json(data)
        if not form.validate():
            return web.HTTPBadRequest()

        data['status'] = CardTrack.STATUS_NEW
        card_track = CardTrack.table
        with (yield from request.app['db']) as conn:
            trans = yield from conn.begin()
            yield from conn.execute(card_track.insert().values(data))
            yield from trans.commit()

            logging.debug("Insert new card tack")
            logging.debug(data)

        return web.Response(text=json.dumps({'status': 'ok'}),
                            content_type='application/json')

    @asyncio.coroutine
    def set_bus_track(self, request):

        data = yield from is_json(request)
        form = BusTrackForm.from_json(data)
        if not form.validate():
            return web.HTTPBadRequest()

        bus_track = BusTrack.table
        with (yield from request.app['db']) as conn:
            trans = yield from conn.begin()
            yield from conn.execute(bus_track.insert().values(data))
            yield from trans.commit()

            logging.debug("Insert new bus tack")
            logging.debug(data)

        return web.Response(text=json.dumps({'status': 'ok'}),
                            content_type='application/json')
