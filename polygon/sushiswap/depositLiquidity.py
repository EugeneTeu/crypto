from src.helper.format import convertToWei, convertFromWeiUSDC, convertToWeiUSDC, calcualateMin
from src.constants.constants import AURUM_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT
from src.clients import sushiswapRouterClient, usdcTokenClient
from src.logger.logger import logger
from src.logger.txLogger import txLogger, logTx


def depositToken(tokenA: str, tokenB: str, amtA: int, amtB: int) -> None:
    '''
        pass in wei values
    '''

    # base off all aurum u have
    path = [tokenA, tokenB]
    assert(tokenA != tokenB)

    # simulate deposit amount
    vals = sushiswapRouterClient.getAmountsOut(amtA, path)
    amtNeeded = vals[len(vals) - 1]
    if amtNeeded > amtB:
        logger.error(f"amount needed {amtNeeded} > {amtB}")
        exit(1)

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
    logTx(txReceipt)
    return
