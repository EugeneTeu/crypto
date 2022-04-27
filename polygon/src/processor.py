from src.clients import sushiswapRouterClient,  getUniswapV2Client, raiderUsdcSLPTokenClient
from web3.types import TxReceipt, LogReceipt


def getSwapTxnAmountOut(txHash: str) -> int:
    '''
        return amount received from a single swap event in Wei
    '''
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
    return processSwapTxnLog(txReceipt)

# TODO: this depends on number of paths. here is only a single addr to addr swap


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


def getSlpDeposited(txReceipt: TxReceipt) -> int:
    '''
        return in wei the amount of SLP received in this txn
    '''
    logs = txReceipt["logs"]
    transferLog = logs[len(logs) - 4]
    slp = raiderUsdcSLPTokenClient.processTransferEvent(transferLog)
    return slp


def getSlpAmountOut(txHash: str) -> int:
    txReceipt = sushiswapRouterClient.getTransactionReceipt(txHash)
    return getSlpDeposited(txReceipt)
