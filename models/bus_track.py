import sqlalchemy as sa


class BusTrack(object):

    __name__ = 'bus track'

    metadata = sa.MetaData()

    TYPE_START = 'start'
    TYPE_MOVE = 'move'
    TYPE_STOP = 'stop'

    KEYS = ['blockid', 'lat', 'lon', 'event', 'time']

    table = sa.Table(
        'bus_track',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('blockid', sa.String(128), nullable=False),
        sa.Column('time', sa.Integer, nullable=False),
        sa.Column('lat', sa.Float, nullable=False),
        sa.Column('lon', sa.Float, nullable=False),
        sa.Column('event', sa.String(32), nullable=False),
    )
