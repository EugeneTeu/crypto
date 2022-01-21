import threading
import util.client as c
import util.gemini as u
import time
from datetime import datetime

BTC_SYMBOL = "BTCUSD"
ETH_SYMBOL = "ETHUSD"
CRV_SYMBOL = "CRVUSD"
ANKR_SYMBOL = "ANKRUSD"
YFI_SYMBOL = "YFIUSD"

symbols = [BTC_SYMBOL, ETH_SYMBOL, CRV_SYMBOL]


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


def getClient(symbol, orderBooks, lock):
    url = u.WEB_SOCKET_URL + "/marketdata/" + symbol + "?top_of_book=true"
    client = c.Client(url, symbol,
                      orderBook=orderBooks, lock=lock)
    return client


def main():
    lock = threading.Lock()
    orderBooks = {}
    for symbol in symbols:
        orderBooks[symbol] = {}
    orderBooks["last_update"] = None
    for key, value in orderBooks.items():
        if key != 'last_update':
            client = getClient(key, orderBooks, lock)
            client.start()
    # orderBooks = {
    #     BTC_SYMBOL: {},
    #     ETH_SYMBOL: {},
    #     CRV_SYMBOL: {},
    #     "last_update": None
    # }
    # btc = getClient(BTC_SYMBOL, orderBooks, lock)
    # eth = getClient(ETH_SYMBOL, orderBooks, lock)
    # crv = getClient(CRV_SYMBOL, orderBooks, lock)
    # btc.start()
    # eth.start()
    # crv.start()
    process(orderBooks, lock)


main()
