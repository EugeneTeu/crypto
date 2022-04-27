

from eth_typing import Address, ChecksumAddress
from web3 import Web3
from src.helper.format import convertToWei
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT
from src.clients import sushiswapRouterClient
from src.logger.txLogger import logTx, txLogger
from src.processor import processSwapTxnLog


def createPath(addresses: list[str]) -> list[ChecksumAddress]:
    result = []
    for addr in addresses:
        result.append(Web3.toChecksumAddress(
            addr))
    return result


def swapTxn(amtIn: int, path: list[ChecksumAddress]) -> int:
    '''
        returns minimum amount out swapped in wei
    '''
    # simulate swap amount
    val1 = sushiswapRouterClient.getAmountsOut(amtIn, path)

    amtOut = val1[len(val1) - 1]
    # account for slippage
    amtOutMin = int(amtOut / 100 * 99.5)
    # transact
    try:
        txHash = sushiswapRouterClient.swapExactTokensForTokens(
            amtIn, amtOutMin, path)
        txLogger.info(txHash)
        txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
        amountOut = processSwapTxnLog(txReceipt)
        # amountOut = 0
        return amountOut
    except Exception as e:
        txLogger.error(f"failed swap - {e}")
        exit(1)


def swapTxnV2(amtIn: int, path: list[ChecksumAddress]) -> None:
    '''
        returns minimum amount out swapped in wei
    '''
    # simulate swap amount
    val1 = sushiswapRouterClient.getAmountsOut(amtIn, path)

    amtOut = val1[len(val1) - 1]
    # account for slippage
    amtOutMin = int(amtOut / 100 * 99.5)
    # transact
    try:
        txHash = sushiswapRouterClient.swapExactTokensForTokens(
            amtIn, amtOutMin, path)
        txLogger.info(txHash)
        txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
        logTx(txReceipt)
    except Exception as e:
        txLogger.error(f"failed swap - {e}")
        exit(1)


def simulateAmount(amtIn: float, path: list[str]) -> int:
    amtIn = convertToWei(amtIn)
    val1 = sushiswapRouterClient.getAmountsOut(amtIn, path)
    amtOut = val1[len(val1) - 1]
    return amtOut
