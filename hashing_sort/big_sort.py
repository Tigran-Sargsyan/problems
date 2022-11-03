"""Sorting a file containing 1 000 000 000 integers using hashing method"""

file = open("big_file.txt","r")
lst = [0] * 121

for i in range(1_000_000):
    #Reading 1 000 000 lines of the file
    nums = file.readline()

    nums = nums.split()  #spliting the numbers in each line
    for j in range(121):
        count = nums.count(str(j))
        lst[j] += count   #incrementing the number under the corresponding list index

file.close()

print(lst)   # Every index shows how many times has the index_number occured in our file

sorted_list = open("sorted_list.txt","w")

el_counter = 0
for i in range(121):
    for j in range(lst[i]):
        sorted_list.write(str(i)+" ")
        el_counter += 1
        if el_counter == 1000:
            sorted_list.write("\n")
            el_counter = 0

sorted_list.close()