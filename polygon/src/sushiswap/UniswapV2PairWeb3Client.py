import os
import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams, TxReceipt, LogReceipt

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.base.Web3Client import Web3Client


class UniswapV2PairWeb3Client(PolygonWeb3Client):

    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/uniswap_v2_pair.json")

    def __init__(self, tokenAddress: str):
        self.contractAddress = cast(Address, tokenAddress)

    def processTransferEvent(self, txReceipt: LogReceipt) -> int:
        logs = self.contract.events.Transfer().processLog(txReceipt)
        if logs["args"]["to"] == self.userAddress:
            valueOfTransfer = logs["args"]["value"]
            return valueOfTransfer
        else:
            return -1
