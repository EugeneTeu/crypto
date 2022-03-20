import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.constants.constants import DARK_FOREST_CONTRACT
from src.base.Web3Client import Web3Client


class DarkForestWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, DARK_FOREST_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/unicorn_abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/dark_forest_abi.json")

    def getNumberOfUnicornStaked(self) -> int:
        numStaked = self.contract.functions.numStaked(self.userAddress).call()
        return numStaked

    def getTokenOfStakerByIndex(self, i) -> int:
        tokenId = self.contract.functions.tokenOfStakerByIndex(
            self.userAddress, i).call()
        return tokenId

    def canUnstake(self, tokenId) -> bool:
        unstakedAt = self.contract.functions.unstakesAt(tokenId).call()
        currentTime = time.time()
        return currentTime > unstakedAt

    def getUnicornStatus(self) -> list:
        result = []
        numStaked = self.getNumberOfUnicornStaked()
        for i in range(numStaked):
            tokenId = self.getTokenOfStakerByIndex(i)
            canUnstake = self.canUnstake(tokenId)
            result.append({
                "tokenId": tokenId,
                "canUnstake": canUnstake
            })
        return result

    def unStakeUnicorns(self, tokenId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.exitForest(tokenId))
        return self.signAndSendTransaction(tx)

    def stakeUnicorns(self, tokenId) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.exitForest(tokenId))
        return self.signAndSendTransaction(tx)
