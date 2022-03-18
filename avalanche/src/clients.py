
from lib2to3.pgen2 import token
from os import getenv
import os
from typing import cast

import dotenv
from src.constants import USDC_CONTRACT

from src.traderJoeClient.JoeLcWebc3Client import JoeLcWeb3Client


if not os.path.isfile(".env"):
    raise Exception(".env file not found")
dotenv.load_dotenv()

# RPC
nodeUri = getenv("WEB3_NODE_URI")
key = getenv("PRIVATE_KEY")


UsdcClient = cast(JoeLcWeb3Client, JoeLcWeb3Client(
    USDC_CONTRACT, "/abi/joepool_abi.json").setNodeUri(nodeUri))
