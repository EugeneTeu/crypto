import asyncio
import json
import pprint
import os
from typing import List, Tuple
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

    def printLocalOrderbook(asks: dict, bids: dict):
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

    # asks: List[str]  # price, size , sequence
    def processAskAndBids(
        current_seq: float, asks: List[str]
    ) -> list[Tuple[float, float, float]]:
        remaining = []
        for ask in asks:
            ask_seq = ask[2]
            if ask_seq > current_seq:
                price = float(ask[0])
                size = float(ask[1])
                seq = float(ask[2])
                val = [price, size, seq]
                remaining.append(val)
        return remaining

    def updatePriceAndSizes(
        process_asks: list[Tuple[float, float, float]], asks: dict, asks_seq: dict
    ) -> list[dict]:
        for ask in process_asks:
            curr_price = ask[0]
            curr_size = ask[1]
            curr_seq = ask[2]
            if curr_price not in asks:
                asks[curr_price] = curr_size
                asks_seq[curr_price] = curr_seq
            elif curr_price in asks:
                if asks_seq[curr_price] <= curr_seq:
                    if curr_size == 0:
                        # delete
                        asks.pop(curr_price)
                        asks_seq.pop(curr_price)
                    else:
                        asks[curr_price] = curr_size
                        asks_seq[curr_price] = curr_seq
        return [asks, asks_seq]

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

    # price to sizes
    asks = {}
    # price to seq
    asks_seq = {}

    bids = {}
    bids_seq = {}

    while True:
        # step 1
        # local snapshot
        # orderBookData = REST_CLIENT.get_aggregated_orderv3(ETH_USDT_SYMBOL)
        orderBookData = REST_CLIENT.get_part_order(20, ETH_USDT_SYMBOL)
        order_book_asks = orderBookData["asks"]
        order_book_bids = orderBookData["bids"]
        seq = float(orderBookData["sequence"])

        # print(current_seq_num)
        # printData(order_book_asks, order_book_bids)

        for ask in order_book_asks:
            price = float(ask[0])
            size = float(ask[1])
            asks[price] = size
            asks_seq[price] = seq

        for bid in order_book_bids:
            price = float(bid[0])
            size = float(bid[1])
            bids[price] = size
            bids_seq[price] = seq

        # step 2
        # update order book
        for data in current_data:
            seq_start = data.sequenceStart
            seq_end = data.sequenceEnd
            if seq_end <= seq:
                data_asks = data.changes.asks
                data_bids = data.changes.bids
                # list of price to size
                processed_asks = processAskAndBids(seq, data_asks)
                processed_bids = processAskAndBids(seq, data_bids)
                result = updatePriceAndSizes(
                    process_asks=processed_asks, asks=asks, asks_seq=asks_seq
                )
                asks = result[0]
                asks_seq = result[1]

                result_bids = updatePriceAndSizes(
                    process_asks=processed_bids, asks=bids, asks_seq=bids_seq
                )
                bids = result_bids[0]
                bids_seq = result_bids[1]

        # step 3 working order book
        print(asks)
        print(bids)
        # print(current_seq_num)
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
