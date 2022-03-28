

# https://polygonscan.com/address/0x8d528e98a69fe27b11bb02ac264516c4818c3942
import json
import os

import dotenv
dotenv.load_dotenv()

DARK_FOREST_CONTRACT = "0x8d528e98a69fe27b11bb02ac264516c4818c3942"
# https://polygonscan.com/token/0xdc0479cc5bba033b3e7de9f178607150b3abce1f
UNICORN_NFT_CONTRACT = "0xdc0479cc5bba033b3e7de9f178607150b3abce1f"

GRIMWEED_CONTRACT = "0xe193364370F0E2923b41a8d1850F442B45E5ccA7"
NEWT_CONTRACT = "0x98a195e3eC940f590D726557c95786C8EBb0A2D2"

AURUM_STAKING_CONTRACT = "0x3bfC2f02D8d7E09902D203Dff3AD6C0e1a614106"

RAIDER_IDS = json.loads(os.getenv("RAIDERS_IDS", "[]"))

RAIDER_TOKEN_CONTRACT = "0xcd7361ac3307D1C5a46b63086a90742Ff44c63B3"

WMATIC_TOKEN_CONTRACT = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"

AURUM_TOKEN_CONTRACT = "0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23"

SUSHISWAP_ROUTER_CONTRACT = "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"

USDC_TOKEN_CONTRACT = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

AURUM_USDC_SLP_TOKEN_CONTRACT = "0xaBEE7668a96C49D27886D1a8914a54a5F9805041"
