
import os
import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from src.AvalancheCWeb3Client import AvalancheCWeb3Client
from src.Web3Client import Web3Client


class JoeLcWeb3Client(AvalancheCWeb3Client):

    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/joepool_abi.json")

    def __init__(self, liquidityContractAddr):
        self.contractAddress = cast(Address, liquidityContractAddr)

    def getReserves(self):
        return self.contract.functions.getReserves().call()

    def getToken0(self):
        return self.contract.functions.token0().call()

    def getToken1(self):
        return self.contract.functions.token1().call()
