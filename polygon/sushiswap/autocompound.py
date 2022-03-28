
from enum import auto
import json

from hexbytes import HexBytes
from src.helper.format import convertFromWei, convertFromWeiUSDC, convertToWei, convertToWeiUSDC
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT, AURUM_USDC_SLP_TOKEN_CONTRACT
from sushiswap.depositLiquidity import depositToken
from sushiswap.swapToken import simulateAmount, swapTxn
from src.clients import aurumStakingClient, sushiswapRouterClient, raiderUsdcSLPTokenClient
from src.getAurumLpRewards import claimAurumLpRewards
from src.logger.txLogger import logTx, txLogger
from src.stakeAurumLp import stakeAurumLp
from web3.types import TxReceipt

raiderWmaticAurumPath = [RAIDER_TOKEN_CONTRACT,
                         WMATIC_TOKEN_CONTRACT, AURUM_TOKEN_CONTRACT]
raiderWmaticUsdcPath = [RAIDER_TOKEN_CONTRACT,
                        WMATIC_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT]


def getSlpDeposited(txReceipt: TxReceipt) -> int:
    '''
        return in wei the amount of SLP received in this txn
    '''
    logs = txReceipt["logs"]
    for log in logs:
        if log["address"] == AURUM_USDC_SLP_TOKEN_CONTRACT:
            for topic in log["topics"]:
                if topic == HexBytes("0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"):
                    slp = raiderUsdcSLPTokenClient.processTransferEvent(log)
                    if slp == -1:
                        continue
                    else:
                        return slp
    raise Exception("error parsing logs, is it wrong topic?")


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
    txReceipt = depositToken(AURUM_TOKEN_CONTRACT,
                             USDC_TOKEN_CONTRACT, minAmtA, minAmtB)
    # get balance of SLP
    slpDeposited = getSlpDeposited(txReceipt)
    # stake SLP
    stakeAurumLp(slpDeposited)
