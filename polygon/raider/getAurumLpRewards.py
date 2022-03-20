from typing import cast, NewType
from web3 import Web3
from web3.types import Wei
from src.logger.txLogger import logTx
from src.clients import aurumStakingClient
from src.logger.txLogger import txLogger

txHash = aurumStakingClient.getUserRewards()
txLogger.info(txHash)
txReceipt = aurumStakingClient.getTransactionReceipt(txHash)
logTx(txReceipt)
