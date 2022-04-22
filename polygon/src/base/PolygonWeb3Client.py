from __future__ import annotations
from src.base.Web3Client import Web3Client
from web3.middleware import geth_poa_middleware
import dotenv
from os import getenv
import os


class PolygonWeb3Client(Web3Client):
    """
    Client to interact with the Polygon blockchain and
    its smart contracts.
    """

    chainId: int = 137
    gasLimit: int = 400000  # sensible value for polygon
    maxPriorityFeePerGasInGwei: int = 40

    def __init__(self) -> None:
        super().__init__()
        if not os.path.isfile(".env"):
            raise Exception(".env file not found")
        dotenv.load_dotenv()

        # RPC
        nodeUri = getenv("WEB3_NODE_URI")
        key = getenv("PRIVATE_KEY")
        self.setNodeUri(nodeUri)
        self.setCredentials(key)

    def setNodeUri(self, nodeUri: str = None) -> PolygonWeb3Client:
        """
        Inject the POA middleware
        """
        super().setNodeUri(nodeUri)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return self
