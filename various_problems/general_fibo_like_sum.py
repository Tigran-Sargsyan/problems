def fibo(n):   
    if n == 1 or n == 2:  
        return 1  
    else:  
        return (fibo(n - 1) + fibo(n - 2))   

def formula(a, b, n):
    return a + (fibo(n) - 1) * a + (fibo(n + 1) - 1) * b 

def iterative(a, b, n):
    seq_sum = a + b
    for i in range(n - 2):
        a, b = b, a + b
        seq_sum += b
        
    return seq_sum
    
a = 4
b = 7

for n in range(2, 20):
    print("formula: ", formula(a, b, n))
    print("iterative: ", iterative(a, b, n))
    print("-------------")
