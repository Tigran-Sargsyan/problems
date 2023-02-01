file_name = input("Enter the name of the file: ")
with open(f"{file_name}.txt") as file:
  file = file.read().split()
  len_lst = [] # A list for storing the length of each word in a text file
for word in file:
  len_lst.append(len(word))

len_lst.sort()
print(file) 
print(len_lst)

mean = sum(len_lst) / len(file)

if len(file) % 2 == 0:
  median = (len_lst[len(file) // 2] + len_lst[len(file) // 2 - 1]) / 2 
else:
  median = len_lst[len(file)//2]

mode,max = 0,0
for len in set(len_lst):
  if len_lst.count(len) > max:
      max = len_lst.count(len)
      mode = len
    

print("Mean is: ",mean)
print("Median is: ",median)
print("Mode is: ",mode)