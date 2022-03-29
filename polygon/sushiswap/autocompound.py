
from enum import auto
import json

from hexbytes import HexBytes
from src.helper.format import convertFromWei, convertFromWeiUSDC, convertToWei, convertToWeiUSDC
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT, AURUM_USDC_SLP_TOKEN_CONTRACT
from sushiswap.depositLiquidity import depositToken
from sushiswap.swapToken import simulateAmount, swapTxn
from src.clients import aurumStakingClient, sushiswapRouterClient, raiderUsdcSLPTokenClient, getUniswapV2Client
from src.getAurumLpRewards import claimAurumLpRewards
from src.logger.txLogger import logTx, txLogger
from src.stakeAurumLp import stakeAurumLp
from web3.types import TxReceipt, LogReceipt
from src.logger.logger import logger

raiderWmaticAurumPath = [RAIDER_TOKEN_CONTRACT,
                         WMATIC_TOKEN_CONTRACT, AURUM_TOKEN_CONTRACT]
raiderWmaticUsdcPath = [RAIDER_TOKEN_CONTRACT,
                        WMATIC_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT]


def getSlpDeposited(txReceipt: TxReceipt) -> int:
    '''
        return in wei the amount of SLP received in this txn
    '''
    logs = txReceipt["logs"]
    if len(logs) != 8:
        raise Exception("wrong number of logs")
    transferLog = logs[len(logs) - 4]
    slp = raiderUsdcSLPTokenClient.processTransferEvent(transferLog)
    return slp


def stakeAndSellRaider() -> None:
    raiderAmt = claimAurumLpRewards()
    txLogger.info(f"Claimed raider amt of {raiderAmt}")
    minAmtOut = swapTxn(raiderAmt, raiderWmaticUsdcPath)
    # TODO: get returned amount swapped from swapTxn
    txLogger.info(
        f"Swap raider {convertFromWei(raiderAmt)} to approx {convertFromWeiUSDC(minAmtOut)} usdc")


def autoCompound() -> None:
    raiderAmt = claimAurumLpRewards()
    logger.info(f"Claimed raider amt of {raiderAmt}")
    splitAmt = int(raiderAmt / 2)
    # swap raider to aurum
    amtA = swapTxn(splitAmt, raiderWmaticAurumPath)
    # swap raider to usdc
    amtB = swapTxn(splitAmt, raiderWmaticUsdcPath)
    logger.info(f"swapped for {amtA} aurum and {amtB} USDC")
    txReceipt = depositToken(AURUM_TOKEN_CONTRACT,
                             USDC_TOKEN_CONTRACT, amtA, amtB)
    # get balance of SLP
    slpDeposited = getSlpDeposited(txReceipt)
    logger.info(f"SLP received: {slpDeposited}")
    # stake SLP
    stakeAurumLp(slpDeposited)
