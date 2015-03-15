import os

from helpers.logging_helper import setup_loggers

os_env = os.environ


class Config(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    APP_HOST = '0.0.0.0'
    APP_PORT = 7777

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # MAIL
    MAIL_DEFAULT_SENDER = ""
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

    # TIMEZONES
    TIME_ZONE = 'Europe/Moscow'

    # DATABASES
    SQLALCHEMY_USER = ''
    SQLALCHEMY_PASSWORD = ''
    SQLALCHEMY_DB = ''
    SQLALCHEMY_HOST = ''
    SQLALCHEMY_PORT = ''
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = True

    DB_CONFIG = {'user': SQLALCHEMY_USER,
                 'password': SQLALCHEMY_PASSWORD,
                 'db': SQLALCHEMY_DB,
                 'host': SQLALCHEMY_HOST,
                 'port': SQLALCHEMY_PORT}

    # TEMP
    TEMP_DIR = os.path.join(PROJECT_ROOT, 'tmp')

    # LOGGING
    LOG_ENABLE = True
    LOG_LEVEL = 'ERROR'
    LOG_MAX_SIZE = 1024 * 1024
    LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
    LOG_SETTINGS = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(levelname)s] [P:%(process)d] [%(asctime)s] %(pathname)s:%(lineno)d: %(message)s',
                'datefmt': '%d/%b/%Y %H:%M:%S',
            },
            'simple': {
                'format': '[%(levelname)s] [%(asctime)s] %(message)s',
                'datefmt': '%d/%b/%Y %H:%M:%S',
            },
        }
    }

    setup_loggers(LOG_SETTINGS, LOG_ENABLE, LOG_LEVEL, LOG_DIR, LOG_MAX_SIZE)

    # SMS
    SMS_URL = ''

    SMS_API_ID = ''
    SMS_LOGIN = ''
    SMS_PASSWORD = ''

    SMS_PARTNER_ID = ''
    SMS_SENDER_NAME = False

    REQUEST_TIMEOUT = 10  # 10 sec
