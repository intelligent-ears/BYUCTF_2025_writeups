U = 256
u = 3
pow_values = [pow(u, abs(i), U) for i in range(U)]
unique_pow = list(set(pow_values))
S = unique_pow[u : u + 30] 

รน = [
    12838, 1089, 16029, 13761, 1276, 14790, 2091, 17199, 2223, 2925,
    17901, 3159, 18135, 18837, 3135, 19071, 4095, 19773, 4797, 4085,
    20007, 5733, 20709, 17005, 2601, 9620, 3192, 9724, 3127, 8125
]

input_bytes = []
for a, c in zip(S, รน):
    input_bytes.append(c // a)

flag = ''.join(chr(b) for b in input_bytes)
print(flag)
