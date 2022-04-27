
from enum import auto
import time

from hexbytes import HexBytes
from web3 import Web3
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
from src.processor import getSlpDeposited

raiderWmaticAurumPath = [Web3.toChecksumAddress(RAIDER_TOKEN_CONTRACT),
                         Web3.toChecksumAddress(WMATIC_TOKEN_CONTRACT), Web3.toChecksumAddress(AURUM_TOKEN_CONTRACT)]
raiderWmaticUsdcPath = [Web3.toChecksumAddress(RAIDER_TOKEN_CONTRACT),
                        Web3.toChecksumAddress(WMATIC_TOKEN_CONTRACT), Web3.toChecksumAddress(USDC_TOKEN_CONTRACT)]


def stakeAndSellRaider() -> None:
    raiderAmt = claimAurumLpRewards()
    txLogger.info(f"Claimed raider amt of {raiderAmt}")
    minAmtOut = swapTxn(raiderAmt, raiderWmaticUsdcPath)
    # TODO: get returned amount swapped from swapTxn
    txLogger.info(
        f"Swap raider {convertFromWei(raiderAmt)} to approx {convertFromWeiUSDC(minAmtOut)} usdc")


def getRaiderReward() -> None:
    raiderAmt = claimAurumLpRewards()
    logger.info(f"Claimed raider amt of {raiderAmt}")


def autoCompound() -> None:
    raiderAmt = claimAurumLpRewards()
    logger.info(f"Claimed raider amt of {raiderAmt}")
    splitAmt = int(raiderAmt / 2)
    time.sleep(5)
    # swap raider to aurum
    amtA = swapTxn(splitAmt, raiderWmaticAurumPath)
    time.sleep(5)
    # swap raider to usdc
    amtB = swapTxn(splitAmt, raiderWmaticUsdcPath)
    time.sleep(5)
    logger.info(f"swapped for {amtA} aurum and {amtB} USDC")
    txReceipt = depositToken(AURUM_TOKEN_CONTRACT,
                             USDC_TOKEN_CONTRACT, amtA, amtB)
    time.sleep(5)
    # get balance of SLP
    slpDeposited = getSlpDeposited(txReceipt)
    time.sleep(5)
    logger.info(f"SLP received: {slpDeposited}")
    # stake SLP
    stakeAurumLp(slpDeposited)
    logger.info(f"Auto compounding complete!")


def test() -> None:
    '''
        test with your amount of aurum + usdc
    '''
    aurum = 67961064017857483453
    usdc = 2187200
    txReceipt = depositToken(AURUM_TOKEN_CONTRACT,
                             USDC_TOKEN_CONTRACT, aurum, usdc)
    # get balance of SLP
    slpDeposited = getSlpDeposited(txReceipt)
    logger.info(f"SLP received: {slpDeposited}")
    # stake SLP
    stakeAurumLp(slpDeposited)
    logger.info(f"Auto compounding complete!")
