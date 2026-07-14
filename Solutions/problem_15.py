"""
How many such routes to reach point A - B: This is a classic combination problem
Learn about Permutation and Combination before you solve this 
    
"""
import math
m, n = map(int, input().split()) #grid row and column
factorial_denominator = math.prod(i for i in range(1,m+1)) 
factorial_numeratorator = math.prod(i for i in range(m+n,m,-1))
print(factorial_numeratorator//factorial_denominator)
