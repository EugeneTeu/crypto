from typing import cast, NewType
from web3 import Web3
from web3.types import Wei
from src.logger import txLogger, logger
from src.logger.txLogger import logTx
from src.clients import aurumStakingClient

txHash = aurumStakingClient.getUserRewards()
txLogger.info(txHash)
txReceipt = aurumStakingClient.getTransactionReceipt(txHash)
logTx(txReceipt)
if txReceipt["status"] != 1:
    logger.error(f"error claiming rewards from LP")
