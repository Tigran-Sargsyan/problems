output = open("sorted.txt","w")
chunk1 = open("chunk1.txt", "r+")
chunk2 = open("chunk2.txt", "r+")
chunk3 = open("chunk3.txt", "r+")
chunk4 = open("chunk4.txt", "r+")
chunk5 = open("chunk5.txt", "r+")
chunk6 = open("chunk6.txt", "r+")
chunk7 = open("chunk7.txt", "r+")
chunk8 = open("chunk8.txt", "r+")
chunk9 = open("chunk9.txt", "r+")
chunk10 = open("chunk10.txt", "r+")
chunk11 = open("chunk11.txt", "r+")
chunk12 = open("chunk12.txt", "r+")
chunk13 = open("chunk13.txt", "r+")
chunk14 = open("chunk14.txt", "r+")
chunk15 = open("chunk15.txt", "r+")
chunk16 = open("chunk16.txt", "r+")
chunk17 = open("chunk17.txt", "r+")
chunk18 = open("chunk18.txt", "r+")
chunk19 = open("chunk19.txt", "r+")
chunk20 = open("chunk20.txt", "r+")

lst = []

for i in range(1,21):
    num = eval(f"chunk{i}").readline()
    num = num.replace("\n","")   
    lst.append(int(num))

t = 1
while t < 1_000_000_000:
    if lst:
        minimal = min(lst)
        output.write(str(minimal)+" ")
        min_index = lst.index(minimal)

        for i in range(20):
            if min_index == i:
                current = eval(f"chunk{i+1}").readline()
                if current:
                    current = current.replace("\n","")
                    lst.remove(minimal)
                    lst.insert(min_index,int(current))
                else:
                    lst.remove(minimal)    
    t+=1

print(lst)
chunk1.close()
chunk2.close()
chunk3.close()
chunk4.close()
chunk5.close()
chunk6.close()
chunk7.close()
chunk8.close()
chunk9.close()
chunk10.close()
chunk11.close()
chunk12.close()
chunk13.close()
chunk14.close()
chunk15.close()
chunk16.close()
chunk17.close()
chunk18.close()
chunk19.close()
chunk20.close()
