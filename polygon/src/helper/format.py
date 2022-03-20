
from typing import cast, NewType
from web3 import Web3
from web3.types import Wei


def convertReadable(amount, type):
    '''
      convert amount to type assuming 10^18 decimals
    '''
    return cast(type, Web3.fromWei(amount, 'ether'))
