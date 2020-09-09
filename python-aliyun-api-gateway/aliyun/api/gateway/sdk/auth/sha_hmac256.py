import hmac
import hashlib
import base64


def sign(source, secret):
    h = hmac.new(secret.encode('utf-8'), source.encode('utf-8'), digestmod=hashlib.sha256)
    signature = base64.encodebytes(h.digest()).strip()
    return signature



