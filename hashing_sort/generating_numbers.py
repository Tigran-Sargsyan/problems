"""Generating a file containing 1 000 000 000 integers in interval [0,120]"""

import random
file = open("big_file.txt","w")

for i in range(1, 1_000_000_000):
    current = str(random.randint(0, 121)) + " "
    file.write(current)
    if i % 1000 == 0:
        file.write("\n")

file.close()
