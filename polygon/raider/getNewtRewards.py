'''
usage: python3 -m raider.getGrimweedRewards

'''

from src.logger.txLogger import logTx
from src.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import newtClient
for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = newtClient.getRaiderStatus(raiderId)
    if status1 == 2:
        timeTillHome = newtClient.timeTillHome(raiderId)
        if timeTillHome <= 0:
            txHash = newtClient.getRewards(raiderId)
            txLogger.info(txHash)
            txReceipt = newtClient.getTransactionReceipt(txHash)
            logTx(txReceipt)
        else:
            txLogger.info("%s still need %ss to get home!",
                          str(raiderId), str(timeTillHome))
