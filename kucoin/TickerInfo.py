

from typing import Any


class TickerInfo:
    tickerName = ''
    price = 0.0
    time = 0
    bestAsk = 0.0
    bestBid = 0.0

    def __init__(self, tickerName, tickerInfo: Any):
        self.ticker_name = tickerName
        if tickerInfo is not None:
            self.price = float(tickerInfo['price'])
            self.time = int(tickerInfo['time'])
            self.bestAsk = float(tickerInfo['bestAsk'])
            self.bestBid = float(tickerInfo['bestBid'])

    def getPrice(self):
        if self.price is None:
            return 0.0
        return self.price

