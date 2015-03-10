import asyncio
from aiohttp import web


@asyncio.coroutine
def is_json(request):
    try:
        data = yield from request.json()
    except:
        return web.HTTPBadRequest()
    else:
        return data
