import asyncio
import logging
__all__ = (
    'insert_data',
)


@asyncio.coroutine
def insert_data(engine, model, data):
    logging.debug("Insert in %(name)s", {'name': model.__name__})
    logging.debug("Data %(data)s", {'data': data})

    with (yield from engine) as conn:
        try:
            yield from conn.execute(model.table.insert().values(data))
        except Exception as e:
            yield from conn.connection.ping()
            logging.debug("Info: %(body)s", {'body': e})
        finally:
            try:
                yield from conn.connection.commit()
            except Exception as e:
                logging.exception("Exception: %(body)s", {'body': e})
