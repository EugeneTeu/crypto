

class TickerInfo:
        
    def __init__(self, tickerInfo):
        self.price = tickerInfo['price']
        self.time = tickerInfo['time']

    def getPrice(self):
        return float(self.price)
    