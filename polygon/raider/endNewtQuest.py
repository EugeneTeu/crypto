'''
usage: python3 -m raider.endGrimweedQuest

'''
from src.logger.txLogger import logTx
from src.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import newtClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status = newtClient.getRaiderStatus(raiderId)
    if status == 1:
        txHash = newtClient.endQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = newtClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
