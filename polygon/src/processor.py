from src.clients import sushiswapRouterClient,  getUniswapV2Client
from web3.types import TxReceipt, LogReceipt


def getSwapTxnAmountOut(txHash: str) -> int:
    '''
        return amount received from a single swap event in Wei
    '''
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
    return processSwapTxnLog(txReceipt)


def processSwapTxnLog(txReceipt: TxReceipt) -> int:
    logs = txReceipt["logs"]
    swapLog = logs[len(logs) - 2]
    return getSwapLogFromSwapEvent(swapLog)


def getSwapLogFromSwapEvent(swapLog: LogReceipt) -> int:
    '''
        return amount received from a single swap event in Wei
    '''
    slpAddress = swapLog["address"]
    client = getUniswapV2Client(slpAddress)
    amt = client.processSwapEvent(swapLog)
    return amt
