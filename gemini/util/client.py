import websocket
import requests
import threading
from datetime import datetime
import ssl


class Client(threading.Thread):
    def __init__(self, url, symbol, orderBook, lock):
        super().__init__()
        self.ws = websocket.WebSocketApp(
            url, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close, on_open=self.on_open)
        self.symbol = symbol

        self.orderBook = orderBook[symbol]
        self.lock = lock
        self.updates = 0
        self.last_update = orderBook

    def run(self):
        while True:
            self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def on_message(self, ws, msg):
        # To keep an up-to-date order book, just watch for any events with {"type": "change"},
        # and update the price level at price with the amount at remaining. The initial response message will contain all the change events necessary to populate your order book from scratch.
        with self.lock:
            events = eval(msg).get("events")

            for event in events:
                if event.get("type") == "change":
                    currPrice = event.get("price")
                    currAmt = event.get("remaining")
                    currSide = event.get("side")
                    string = self.symbol + " price:$" + currPrice + \
                        " amt:" + currAmt + " side: " + currSide
                    self.orderBook["latest"] = string

            self.last_update['last_update'] = datetime.now()
        # convert message to dict, process update

    # catch errors
    def on_error(self, ws, error):
        print(error)

    # run when websocket is closed
    def on_close(self, ws):
        print("### closed ###")

    # run when websocket is initialised
    def on_open(self, ws):
        print(f'Connected to {self.symbol}\n')
