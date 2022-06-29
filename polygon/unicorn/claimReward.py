'''
usage: python3 -m unicorn.claimReward

'''

from audioop import add
from src.clients import stakedRbwClient
from web3 import Web3
from src.logger.txLogger import logTx, txLogger

addr = Web3.toChecksumAddress("0xdaaed1035319299174299d066b41a9a63d87e805")
lockedRewards = stakedRbwClient.withdrawableRewards(addr)

if lockedRewards > 5:
    # unlock
    txHash = stakedRbwClient.claimRewards(addr)
    txLogger.info(txHash)
    txReceipt = stakedRbwClient.getTransactionReceipt(txHash)
    logTx(txReceipt)
