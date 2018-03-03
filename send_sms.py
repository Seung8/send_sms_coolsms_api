import requests
import hmac
import uuid
import time
import requests

from _md5 import md5


# send sms using coolsms rest api
def send_sms(to, content):
    api_key = 'your coolsms api key'
    api_secret = 'your coolsms api secret key'
    salt = str(uuid.uuid1())
    timestamp = str(int(time.time()))
    data = timestamp + salt
    signature = hmac.new(api_secret.encode(), data.encode(), md5)

    # coolsms rest api v2(example)
    url = 'https://api.coolsms.co.kr/sms/2/send'

    data = {
        'api_key': api_key,
        'signature': signature.hexdigest(),
        'timestamp': timestamp,
        'salt': salt,
        'to': to,
        'from': 'sender number',
        'text': content,
    }

    requests.post(url, data=data)
    print('send message to: {}, content: {}'.format(to, content)
