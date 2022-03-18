
from lib2to3.pgen2 import token
from os import getenv
import os
from typing import cast

import dotenv
from src.constants import TUS_LP_CONTRACT, USDC_LP_CONTRACT

from src.traderJoeClient.JoeLcWebc3Client import JoeLcWeb3Client
from src.token.TokenWeb3Client import TokenWeb3Client


if not os.path.isfile(".env"):
    raise Exception(".env file not found")
dotenv.load_dotenv()

# RPC
nodeUri = getenv("WEB3_NODE_URI")
key = getenv("PRIVATE_KEY")


# ==============================================================================
# Init client
# ==============================================================================

UsdcWavaxLpClient = cast(JoeLcWeb3Client, JoeLcWeb3Client(
    USDC_LP_CONTRACT).setNodeUri(nodeUri))

TusWavaxLpCLient = cast(JoeLcWeb3Client, JoeLcWeb3Client(
    TUS_LP_CONTRACT).setNodeUri(nodeUri))


def getTokenClient(contractAddress):
    return cast(TokenWeb3Client, TokenWeb3Client(contractAddress).setNodeUri(nodeUri))
