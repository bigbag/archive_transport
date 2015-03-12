import asyncio


@asyncio.coroutine
def insert_data(engine, model, data):
    with (yield from engine) as conn:
        yield from conn.connection.ping()
        yield from conn.execute(model.table.insert().values(data))
        yield from conn.connection.commit()
