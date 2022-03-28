from sushiswap.autocompound import getSlpDeposited
from src.helper.format import convertFromWei, convertFromWeiUSDC, convertToWei, convertToWeiUSDC

hash = "0xaaed3f544294cac26a855af9def94d25c09137a48321dfb7f8bccb1555ab0c47"
expected = convertToWei(0.000040280031294405)
actual = getSlpDeposited(hash)

hash2 = "0xe6cf4eef424e26fc9935216b7a6150eead3f5df56caaa9d05f0a9be350dc8719"
expected2 = convertToWei(0.000056354036191093)
actual2 = getSlpDeposited(hash2)

if actual == expected:
    print(f"{hash} passed")
else:
    print(f"{hash} wrong")


if actual2 == expected2:
    print(f"{hash2} passed")
else:
    print(f"actual {actual2}, expected {expected2} ")
    print(f"{hash2} wrong")
