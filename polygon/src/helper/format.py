
from decimal import Decimal
from typing import Any, Type, Union, cast, NewType
from web3 import Web3
import web3
from web3.types import Wei


def convertFromWei(amount: int) -> float:
    '''
      convert amount to type assuming 10^18 decimals
    '''
    return cast(float, Web3.fromWei(amount, 'ether'))


def convertToWei(amount: float) -> Wei:
    return Web3.toWei(amount, 'ether')


def convertToWeiUSDC(amount: float) -> Wei:
    return cast(Wei, int(amount * (pow(10, 6))))


def convertFromWeiUSDC(amount: int) -> float:
    return amount / pow(10, 6)


def calcualateMin(amt: float) -> int:
    return int(amt / 100 * 99.5)
