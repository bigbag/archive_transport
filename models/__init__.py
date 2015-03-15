import asyncio
import logging
__all__ = (
    'insert_data',
)


@asyncio.coroutine
def insert_data(engine, model, data):
    with (yield from engine) as conn:
        trans = yield from conn.begin()
        try:
            yield from conn.execute(model.table.insert().values(data))
        except Exception as e:
            logging.debug("Exception: %(body)s", {'body': e})
            yield from conn.connection.ping()
        finally:
            try:
                yield from trans.commit()
            except Exception as e:
                logging.exception("Exception: %(body)s", {'body': e})
                yield from trans.rollback()
