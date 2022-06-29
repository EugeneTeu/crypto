import decimal
import time
from typing import Dict, Union, cast
import json
from eth_typing import Address
from web3 import Web3
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.constants.constants import STAKED_RBW_CONTRACT
from src.base.Web3Client import Web3Client


class StakedRbwWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, STAKED_RBW_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/unicorn_abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/staked_rbw_abi.json")

    def withdrawableRewards(self, address: Address) -> int:
        val = self.contract.functions.withdrawableRewardsOf(address).call()
        return cast(int, Web3.fromWei(val, "ether"))

    def claimRewards(self, address: Address) -> int:
        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.claimRewards(address))
        return self.signAndSendTransaction(tx)
