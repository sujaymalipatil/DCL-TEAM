# learnt: 8 Oct 2026
# Bitwise operators use the binary (0 and 1) form of integers.
# 12 in binary is 1100.  5 in binary is 0101.

#bitwise and
# & keeps a bit only where BOTH numbers have 1.
# 1100 & 0101 = 0100, which is 4
print(12 & 5)       # 4

#bitwise or
# | keeps a bit where EITHER number has 1.
# 1100 | 0101 = 1101, which is 13
print(12 | 5)       # 13

#bitwise xor
# ^ keeps a bit where the two bits are DIFFERENT.
# 1100 ^ 0101 = 1001, which is 9
print(12^5)         # 9

#bitwise not(~)
# ~ flips every bit. In Python, ~n = -n - 1
print(~12)          # -13

