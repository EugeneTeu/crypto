'''
usage: python3 -m raider.endGrimweedQuest

'''
from src.logger.txLogger import logTx
from src.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import grimweedClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status = grimweedClient.getRaiderStatus(raiderId)
    if status == 1:
        txHash = grimweedClient.endQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = grimweedClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
