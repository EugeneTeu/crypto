from typing import cast, NewType
from web3 import Web3
from web3.types import Wei
from src.logger.logger import logger
from src.logger.txLogger import logTx, txLogger
from src.clients import aurumStakingClient

txHash = aurumStakingClient.getUserRewards()
txLogger.info(txHash)
txReceipt = aurumStakingClient.getTransactionReceipt(txHash)
logTx(txReceipt)
if txReceipt["status"] != 1:
    txLogger.error(f"error claiming rewards from LP")
