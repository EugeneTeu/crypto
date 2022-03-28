'''
usage: python3 -m raider.getGrimweedRewards

'''

from src.logger.txLogger import logTx, txLogger
from src.constants.constants import RAIDER_IDS
from src.clients import grimweedClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status1 = grimweedClient.getRaiderStatus(raiderId)
    if status1 == 2:
        timeTillHome = grimweedClient.timeTillHome(raiderId)
        if timeTillHome <= 0:
            txHash = grimweedClient.getRewards(raiderId)
            txLogger.info(txHash)
            txReceipt = grimweedClient.getTransactionReceipt(txHash)
            logTx(txReceipt)
            if txReceipt["status"] != 1:
                txLogger.error(
                    f"Error getting grimweed rewards for {raiderId}")
        else:
            txLogger.info("%s still need %ss to get home!",
                          str(raiderId), str(timeTillHome))
