'''
usage: python3 -m raider.startNewtQuest

'''

from src.logger.txLogger import logTx, txLogger
from src.constants.constants import RAIDER_IDS
from src.clients import newtClient, grimweedClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = grimweedClient.getRaiderStatus(raiderId)
    status2 = newtClient.getRaiderStatus(raiderId)
    if status1 == 0 and status2 == 0:
        txHash = newtClient.raiderStartQuest(raiderId)
        txLogger.info(txHash)
        txReceipt = newtClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
