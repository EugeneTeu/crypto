
from lib2to3.pgen2 import token
from os import getenv
import os
from platform import node
from tokenize import Token
from typing import cast

import dotenv
from src.raider.RaiderAurumStakingWeb3Client import RaiderAurumStakingWeb3Client
from src.unicorn.UnicornNFTWeb3Client import UnicornNFTWeb3Client
from src.unicorn.DarkForestWeb3Client import DarkForestWeb3Client
from src.raider.RaiderNewtQuestWeb3Client import RaiderNewtQuestWeb3Client
from src.raider.RaiderGrimweedQuestWeb3Client import RaiderGrimweedQuestWeb3Client

from src.sushiswap.SushiSwapRouterWeb3Client import SushiSwapRouterWeb3Client
from src.constants.constants import USDC_TOKEN_CONTRACT, AURUM_TOKEN_CONTRACT
from src.sushiswap.TokenWeb3Client import TokenWeb3Client

if not os.path.isfile(".env"):
    raise Exception(".env file not found")
dotenv.load_dotenv()

# RPC
nodeUri = getenv("WEB3_NODE_URI")
key = getenv("PRIVATE_KEY")

# ==============================================================================
# RAIDER CLIENTS
# ==============================================================================
grimweedClient = cast(RaiderGrimweedQuestWeb3Client, (RaiderGrimweedQuestWeb3Client().setNodeUri(
    nodeUri).setCredentials(key)))

newtClient = cast(RaiderNewtQuestWeb3Client, (RaiderNewtQuestWeb3Client().setNodeUri(
    nodeUri).setCredentials(key)))

aurumStakingClient = cast(RaiderAurumStakingWeb3Client, RaiderAurumStakingWeb3Client(
).setNodeUri(nodeUri).setCredentials(key))

# ==============================================================================
# UNICORN CLIENTS
# ==============================================================================

darkForestClient = cast(DarkForestWeb3Client, DarkForestWeb3Client(
).setNodeUri(nodeUri).setCredentials(key))

unicornNFTClient = cast(UnicornNFTWeb3Client, UnicornNFTWeb3Client(
).setNodeUri(nodeUri).setCredentials(key))

# ==============================================================================
# Sushiswap client
# ==============================================================================

sushiswapRouterClient = cast(SushiSwapRouterWeb3Client, SushiSwapRouterWeb3Client(
).setNodeUri(nodeUri).setCredentials(key))


# ==============================================================================
# Token Clients
# ==============================================================================

def getTokenClient(address: str) -> TokenWeb3Client:
    return cast(TokenWeb3Client, TokenWeb3Client(address
                                                 ).setNodeUri(nodeUri).setCredentials(key))


usdcTokenClient = getTokenClient(USDC_TOKEN_CONTRACT)
aurumTokenClient = getTokenClient(AURUM_TOKEN_CONTRACT)
