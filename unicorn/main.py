
from os import getenv
import os
from typing import cast

import dotenv
from src.UnicornWeb3Client import UnicornWeb3Client

if not os.path.isfile(".env"):
    raise Exception(".env file not found")
dotenv.load_dotenv()

# RPC
nodeUri = getenv("WEB3_NODE_URI")

# Gas
defaultGas = getenv("DEFAULT_GAS", "200000")  # units
defaultGasPrice = getenv("DEFAULT_GAS_PRICE", "30")  # gwei
key = getenv("PRIVATE_KEY")

print(nodeUri)

client = cast(UnicornWeb3Client, (UnicornWeb3Client().setNodeUri(
    nodeUri).setCredentials(key)))
print(client.getUnicornStatus())
