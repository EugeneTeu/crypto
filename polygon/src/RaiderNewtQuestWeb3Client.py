import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os

from src.PolygonWeb3Client import PolygonWeb3Client
from src.constants import NEWT_CONTRACT
from src.Web3Client import Web3Client


class RaiderNewtQuestWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, NEWT_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/raider_abi"
    abi = Web3Client.getContractAbiFromFile(
        abiDir + "/grimweed_quest_abi.json")

    def getRewards(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.getRewards(raiderId))
        print(tx)
        return self.signAndSendTransaction(tx)

    def endQuest(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.endQuest(raiderId))
        return self.signAndSendTransaction(tx)
