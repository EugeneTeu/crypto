import requests
import json
import base64
import hmac
import hashlib
import datetime
import time
import os
import ssl
import websocket

from dotenv import load_dotenv
load_dotenv()
# BASE_URL = "https://api.sandbox.gemini.com/v1"
# API_KEY = os.environ["API_KEY_TEST"]
# API_SECRET = os.environ["API_SECRET_TEST"].encode()
# WEB_SOCKET_URL = "wss://api.sandbox.gemini.com/v1"

BASE_URL = "https://api.gemini.com/v1"
API_KEY = os.environ["REAL_API_KEY"]
API_SECRET = os.environ["REAL_API_SECRET"].encode()
WEB_SOCKET_URL = "wss://api.gemini.com/v1"

# ------------------------------------------------------------------------------
# Util
# ------------------------------------------------------------------------------


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
    response = requests.get(BASE_URL + "/symbols")
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


def getMarketData(symbol):
    # {"type": "update", "eventId": 1320430971, "timestamp": 1639622222, "timestampms": 1639622222393, "socket_sequence": 2, "events": [
    #     {"type": "change", "side": "bid", "price": "49039.93", "remaining": "0", "delta": "-0.04078309", "reason": "cancel"}]}
    currPrice = -1
    currAmt = -1

    def on_message(ws, msg):
        # To keep an up-to-date order book, just watch for any events with {"type": "change"},
        # and update the price level at price with the amount at remaining. The initial response message will contain all the change events necessary to populate your order book from scratch.
        events = eval(msg).get("events")

        for event in events:
            if event.get("type") == "change":
                currPrice = event.get("price")
                currAmt = event.get("remaining")
                print(symbol + " price:$" + currPrice + " amt:" + currAmt)

    url = WEB_SOCKET_URL + "/marketdata/" + symbol
    ws = websocket.WebSocketApp(url, on_message=on_message)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    # ------------------------------------------------------------------------------
    #  Buy and sell market orders
    # ------------------------------------------------------------------------------


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


def placeSellOrder(symbol, amount, price):
    url = BASE_URL + "/order/new"
    payload_nonce = createNonce()
    payload = {
        "nonce": payload_nonce,
        "request": "/v1/order/new",
        "symbol": symbol,
        "amount": amount,
        "price": price,
        "side": "sell",
        "type": "exchange limit",
        "options": ["maker-or-cancel"]
    }
    res = encodePayloadAndPost(payload, url)
    print(res)
