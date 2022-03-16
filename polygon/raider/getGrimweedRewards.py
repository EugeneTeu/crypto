'''
usage: python3 -m raider.getGrimweedRewards

'''

from src.constants import RAIDER_IDS
from src.logger.txLogger import txLogger
from src.clients import grimweedClient

for id in RAIDER_IDS:
    raiderId = int(id)
    status = grimweedClient.getRaiderStatus(raiderId)
    if status == 2:
        time = grimweedClient.calcRaiderRewardTime(raiderId)
        print(time)
