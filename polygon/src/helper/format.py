
from typing import Any, Type, cast, NewType
from web3 import Web3
import web3
from web3.types import Wei


def convertReadable(amount: int) -> float:
    '''
      convert amount to type assuming 10^18 decimals
    '''
    return cast(float, Web3.fromWei(amount, 'ether'))


def convertToWei(amount: float) -> Wei:
    return Web3.toWei(amount, 'ether')
