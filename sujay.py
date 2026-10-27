#bitwise left shift(<<)
# << moves bits left. Empty spots on the right become 0.
# Each step multiplies by 2.
a=2
print(12<<a)        # 48    12 * 2 * 2

#bitwise right shift(>>)
# >> moves bits right and drops bits on the right.
# Each step does floor division by 2.
print(12>>2)        # 3     12 // 4
