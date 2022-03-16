'''
usage: python3 -m raider.getGrimweedRewards

'''

from src.logger.txLogger import logTx
from src.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import grimweedClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status = grimweedClient.getRaiderStatus(raiderId)
    if status == 2:
        timeTillHome = grimweedClient.timeTillHome(raiderId)
        if timeTillHome < 0:
            txHash = grimweedClient.getRewards(raiderId)
            txLogger.info(txHash)
            txReceipt = grimweedClient.getTransactionReceipt(txHash)
            logTx(txReceipt)
        else:
            txLogger.info("%s still need %ss to get home!",
                          str(raiderId), str(timeTillHome))
