#https://projecteuler.net/problem=11
"""
FACT - the method used to find if a number is prime number is called:
                            Sieve of Eratosthenes 
"""

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def summation_of_primes(n):
    i = 2
    sum = 0
    while i < n:
        if is_prime(i):
            sum = sum + i
        i = i + 1    

    return sum        


n = int(input())
print(summation_of_primes(n))