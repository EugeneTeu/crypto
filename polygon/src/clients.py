
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
from src.unicorn.StakedRbwWeb3Client import StakedRbwWeb3Client

from src.raider.RaiderNewtQuestWeb3Client import RaiderNewtQuestWeb3Client
from src.raider.RaiderGrimweedQuestWeb3Client import RaiderGrimweedQuestWeb3Client

from src.sushiswap.SushiSwapRouterWeb3Client import SushiSwapRouterWeb3Client
from src.constants.constants import AURUM_USDC_SLP_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, AURUM_TOKEN_CONTRACT
from src.sushiswap.TokenWeb3Client import TokenWeb3Client
from src.sushiswap.UniswapV2PairWeb3Client import UniswapV2PairWeb3Client

if not os.path.isfile(".env"):
    raise Exception(".env file not found")
dotenv.load_dotenv()


# ==============================================================================
# Unicorn clients
# ==============================================================================
stakedRbwClient = cast(StakedRbwWeb3Client, (StakedRbwWeb3Client()))

# ==============================================================================
# RAIDER CLIENTS
# ==============================================================================
grimweedClient = cast(RaiderGrimweedQuestWeb3Client,
                      (RaiderGrimweedQuestWeb3Client()))

newtClient = cast(RaiderNewtQuestWeb3Client, (RaiderNewtQuestWeb3Client()))

aurumStakingClient = cast(RaiderAurumStakingWeb3Client, RaiderAurumStakingWeb3Client(
))


# ==============================================================================
# Sushiswap client
# ==============================================================================

sushiswapRouterClient = cast(SushiSwapRouterWeb3Client, SushiSwapRouterWeb3Client(
))


# ==============================================================================
# Token Clients
# ==============================================================================

def getTokenClient(address: str) -> TokenWeb3Client:
    return cast(TokenWeb3Client, TokenWeb3Client(address
                                                 ))


usdcTokenClient = getTokenClient(USDC_TOKEN_CONTRACT)
aurumTokenClient = getTokenClient(AURUM_TOKEN_CONTRACT)


raiderUsdcSLPTokenClient = cast(
    UniswapV2PairWeb3Client, UniswapV2PairWeb3Client(AURUM_USDC_SLP_TOKEN_CONTRACT))


def getUniswapV2Client(address: str) -> UniswapV2PairWeb3Client:
    return cast(UniswapV2PairWeb3Client, UniswapV2PairWeb3Client(address))
