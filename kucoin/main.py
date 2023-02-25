import asyncio
import json
import pprint
import os

from kucoin.client import WsToken, Market
from kucoin.ws_client import KucoinWsClient
from MarketDataLevel2Type import Level2MarketDataMsg, Changes, Data

from dotenv import load_dotenv

load_dotenv()
from UtilLogic import UtilLogic
from tabulate import tabulate

BASE_URL = "https://api.kucoin.com"
API_KEY = os.environ["key"]
API_SECRET = os.environ["secret"]
PASS_PHRASE = os.environ["pass_phrase"]

REST_CLIENT = Market(
    key=API_KEY, secret=API_SECRET, passphrase=PASS_PHRASE, url=BASE_URL
)

# REST
ETH_USDT_SYMBOL = "ETH-USDT"

# websocket
ETH_KLINE_THREE_MIN = "/market/candles:ETH-USDT_3min"
ETH_MARKET_DATA = "/market/level2:ETH-USDT"
ETH_MARKET_DATA_FILE_NAME = "market-ETH-USDT"

# websocket data
current_data: list[Data] = []
current_seq_num = -1


async def main():
    def isETHMarketDataMessage(msg):
        return msg["topic"] == ETH_MARKET_DATA

    def updateAsksAndBids(msg: Level2MarketDataMsg):
        current_data.extend([msg.data])

    def printData(asks: list[str], bids: list[str]):
        print("Asks:\n")
        print(
            tabulate(
                asks,
                [
                    "price",
                    "size",
                ],
                tablefmt="grid",
            )
        )
        print("Bids:\n")
        print(
            tabulate(
                bids,
                [
                    "price",
                    "size",
                ],
                tablefmt="grid",
            )
        )

    async def dealMsg(msg):
        if isETHMarketDataMessage(msg):
            parsed_msg = Level2MarketDataMsg.from_dict(msg)
            updateAsksAndBids(parsed_msg)
            # UtilLogic.streamToFile(ETH_MARKET_DATA_FILE_NAME, msg)

    # MAIN DRIVER
    # is public
    client = WsToken()
    # is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, dealMsg, private=False)
    # await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    # await ws_client.subscribe('/spotMarket/level2Depth5:ETH-USDT,MATIC-USDT')
    # await ws_client.subscribe(ETH_MARKET_DATA)
    while True:
        # step 1
        # local snapshot
        orderBookData = REST_CLIENT.get_aggregated_orderv3(ETH_USDT_SYMBOL)
        current_seq_num = float(orderBookData["sequence"])
        order_book_asks = orderBookData["asks"]
        order_book_bids = orderBookData["bids"]

        # step 2
        # update order book

        # step 3 working order book

        # print(current_seq_num)
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
