import hashlib
import logging
import time

import asyncio
from external_services import api_request


class SmsruApi(object):

    METHODS = {
        'get_token': 'auth/get_token',
        'sms_send': 'sms/send',
        'sms_status': 'sms/status',
        'get_balance': 'my/balance',
        'get_limit': 'my/limit',
    }

    SUCCESS_STATUS = 100

    SEND_STATUS = {
        100: "Message accepted",
        201: "Out of money",
        202: "Bad recipient",
        203: "Message text not specified",
        204: "Bad sender (unapproved)",
        205: "Message too long",
        206: "Day message limit reached",
        207: "Can't send messages to that number",
        208: "Wrong time",
        209: "Blacklisted recipient",
        210: "Bad method! Use GET, where you must use POST",
        211: "Method not found",
        212: "Message to be transmitted in UTF-8 (you passed in a different encoding)",
        220: "The service is temporarily unavailable, please try later.",
        230: "One phone on the day you can not send more than 250 messages",
        300: "Wrong token",
        301: "Wrong password or user not found",
        302: "The user is authenticated, but the account is not certified"
    }

    SMS_STATUS = {
        -1: "Message not found",
        100: "Message is in the queue",
        101: "Message is on the way to the operator",
        102: "Message is on the way to the recipient",
        103: "Message delivered",
        104: "Message failed: out of time",
        105: "Message failed: cancelled by the operator",
        106: "Message failed: phone malfunction",
        107: "Message failed, reason unknown",
        108: "Message declined",
    }

    COST_STATUS = {
        100: "Success"
    }

    def __init__(self, settings):
        self.settings = settings
        self.token = None
        self.sign = None
        self.token_ts = 0

    def get_url(self, method):
        if method not in self.METHODS:
            return False

        return "%(url)s/%(method)s" % {
            'url': self.settings.SMS_URL,
            'method': self.METHODS[method]}

    def get_sign(self):
        if not self.token:
            logging.debug(u'Not found token')
            return

        value = "%(password)s%(token)s" % {
            'password': self.settings.SMS_PASSWORD,
            'token': self.token}
        self.sign = hashlib.sha512(value.encode('utf-8')).hexdigest()

    @asyncio.coroutine
    def get_token(self):
        if self.token_ts < time.time() - 500:
            self.token = None

        if self.token is None:
            self.token = yield from api_request(
                method='GET',
                url=self.get_url('get_token'))
            if self.token:
                self.token = self.token.decode(encoding='UTF-8')
            self.token_ts = time.time()

    @asyncio.coroutine
    def init_request(self):
        yield from self.get_token()
        self.get_sign()

        if not self.token or not self.sign:
            return
        return True

    @asyncio.coroutine
    def send_sms(self, to, text):
        result = yield from self.init_request()
        if not result:
            return

        data = {
            'login': self.settings.SMS_LOGIN,
            'token': self.token,
            'sha512': self.sign,
            'to': to,
            'text': text.encode("utf-8")
        }

        if self.settings.SMS_SENDER_NAME:
            data['from'] = self.settings.SMS_SENDER_NAME

        result = yield from api_request(
            method='POST',
            url=self.get_url('sms_send'),
            data=data)
        if not result:
            return

        try:
            result = result.decode("utf-8").split("\n")
        except Exception as e:
            logging.exception("Exception: %(body)s", {'body': e})
            return

        code = int(result[0])
        if code == self.SUCCESS_STATUS:
            logging.debug("SMS id %(id)s send.", {'id': result[1]})
            return True

        logging.error("SMS not send. Code %(code)s, %(msg)s",
                      {'code': code, 'msg': self.SEND_STATUS[code]})

    @asyncio.coroutine
    def get_sms_status(self, sms_id):
        result = yield from self.init_request()
        if not result:
            return

        data = {
            'login': self.settings.SMS_LOGIN,
            'token': self.token,
            'sha512': self.sign,
            'id': sms_id,
        }

        result = yield from api_request(
            method='POST',
            url=self.get_url('sms_status'),
            data=data)
        if not result:
            return

        try:
            status = int(result.decode("utf-8"))
        except Exception as e:
            logging.exception("Exception: %(body)s", {'body': e})
            return

        return status

    @asyncio.coroutine
    def get_balance(self):
        result = yield from self.init_request()
        if not result:
            return

        data = {
            'login': self.settings.SMS_LOGIN,
            'token': self.token,
            'sha512': self.sign,
        }

        result = yield from api_request(
            method='POST',
            url=self.get_url('get_balance'),
            data=data)
        if not result:
            return

        try:
            result = result.decode("utf-8").split("\n")
        except Exception as e:
            logging.exception("Exception: %(body)s", {'body': e})
            return

        code = int(result[0])
        if code == self.SUCCESS_STATUS:
            return result[1]

        logging.error("The balance is not received. Code %(code)s, %(msg)s",
                      {'code': code, 'msg': self.SEND_STATUS[code]})

    @asyncio.coroutine
    def get_limit(self):
        result = yield from self.init_request()
        if not result:
            return

        data = {
            'login': self.settings.SMS_LOGIN,
            'token': self.token,
            'sha512': self.sign,
        }

        result = yield from api_request(
            method='POST',
            url=self.get_url('get_limit'),
            data=data)
        if not result:
            return

        try:
            result = result.decode("utf-8").split("\n")
        except Exception as e:
            logging.exception("Exception: %(body)s", {'body': e})
            return

        code = int(result[0])
        if code == self.SUCCESS_STATUS:
            return result[1]

        logging.error("The limit is not received. Code %(code)s, %(msg)s",
                      {'code': code, 'msg': self.SEND_STATUS[code]})
