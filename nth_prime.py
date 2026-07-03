#https://projecteuler.net/problem=7
'''
I tried to run it by formulas but it does not hold true for all numbers
So gotta do the divisibility rule
'''
import math
def calc_nth_prime(limit) :
    counter,number = 0,2
    while True :
        divisor_count = 0
        for i in range(2,int(math.sqrt(number)+1)):
            if number % i == 0:
                divisor_count = divisor_count + 1
        if not divisor_count:
            counter = counter + 1
        if counter == limit:
            return number
        number = number + 1
limit = int(input())            
print(calc_nth_prime(limit))