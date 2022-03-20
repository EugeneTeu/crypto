import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.constants.constants import NEWT_CONTRACT
from src.base.Web3Client import Web3Client


class RaiderNewtQuestWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, NEWT_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/raider_abi"
    abi = Web3Client.getContractAbiFromFile(
        abiDir + "/grimweed_quest_abi.json")

    def getRewards(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.getRewards(raiderId))
        return self.signAndSendTransaction(tx)

    def endQuest(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.endQuest(raiderId))
        return self.signAndSendTransaction(tx)

    def calcReturnTime(self, raiderId) -> int:
        time = self.contract.functions.calcReturnTime(raiderId).call()
        return time

    def calcRaiderRewardTime(self, raiderId) -> int:
        time = self.contract.functions.calcRaiderRewardTime(raiderId).call()
        return time

    def raiderStartQuest(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.startQuest(raiderId))
        return self.signAndSendTransaction(tx)

    def raiderEndQuest(self, raiderId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.endQuest(raiderId))
        return self.signAndSendTransaction(tx)

    def timeTillHome(self, raiderId) -> int:
        try:
            time = self.contract.functions.timeTillHome(raiderId).call()
            return time
        except:
            return 0

    def getRaiderStatus(self, raiderId) -> int:
        '''
            returns an int for each raider
            0 -> not on this quest
            1 -> on quest
            2 -> quest ended waiting for cooldown

            enum Status {
                None,
                Questing,
                Returning
            } 
        '''
        status = self.contract.functions.raiderStatus(raiderId).call()
        return status
