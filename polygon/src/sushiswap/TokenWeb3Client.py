import os
import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.base.Web3Client import Web3Client


class TokenWeb3Client(PolygonWeb3Client):

    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/erc20_abi.json")

    def __init__(self, tokenAddress: str):
        self.contractAddress = cast(Address, tokenAddress)
        super().__init__()

    def getTokenInfo(self) -> dict[str, str]:
        symbol = self.contract.functions.symbol().call()
        decimals = self.contract.functions.decimals().call()
        return {"symbol": symbol, "decimals": decimals}

    def getBalance(self) -> int:
        return self.contract.functions.balanceOf(self.userAddress).call()
