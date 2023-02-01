my_dict = {} #Dictionary for storing how many times has each word occured in the given txt file
file_name = input("Enter the file name: ")

with open (f"{file_name}.txt") as file:
    file = file.read()
    file = file.split()
    for word in file:
        word = word.lower()
        if not word in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1    

most_used_word = ""
most_used_count = 0

for k,v in my_dict.items():
    if v > most_used_count:
        most_used_count = v
        most_used_word = k

for k,v in my_dict.items():
    print(k,":",v)
    
print(f"The most used word in your text is '{most_used_word}' which is used {most_used_count} times.")