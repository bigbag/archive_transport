import math

import sqlalchemy as sa


class Point(object):

    __name__ = 'point'

    metadata = sa.MetaData()

    TYPE_SCHOOL = 1
    TYPE_HOME = 2

    DISTANCE = float(100)  # расстояние, м
    EQUATOR = float(40075000)  # длинна экватора, м

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

    @staticmethod
    def get_nearby(lat, lon):
        """Получает точки в квадрате со сторонами 2*DISTANCE с центром в переданных координатах"""
        lat_delta = Point.DISTANCE * 360 / Point.EQUATOR
        lon_delta = Point.DISTANCE * 360 / \
            (Point.EQUATOR * math.cos(math.radians(lat)))

        query = Point.query.filter(
            Point.lat.between(lat - lat_delta, lat + lat_delta))
        query = query.filter(
            Point.lon.between(lon - lon_delta, lon + lon_delta))

        return query.all()
