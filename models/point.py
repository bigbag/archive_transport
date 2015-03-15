import asyncio
import logging
import math

import sqlalchemy as sa


class Point(object):

    __name__ = 'point'

    metadata = sa.MetaData()

    TYPE_SCHOOL = 1
    TYPE_HOME = 2

    DISTANCE = float(100)  # meter
    EQUATOR = float(40075000)  # length of the equator, meter

    table = sa.Table(
        'point',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lat', sa.Float, nullable=False),
        sa.Column('lon', sa.Float, nullable=False),
        sa.Column('code128', sa.String(128)),
        sa.Column('hard_id', sa.String(32), nullable=False),
        sa.Column('type', sa.Integer, nullable=False),
        sa.Column('address', sa.String(256)),
    )

    @asyncio.coroutine
    def get_nearby(self, engine, lat, lon):
        lat_delta = self.DISTANCE * 360 / self.EQUATOR
        lon_delta = self.DISTANCE * 360 / \
            (self.EQUATOR * math.cos(math.radians(lat)))

        point = self.table
        stmt = point.select().\
            where(point.c.lat.between(lat - lat_delta, lat + lat_delta)). \
            where(point.c.lon.between(lon - lon_delta, lon + lon_delta))
        with (yield from engine) as conn:
            try:
                result = yield from conn.execute(stmt)
            except Exception as e:
                logging.exception("Exception: %(body)s", {'body': e})
            else:
                return result
