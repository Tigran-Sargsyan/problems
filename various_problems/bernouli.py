import math

def bernouli(n,k,p):
    """
    A function to calculate the probability
    of the Bernouli trials
    """
    return math.comb(n,k) * (p**k) * ((1-p)**(n-k))

def bernouli_cdf(n,k,p):
    """
    A function which returns the CDF(F(k)) of a
    Bernouli trials with paramaters (n,p)
    """
    prob = 0
    for i in range(k+1):
        prob += bernouli(n,i,p)
    
    return prob
 

p = float(input('Enter the probability of the event: '))
n = int(input('Enter the number of trials: '))
success = int(input('Enter the number of successes: '))

k = n - 1 - success
probability = 1 - bernouli_cdf(n,k,p)     

print(f'The probability of the event happaning {success} or more times is: {probability}')