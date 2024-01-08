"""
given two numbers 'a' and 'b' calculates the sum of the sequence descripted below.
[a, b, a+b, b+a+b, a+b+b+a+b, ...]

a1 = a
a2 = b
....
an = a(n-1) + a(n-2)
"""

def intuitive_formula(a, b, n):
    return a + (fibo_general(1, 1, n) - 1) * a + (fibo_general(1, 1, n + 1) - 1) * b 

def iterative_solution(a, b, n):
    seq_sum = a + b
    for i in range(n - 2):
        a, b = b, a + b
        seq_sum += b
        
    return seq_sum

def fibo_general(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fibo_general(a, b, n - 2) + fibo_general(a, b, n - 1)

def fibo_general_sum(a, b, n):
    return fibo_general(a, b, n + 2) - b
    
a = 4
b = 7

for n in range(2, 20):
    print("intuitive formula: ", intuitive_formula(a, b, n))
    print("fibo general sum formula: ", fibo_general_sum(a, b, n))
    print("iterative solution: ", iterative_solution(a, b, n))
    print("-------------")
