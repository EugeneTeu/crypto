from src.clients import UsdcWavaxLpClient, TusWavaxLpCLient, getTokenClient
from src.traderJoeClient.JoeLcWebc3Client import JoeLcWeb3Client


def getPrice(lcClient: JoeLcWeb3Client):
    reserves = lcClient.getReserves()
    reserveToken0 = reserves[0]
    reserveToken1 = reserves[1]

    token0Address = lcClient.getToken0()
    token1Address = lcClient.getToken1()

    t0Client = getTokenClient(token0Address)
    t1Client = getTokenClient(token1Address)

    t0TokenInfo = t0Client.getTokenInfo()
    t1TokenInfo = t1Client.getTokenInfo()

    token0Symbol = t0TokenInfo["symbol"]
    token0Decimals = t0TokenInfo["decimals"]

    token1Symbol = t1TokenInfo["symbol"]
    token1Decimals = t1TokenInfo["decimals"]

    if token0Symbol == "WAVAX":
        price = (reserveToken1/10**token1Decimals) / \
            (reserveToken0/10**token0Decimals)
    else:
        price = (reserveToken0/10**token0Decimals) / \
            (reserveToken1/10**token1Decimals)
    return price


def getUSDCInWavax():
    return getPrice(UsdcWavaxLpClient)


def getUSDCPrice(amt):
    '''
      convert wavax denoted amounts to actual USD
    '''
    return getUSDCInWavax() / amt
