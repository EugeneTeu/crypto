import requests
import json
import base64
import hmac
import hashlib
import datetime
import time
import os
from dotenv import load_dotenv
load_dotenv()
# BASE_URL = "https://api.sandbox.gemini.com/v1"
# API_KEY = os.environ["API_KEY_3"]
# API_SECRET = os.environ["API_SECRET_3"].encode()

BASE_URL = "https://api.gemini.com/v1"
API_KEY = os.environ["REAL_API_KEY"]
API_SECRET = os.environ["REAL_API_SECRET"].encode()


def createNonce():
    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))
    return payload_nonce


def encodePayloadAndPost(payload, url):
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(API_SECRET, b64, hashlib.sha384).hexdigest()
    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': API_KEY,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
    }
    response = requests.post(url, headers=request_headers)
    responseJson = response.json()
    return responseJson


def getAllSymbols():
    response = requests.get(base_url + "/symbols")
    symbols = response.json()
    print(symbols)


def getPastTrades():
    url = BASE_URL + "/mytrades"
    payload_nonce = createNonce()
    payload = {"request": "/v1/mytrades",
               "nonce": payload_nonce, "symbol": "btcusd"}
    return encodePayloadAndPost(payload)


def getActiveOrders():
    url = BASE_URL + "/orders"
    payload_nonce = createNonce()
    payload = {
        "nonce":  payload_nonce,
        "request": "/v1/orders"
    }
    res = encodePayloadAndPost(payload, url)
    print(res)


def placeBuyOrder(symbol, amount, price):
    url = BASE_URL + "/order/new"
    payload_nonce = createNonce()
    payload = {
        "nonce": payload_nonce,
        "request": "/v1/order/new",
        "symbol": symbol,
        "amount": amount,
        "price": price,
        "side": "buy",
        "type": "exchange limit",
        "options": ["maker-or-cancel"]
    }
    res = encodePayloadAndPost(payload, url)
    print(res)


placeBuyOrder("ethsgd", "0.01", "400")
getActiveOrders()
