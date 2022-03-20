
from lib2to3.pgen2 import token
from os import getenv
import os
from platform import node
from typing import cast

import dotenv
from src.RaiderAurumStakingWeb3Client import RaiderAurumStakingWeb3Client
from src.UnicornNFTWeb3Client import UnicornNFTWeb3Client
from src.DarkForestWeb3Client import DarkForestWeb3Client
from src.RaiderNewtQuestWeb3Client import RaiderNewtQuestWeb3Client
from src.RaiderGrimweedQuestWeb3Client import RaiderGrimweedQuestWeb3Client

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
