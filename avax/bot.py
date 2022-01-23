import json
from time import sleep
from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# crabs
# CRAB_CONTRACT = "0xfb60Cb3B62a24760F07089f2bA194BFb3FeffcD9"
# with open("crabada.json") as craFile:
#     craABI = json.load(craFile)
# crabContract = w3.eth.contract(address=w3.toChecksumAddress(
#     CRAB_CONTRACT), abi=craABI)
# print(crabContract.functions.startGame(95).transact())

# with open("pool.json") as poolFile:
#     poolABI = json.load(poolFile)
with open("ERC20.json") as erc20File:
    ERC20ABI = json.load(erc20File)

# liquidityContract = w3.eth.contract(address=w3.toChecksumAddress(
#     "0x9ee0a4e21bd333a6bb2ab298194320b8daa26516"), abi=poolABI)

# reserves = liquidityContract.functions.getReserves().call()
# reserveToken0 = reserves[0]
# reserveToken1 = reserves[1]

# token0Address = liquidityContract.functions.token0().call()
# token1Address = liquidityContract.functions.token1().call()

# token0 = w3.eth.contract(
#     address=w3.toChecksumAddress(token0Address), abi=ERC20ABI)
# token1 = w3.eth.contract(
#     address=w3.toChecksumAddress(token1Address), abi=ERC20ABI)

# token0Symbol = token0.functions.symbol().call()
# token0Decimals = token0.functions.decimals().call()

# token1Symbol = token1.functions.symbol().call()
# token1Decimals = token1.functions.decimals().call()


# if token0Symbol == "WAVAX":
#     price = (reserveToken1/10**token1Decimals) / \
#         (reserveToken0/10**token0Decimals)
# else:
#     price = (reserveToken0/10**token0Decimals) / \
#         (reserveToken1/10**token1Decimals)
# print("The current price of AVAX is {:4.2f} USDT from pangolin".format(price))

def getPriceFromLC(LC):
    reserves = LC.functions.getReserves().call()
    reserveToken0 = reserves[0]
    reserveToken1 = reserves[1]
    token0Address = LC.functions.token0().call()
    token1Address = LC.functions.token1().call()
    token0 = w3.eth.contract(
        address=w3.toChecksumAddress(token0Address), abi=ERC20ABI)
    token1 = w3.eth.contract(
        address=w3.toChecksumAddress(token1Address), abi=ERC20ABI)
    token0Symbol = token0.functions.symbol().call()
    token0Decimals = token0.functions.decimals().call()

    token1Symbol = token1.functions.symbol().call()
    token1Decimals = token1.functions.decimals().call()
    if token0Symbol == "WAVAX":
        price = (reserveToken1/10**token1Decimals) / \
            (reserveToken0/10**token0Decimals)
    else:
        price = (reserveToken0/10**token0Decimals) / \
            (reserveToken1/10**token1Decimals)
    return price


usdcToken = w3.eth.contract(address=w3.toChecksumAddress(
    "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664"), abi=ERC20ABI)
usdcTokenSymbol = usdcToken.functions.symbol().call()
usdcTokenDecimal = usdcToken.functions.decimals().call()

with open("traderjoe.json") as joeFile:
    joeRouterABI = json.load(joeFile)
with open("joepool.json") as joePoolFile:
    joePoolABI = json.load(joePoolFile)

WAVAX_TUS_LC = w3.eth.contract(address=w3.toChecksumAddress(
    "0x565d20BD591b00EAD0C927e4b6D7DD8A33b0B319"), abi=joePoolABI)

WAVAX_USDC_LC = w3.eth.contract(address=w3.toChecksumAddress(
    "0xA389f9430876455C36478DeEa9769B7Ca4E3DDB1"), abi=joePoolABI)

while(True):
    tusInWAVAX = getPriceFromLC(WAVAX_TUS_LC)
    USDCInWAVAX = getPriceFromLC(WAVAX_USDC_LC)
    price = USDCInWAVAX / tusInWAVAX
    print(
        "The current price of TUS is {:4.5f} USDC on traderjoe".format(price))
    sleep(5)


# joeLC = w3.eth.contract(address=w3.toChecksumAddress(
#     ("0x60aE616a2155Ee3d9A68541Ba4544862310933d4")), abi=joeRouterABI)
# hard coded with values from gql api
# reserves = joeLC.functions.getAmountIn(
#     1, 82221652, 1291922).call()
# print(reserves)
