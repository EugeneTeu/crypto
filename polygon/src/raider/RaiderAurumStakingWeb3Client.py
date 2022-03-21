import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os
from src.logger import logTx, txLogger, logger
from src.helper.format import convertReadable
from src.helper.types import Raider

from src.constants.constants import AURUM_STAKING_CONTRACT
from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.base.Web3Client import Web3Client


class RaiderAurumStakingWeb3Client(PolygonWeb3Client):
    contractAddress = cast(
        Address, AURUM_STAKING_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/raider_abi"
    abi = Web3Client.getContractAbiFromFile(
        abiDir + "/aurum_staking_abi.json")

    def _getUserPendingRewards(self) -> Raider:
        return convertReadable(self.contract.functions.userPendingRewards(self.userAddress).call())

    def getUserRewards(self) -> HexStr:
        currentRewards = self._getUserPendingRewards()
        txLogger.info("current Aurum-USDC Rewards: %f RAIDERS", currentRewards)
        if currentRewards > 3.0:
            # if greater than 3 raider we claim
            tx: TxParams = self.buildContractTransaction(
                self.contract.functions.getRewards())
            return self.signAndSendTransaction(tx)
        else:
            txLogger.error("Raider rewards is currently below claim threshold")
            exit(1)
