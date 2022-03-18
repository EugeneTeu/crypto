
import os
import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from src.AvalancheCWeb3Client import AvalancheCWeb3Client
from src.Web3Client import Web3Client


class JoeLcWeb3Client(AvalancheCWeb3Client):

    def __init__(self, liquidityContractAddr, abiFilePath):
        self.contractAddress = cast(Address, liquidityContractAddr)
        self.abi = Web3Client.getContractAbiFromFile(
            os.path.dirname(os.path.realpath(__file__)) + abiFilePath)

    def test(self):
        val = self.contract.functions.getReserves().call()
        return val
