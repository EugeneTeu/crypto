from sushiswap.autocompound import autoCompound, test
from src.clients import sushiswapRouterClient

# Only call function here so we dont anyhow do txn
autoCompound()
