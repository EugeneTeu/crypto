

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

RAIDER_IDS = json.loads(os.getenv("RAIDERS_IDS"))
