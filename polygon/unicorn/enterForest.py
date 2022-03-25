'''
usage: python3 -m unicorn.enterForest 

'''

from web3 import Web3
from src.unicorn.DarkForestWeb3Client import DarkForestWeb3Client

from src.clients import unicornNFTClient
from src.logger.txLogger import txLogger, logTx

# darkForestContractAddress = Web3.toChecksumAddress(
#     DarkForestWeb3Client.contractAddress)
# unicorns = unicornNFTClient.getUnicornStatus()
# if not unicorns:
#     txLogger.info("No unicorns found. are they in the dark forest?")
#     exit(1)

# for uni in unicorns:
#     tokenId = uni['tokenId']
#     txHash = unicornNFTClient.stakeUnicorns(darkForestContractAddress, tokenId)
#     txLogger.info(txHash)
#     txReceipt = unicornNFTClient.getTransactionReceipt(txHash)
#     logTx(txReceipt)
