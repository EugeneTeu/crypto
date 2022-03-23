
from src.helper.format import convertFromWei, convertFromWeiUSDC
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT
from sushiswap.swapToken import simulateAmount, swapTxn
from src.clients import aurumStakingClient, sushiswapRouterClient
from raider.getAurumLpRewards import claimAurumLpRewards
from src.logger.txLogger import logTx, txLogger


raiderWmaticAurumPath = [RAIDER_TOKEN_CONTRACT,
                         WMATIC_TOKEN_CONTRACT, AURUM_TOKEN_CONTRACT]
raiderWmaticUsdcPath = [RAIDER_TOKEN_CONTRACT,
                        WMATIC_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT]

# currRewards = aurumStakingClient.getUserPendingRewards()

# amtA = convertFromWei(currRewards / 2)

# raiderToAurum = simulateAmount(amtA, raiderWmaticAurumPath)
# raiderToUsdc = simulateAmount(amtA, raiderWmaticUsdcPath)

# print(f"{convertFromWei(raiderToAurum)}, {convertFromWeiUSDC(raiderToUsdc)}")


def getTxn(txn: str) -> None:
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txn)
    print(txReceipt)


def stakeAndSellRaider() -> None:
    raiderAmt = claimAurumLpRewards()
    txLogger.info(f"Claimed raider amt of {raiderAmt}")
    swapTxn(raiderAmt, raiderWmaticUsdcPath)
    txLogger.info(f"Swap raider {convertFromWei(raiderAmt)} to usdc")
