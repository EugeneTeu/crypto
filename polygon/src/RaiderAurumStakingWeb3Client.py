import time
from typing import cast
import json
from eth_typing import Address
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os
from src.helper.types import Raider

from src.constants import AURUM_STAKING_CONTRACT
from src.PolygonWeb3Client import PolygonWeb3Client
from src.Web3Client import Web3Client


class RaiderAurumStakingWeb3Client(PolygonWeb3Client):
    contractAddress = cast(
        Address, AURUM_STAKING_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/raider_abi"
    abi = Web3Client.getContractAbiFromFile(
        abiDir + "/aurum_staking_abi.json")

    def userPendingRewards(self) -> Raider:
        return self.contract.functions.userPendingRewards(self.userAddress).call()
