def base_10_easy_pythonic(num,x):
    return int(num, x)

def base_10(n,p):
    """
    A function that takes the number n in base-system p as input
    and returns it's transaltion to base-10 system
    """
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'  # Alphabet for base-systems
    alpha_numbers = list(range(37))                   # Holding the correspondent numbers
    number = 0                                      # A variable for holding the return number
    power = 0                                      # A variable for keeping power count
    for i in n[::-1]:            
        indexx = alphabet.index(i)
        if indexx >= p: 
            print("The base system does not have such number!")
            return False
        number += alpha_numbers[indexx] * (p**power)
        power += 1
    return number

print(base_10('a',13))
print(base_10_easy_pythonic('a1c',16))
