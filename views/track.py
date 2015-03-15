import json
import logging

import asyncio
from aiohttp import web
from forms.track import BusTrackForm, CardTrackForm
from helpers.http_helper import is_json
from models import insert_data
from models.bus_track import BusTrack
from models.card_track import CardTrack
from models.point import Point


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
        yield from insert_data(request.app['db'], CardTrack, data)

        return web.Response(text=json.dumps({'status': 'ok'}),
                            content_type='application/json')

    @asyncio.coroutine
    def set_bus_track(self, request):

        data = yield from is_json(request)
        form = BusTrackForm.from_json(data)
        if not form.validate():
            return web.HTTPBadRequest()

        yield from insert_data(request.app['db'], BusTrack, data)

        return web.Response(text=json.dumps({'status': 'ok'}),
                            content_type='application/json')
