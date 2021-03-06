from src.helper.format import convertFromWei, convertFromWeiUSDC, convertToWei, convertToWeiUSDC
from src.processor import getSwapTxnAmountOut, getSlpAmountOut
hash = "0xaaed3f544294cac26a855af9def94d25c09137a48321dfb7f8bccb1555ab0c47"
expected = convertToWei(0.000040280031294405)
actual = getSlpAmountOut(hash)

hash2 = "0xe6cf4eef424e26fc9935216b7a6150eead3f5df56caaa9d05f0a9be350dc8719"
expected2 = convertToWei(0.000056354036191093)
actual2 = getSlpAmountOut(hash2)

if actual == expected:
    print(f"{hash} passed")
else:
    print(f"{hash} wrong")


if actual2 == expected2:
    print(f"{hash2} passed")
else:
    print(f"actual {actual2}, expected {expected2} ")
    print(f"{hash2} wrong")


hash1 = "0xee36e9982897b51430ffe17d64ecc7dd0539504d24c8b5d67a987210b42a0623"
val1 = getSwapTxnAmountOut(
    hash1)
hash2 = "0xc121e32e18cd0e9b3235efb7ba892fad37a7927dc9ba99f247b2a93c953f4aff"
val2 = getSwapTxnAmountOut(
    hash2)


if val1 == 273616984441948545226:
    print(f"getSwapTxnAmountOut passed for hash {hash1}")
else:
    print(f"actual {val1}, expected {273616984441948545226} ")
    print(f"{hash1} wrong")


if val2 == 8533389:
    print(f"getSwapTxnAmountOut passed for hash {hash2}")
else:
    print(f"actual {val2}, expected {8533389} ")
    print(f"{hash2} wrong")
