

from src.helper.format import convertToWei, convertFromWeiUSDC, convertToWeiUSDC
from src.constants.constants import AURUM_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT
from src.clients import sushiswapRouterClient, usdcTokenClient
from src.logger.logger import logger


def depositToken(tokenA: str, tokenB: str, amtA: float, amtB: float) -> None:
    # base off all aurum u have
    path = [tokenA, tokenB]
    assert(tokenA != tokenB)

    amtIn = convertToWei(
        amtA) if tokenA != USDC_TOKEN_CONTRACT else convertToWeiUSDC(amtA)

    # simulate swap amount
    vals = sushiswapRouterClient.getAmountsOut(amtIn, path)
    usdcNeeded = vals[len(vals) - 1]

    userUSDCBalance = usdcTokenClient.getBalance()
    if usdcNeeded > userUSDCBalance:
        logger.error(
            f"usdc needed {convertFromWeiUSDC(usdcNeeded)} more than current balance: {convertFromWeiUSDC(userUSDCBalance)}")

    # amtOutMin = int(amtOut / 100 * 99.5)
    # print(amtOut, amtOutMin)
