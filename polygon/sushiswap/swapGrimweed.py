from sushiswap.swapToken import swapTxnV2
from web3 import Web3
from sys import argv
from src.logger.logger import logger

GRIMWEED_TO_USDC = [
    Web3.toChecksumAddress("0x06F34105B7DfedC95125348A8349BdA209928730"),
    Web3.toChecksumAddress("0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23"),
    Web3.toChecksumAddress("0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174")
]
if len(argv) < 2:
    logger.error("Specify grimweed amount")
    exit(1)

grimweedAmount = argv[1]

swapTxnV2(int(grimweedAmount), GRIMWEED_TO_USDC)
