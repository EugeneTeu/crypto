'''
usage: python3 -m raider.endNewtQuest

'''
from src.logger.txLogger import logTx
from src.constants.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import newtClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = newtClient.getRaiderStatus(raiderId)
    if status1 == 1:
        txHash = newtClient.endQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = newtClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
