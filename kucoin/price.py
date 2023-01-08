import json
import sys
import os
import pprint 
import time
from dotenv import load_dotenv
import signal
from PriceLogic import PriceLogic

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

current_price = PriceLogic.getPriceFromFile(TICKER) #TODO: read from redis?


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        data = { TICKER : f'{current_price}'}
        json_data = json.dumps(data, indent=4)
        with open(f"{TICKER}.json", "w") as outfile:
            outfile.write(json_data)
            exit(1)
 
signal.signal(signal.SIGINT, handler)
 
print(f'Starting price is {current_price}')
while True:
    ticker_info = TickerInfo(client.get_ticker(TICKER))
    price = ticker_info.getPrice()
    if current_price == 0:
        current_price = price
    else:
       current_price = PriceLogic.measure(current_price, price)
    print(f'Current price is {current_price}')
    time.sleep(30); 




    

