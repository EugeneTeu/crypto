import time
from typing import Tuple, cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os
from src.logger.txLogger import logTx, txLogger
from src.logger.logger import logger
from src.helper.format import convertFromWei, convertToWei
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

    def getUserPendingRewards(self) -> Raider:
        return self.contract.functions.userPendingRewards(self.userAddress).call()

    def claimUserRewards(self) -> Tuple[int, HexStr]:
        currentRewards = self.getUserPendingRewards()
        txLogger.info("current Aurum-USDC Rewards: %f RAIDERS",
                      convertFromWei(currentRewards))
        if currentRewards > convertToWei(2.0):
            # if greater than 3 raider we claim
            tx: TxParams = self.buildContractTransaction(
                self.contract.functions.getRewards())
            return (currentRewards, self.signAndSendTransaction(tx))
        else:
            txLogger.error("Raider rewards is currently below claim threshold")
            exit(1)

    def depositSLP(self, amt: int) -> HexStr:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.createStake(amt)
        )
        return self.signAndSendTransaction(tx)
