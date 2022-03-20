import os
import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from src.PolygonWeb3Client import PolygonWeb3Client
from src.Web3Client import Web3Client


class TokenWeb3Client(PolygonWeb3Client):

    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/erc20_abi.json")

    def __init__(self, tokenAddress):
        self.contractAddress = cast(Address, tokenAddress)

    def getTokenInfo(self) -> dict[str, str]:
        symbol = self.contract.functions.symbol().call()
        decimals = self.contract.functions.decimals().call()
        return {"symbol": symbol, "decimals": decimals}
