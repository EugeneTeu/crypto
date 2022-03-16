from __future__ import annotations
from src.Web3Client import Web3Client
from web3.middleware import geth_poa_middleware


class PolygonWeb3Client(Web3Client):
    """
    Client to interact with the Avalanche blockchain and
    its smart contracts.
    """

    chainId: int = 137
    gasLimit: int = 400000  # sensible value for polygon
    maxPriorityFeePerGasInGwei: int = 40

    def setNodeUri(self, nodeUri: str = None) -> PolygonWeb3Client:
        """
        Inject the POA middleware
        """
        super().setNodeUri(nodeUri)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return self
