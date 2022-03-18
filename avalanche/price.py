from src.price import getPrice, getUSDCPrice
from src.clients import TusWavaxLpCLient

tusPrice = getPrice(TusWavaxLpCLient)
print(getUSDCPrice(tusPrice))
