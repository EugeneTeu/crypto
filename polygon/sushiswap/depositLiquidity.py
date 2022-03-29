from src.helper.format import convertToWei, convertFromWeiUSDC, convertToWeiUSDC, calcualateMin
from src.constants.constants import AURUM_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT
from src.clients import sushiswapRouterClient, usdcTokenClient
from src.logger.logger import logger
from src.logger.txLogger import txLogger, logTx
from web3.types import TxReceipt


def depositToken(tokenA: str, tokenB: str, amtA: int, amtB: int) -> TxReceipt:
    '''
        pass in wei values
    '''

    # base off all aurum u have
    path = [tokenA, tokenB]
    path2 = [tokenB, tokenA]
    assert(tokenA != tokenB)

    # simulate deposit amount
    vals = sushiswapRouterClient.getAmountsOut(amtA, path)
    vals2 = sushiswapRouterClient.getAmountsOut(amtB, path2)
    amtNeeded = vals[len(vals) - 1]
    amtNeeded2 = vals2[len(vals) - 1]
    if amtNeeded > amtB:
        # i have more aurum
        logger.error(f"amount needed for tokenA {amtNeeded} > {amtB}")
        # reduce the usdc needed
        amtB = amtNeeded
        # then we continue
    if amtNeeded2 > amtA:
        # i have more of amtB
        logger.error(f"amount needed for tokenB {amtNeeded} > {amtA}")
        # reduce the usdc needed
        amtA = amtNeeded2
        # then we continue

        # assume wei
    minAmtA = calcualateMin(amtA)
    minAmtB = calcualateMin(amtB)

    txHash = sushiswapRouterClient.addLiquidity(
        tokenA, tokenB, amtA, amtB, minAmtA, minAmtB)
    txLogger.info(txHash)
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
    if txReceipt["status"] != 1:
        logs = txReceipt["logs"]
        txLogger.error(f"transaction failed: {logs}")
        exit(1)
    logTx(txReceipt)
    return txReceipt
