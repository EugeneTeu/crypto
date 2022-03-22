import time
from typing import cast
import json
from eth_account import Account
from eth_typing import Address, ChecksumAddress
from web3.types import TxParams
from web3.exceptions import ContractLogicError

from eth_typing.encoding import HexStr
import os

from src.base.Web3Client import Web3Client
from src.constants.constants import SUSHISWAP_ROUTER_CONTRACT
from src.base.PolygonWeb3Client import PolygonWeb3Client


class SushiSwapRouterWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, SUSHISWAP_ROUTER_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/router_abi.json")

    def getAmountsOut(self, amtIn: int,  path: list[str]) -> list[int]:
        return self.contract.functions.getAmountsOut(amtIn, path).call()

    def swapExactTokensForTokens(self, amtIn: int, amtOutMin: int, path: list[str]) -> int:
        '''
            https://docs.uniswap.org/protocol/V2/reference/smart-contracts/router-02#swapexacttokensfortokens
        '''
        # ensure outgoing address matches current private key
        assert(self.userAddress == Account.from_key(self.privateKey).address)
        assert(len(path) >= 2)
        # deadline is 1  min
        deadline = int(time.time() + (2 * 60))
        try:
            tx = self.buildContractTransaction(self.contract.functions.swapExactTokensForTokens(
                amtIn, amtOutMin, path, self.userAddress, deadline))
            return self.signAndSendTransaction(tx)
        except ContractLogicError as e:
            print(e)
            exit(1)

    def addLiquidity(self, tokenA: str, tokenB: str, amountADesired: int, amountBDesired: int, amountAMin: int, amountBMin: int) -> int:
        assert(self.userAddress == Account.from_key(self.privateKey).address)
        deadline = int(time.time() + (2 * 60))
        try:
            tx = self.buildContractTransaction(self.contract.functions.addLiquidity(
                tokenA, tokenB, amountADesired, amountBDesired, amountAMin, amountBMin, self.userAddress, deadline))
            print(tx)
            return 1
            # return self.signAndSendTransaction(tx)
        except ContractLogicError as e:
            print(e)
            exit(1)
