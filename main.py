import threading
import util.client as c
import util.gemini as u
import time
from datetime import datetime

BTC_SYMBOL = "BTCUSD"
ETH_SYMBOL = "ETHUSD"


def process(orderBooks, lock):
    current_time = datetime.now()
    while True:
        try:
            # check for new update
            if orderBooks['last_update'] != current_time:
                with lock:
                    # extract and print data
                    for key, value in orderBooks.items():
                        if key != 'last_update':
                            print(value["latest"])
                    print()
                    # set local last_update to last_update
                    current_time = orderBooks['last_update']
            time.sleep(1)
        except Exception as e:
            print(e)


def main():
    lock = threading.Lock()
    orderBooks = {
        BTC_SYMBOL: {},
        ETH_SYMBOL: {},
        "last_update": None
    }
    btcUrl = u.WEB_SOCKET_URL + "/marketdata/" + BTC_SYMBOL + "?top_of_book=true"
    btc = c.Client(btcUrl, BTC_SYMBOL,
                   orderBook=orderBooks, lock=lock)
    ethUrl = u.WEB_SOCKET_URL + "/marketdata/" + ETH_SYMBOL + "?top_of_book=true"
    eth = c.Client(ethUrl, ETH_SYMBOL,
                   orderBook=orderBooks, lock=lock)
    btc.start()
    eth.start()
    process(orderBooks, lock)


main()
