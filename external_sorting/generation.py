import random

file = open("big.txt","w")
for j in range(20):
    [file.write(str(random.randint(1,1_000_000))+" ") for i in range(50_000_000)]
    file.write("\n")

file.close()
