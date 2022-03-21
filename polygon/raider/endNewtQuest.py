'''
usage: python3 -m raider.endNewtQuest

'''
from src.logger import logTx, txLogger, logger
from src.constants.constants import RAIDER_IDS
from src.clients import newtClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = newtClient.getRaiderStatus(raiderId)
    if status1 == 1:
        txHash = newtClient.endQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = newtClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
