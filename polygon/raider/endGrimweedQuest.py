'''
usage: python3 -m raider.endGrimweedQuest

'''
from src.logger import txLogger, logger
from src.logger.txLogger import logTx
from src.constants.constants import RAIDER_IDS
from src.clients import grimweedClient, newtClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = grimweedClient.getRaiderStatus(raiderId)
    if status1 == 1:
        txHash = grimweedClient.endQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = grimweedClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
