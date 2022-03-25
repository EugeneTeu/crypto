'''
usage: python3 -m unicorn.exitForest 

'''

from src.clients import darkForestClient
from src.logger.txLogger import txLogger, logTx

# unicorns = darkForestClient.getUnicornStatus()

# for uni in unicorns:
#     tokenId = uni['tokenId']
#     canUnstake = uni["canUnstake"]
#     if canUnstake == True:
#         txHash = darkForestClient.unStakeUnicorns(tokenId)
#         txLogger.info(txHash)
#         txReceipt = darkForestClient.getTransactionReceipt(txHash)
#         logTx(txReceipt)
#     else:
#         txLogger.info(str(tokenId) + " cannot unstake right now")
