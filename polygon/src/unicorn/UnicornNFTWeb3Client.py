import time
from typing import cast
import json
from eth_typing import Address
from web3 import Web3
from web3.types import TxParams

from eth_typing.encoding import HexStr
import os

from src.base.PolygonWeb3Client import PolygonWeb3Client
from src.constants.constants import UNICORN_NFT_CONTRACT, DARK_FOREST_CONTRACT
from src.base.Web3Client import Web3Client


class UnicornNFTWeb3Client(PolygonWeb3Client):

    contractAddress = cast(
        Address, UNICORN_NFT_CONTRACT)
    abiDir = os.path.dirname(os.path.realpath(__file__)) + "/unicorn_abi"
    abi = Web3Client.getContractAbiFromFile(abiDir + "/erc721_abi.json")

    def getNumberOfUnicorn(self) -> int:
        num = self.contract.functions.balanceOf(self.userAddress).call()
        return num

    def getTokenOfOwnerByIndex(self, i) -> int:
        tokenId = self.contract.functions.tokenOfOwnerByIndex(
            self.userAddress, i).call()
        return tokenId

    def canUnstake(self, tokenId) -> bool:
        unstakedAt = self.contract.functions.unstakesAt(tokenId).call()
        currentTime = time.time()
        return currentTime > unstakedAt

    def getUnicornStatus(self) -> list:
        result = []
        numStaked = self.getNumberOfUnicorn()
        for i in range(numStaked):
            tokenId = self.getTokenOfOwnerByIndex(i)
            result.append({
                "tokenId": tokenId
            })
        return result

    def stakeUnicorns(self, darkForestAddress, tokenId) -> int:
        assert str(darkForestAddress) == Web3.toChecksumAddress(
            DARK_FOREST_CONTRACT)

        tx: TxParams = self.buildContractTransaction(
            self.contract.functions.safeTransferFrom(self.userAddress, darkForestAddress, tokenId))
        # return tx
        return self.signAndSendTransaction(tx)
