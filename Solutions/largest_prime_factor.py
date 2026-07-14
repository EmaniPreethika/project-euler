#https://projecteuler.net/problem=3

def max_prime_factor(n):
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 1

    return n
print(max_prime_factor(int(input())))