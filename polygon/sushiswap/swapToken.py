

from eth_typing import Address, ChecksumAddress
from web3 import Web3
from src.helper.format import convertToWei
from src.constants.constants import AURUM_TOKEN_CONTRACT, RAIDER_TOKEN_CONTRACT, USDC_TOKEN_CONTRACT, WMATIC_TOKEN_CONTRACT
from src.clients import sushiswapRouterClient
from src.logger.txLogger import logTx, txLogger


def createPath(addresses: list[str]) -> list[ChecksumAddress]:
    result = []
    for addr in addresses:
        result.append(Web3.toChecksumAddress(
            addr))
    return result


def swapTxn(amtIn: int, path: list[str]) -> int:
    '''
        returns minimum amount out swapped in wei
    '''
    # assume amtIn is in wei
    assert(path[0] != USDC_TOKEN_CONTRACT)
    # simulate swap amount
    val1 = sushiswapRouterClient.getAmountsOut(amtIn, path)
    amtOut = val1[len(val1) - 1]
    # account for slippage
    amtOutMin = int(amtOut / 100 * 99.5)
    # transact
    txHash = sushiswapRouterClient.swapExactTokensForTokens(
        amtIn, amtOutMin, path)
    txLogger.info(txHash)
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
    logTx(txReceipt)
    return amtOutMin


def simulateAmount(amtIn: float, path: list[str]) -> int:
    amtIn = convertToWei(amtIn)
    val1 = sushiswapRouterClient.getAmountsOut(amtIn, path)
    amtOut = val1[len(val1) - 1]
    return amtOut
