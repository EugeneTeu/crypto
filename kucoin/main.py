import asyncio
import pprint
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient



ETH_KLINE_THREE_MIN='/market/candles:ETH-USDT_3min' 

async def main():
    
    async def deal_msg(msg):
        if msg['topic'] == '/spotMarket/level2Depth5:MATIC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotmarket/level2Depth5:ETH-USDT':
            print(msg['data'])
        elif msg['topic'] == ETH_KLINE_THREE_MIN:
            pprint.pprint(msg['data']) 
    
    # MAIN DRIVER

    # is public
    client = WsToken()
    #is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    # await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    # await ws_client.subscribe('/spotMarket/level2Depth5:ETH-USDT,MATIC-USDT')
    await ws_client.subscribe(ETH_KLINE_THREE_MIN)
    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
        asyncio.run(main())