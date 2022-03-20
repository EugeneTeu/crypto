from typing import cast, NewType
from web3 import Web3
from web3.types import Wei
from src.clients import aurumStakingClient

rewards = aurumStakingClient.userPendingRewards()
Aurum = NewType("Aurum", float)
print(cast(Aurum, Web3.fromWei(rewards, 'ether')))
