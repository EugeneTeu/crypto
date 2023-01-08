import json
import sys
import os
import pprint 
import time
from dotenv import load_dotenv
import signal
from UtilLogic import UtilLogic

from TickerInfo import TickerInfo
load_dotenv()

from kucoin.client import Market


BASE_URL = "https://api.kucoin.com"
API_KEY = os.environ["key"]
API_SECRET = os.environ["secret"]
PASS_PHRASE = os.environ["pass_phrase"]

if len(sys.argv) != 2:
    pprint.pprint('wrong number of args')
    sys.exit()

TICKER = sys.argv[1]

client = Market(url=BASE_URL)

server_time = client.get_server_timestamp()

class Runner(object):
    def __init__(self, tickerName: str, info: TickerInfo):
        self.tickerName = tickerName
        self.currentTickerInfo = info
        signal.signal(signal.SIGINT, self.handler)

    
    def handler(self, signum, frame):
        res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
        if res == 'y':
            UtilLogic.saveToFile(TICKER, self.currentTickerInfo)
            exit(1)

    def updateTickerInfo(self, tickerInfo: TickerInfo):
        UtilLogic.measure(self.currentTickerInfo.getPrice(), tickerInfo.getPrice())
        self.currentTickerInfo = tickerInfo
        print(self.currentTickerInfo.price)
    

if __name__ == '__main__':  
    fileInfo = UtilLogic.getInfoFromFile(TICKER)
    information = Runner(TICKER, fileInfo)
    while True:
        ticker_info = TickerInfo(TICKER, client.get_ticker(TICKER))
        information.updateTickerInfo(tickerInfo=ticker_info)
        time.sleep(10); 




    

