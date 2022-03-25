
from enum import auto
from src.helper.format import convertFromWei, convertFromWeiUSDC, convertToWei, convertToWeiUSDC
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT
from sushiswap.depositLiquidity import depositToken
from sushiswap.swapToken import simulateAmount, swapTxn
from src.clients import aurumStakingClient, sushiswapRouterClient
from raider.getAurumLpRewards import claimAurumLpRewards
from src.logger.txLogger import logTx, txLogger
from raider.stakeAurumLp import stakeAurumLp

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
    minAmtOut = swapTxn(raiderAmt, raiderWmaticUsdcPath)

    # TODO: get returned amount swapped from swapTxn
    txLogger.info(
        f"Swap raider {convertFromWei(raiderAmt)} to approx {convertFromWeiUSDC(minAmtOut)} usdc")


def autoCompound() -> None:
    raiderAmt = claimAurumLpRewards()
    txLogger.info(f"Claimed raider amt of {raiderAmt}")
    splitAmt = int(raiderAmt / 2)
    # swap raider to aurum
    minAmtA = swapTxn(splitAmt, raiderWmaticAurumPath)
    # swap raider to usdc
    minAmtB = swapTxn(splitAmt, raiderWmaticUsdcPath)
    depositToken(AURUM_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, minAmtA, minAmtB)
    # get balance of SLP 
    # stake SLP 
