#https://projecteuler.net/problem=5

"""
   when you are asked to find the common factor that satisfies all conditions, its lcm
   I have shown three ways to do it and timed each execution
   formula of lcm = a*b = hcf * lcm
"""

"""
  I added a lot of features.
  code modularity, split each operations in different functions(def)
  code reuasability - DRY principle -Dont repeat yourself. 
  abstraction - in execution() method we dont know how lcm is calculated
  fuction passed as parameter

"""
import math,time

# math formula = a*b = hcf * lcm

def gcd_iterative(x,y):
    small = x if x < y else y# or small = min(x,y)
    for i in range(small,0,-1):
        if  x % i == 0  and  y % i == 0:
            return i
    
    
    

def gcd_euclidean(x, y):# switch variables if y>x
    while y:#till y = 0, i.e reminder is 0 and loop breaks as 0 is false
        x, y = y, x % y
    return x


def lcm_upto(limit,hcf_function):
    lcm_result = 1
    for i in range( 2, limit + 1 ):#lcm of 1 and n is always n
        hcf = hcf_function(lcm_result, i)
        lcm_result = (lcm_result * i) // hcf
    return lcm_result    
        
        

#combined it lcm formula is the same
def built_in_lcm(limit):
    i=2
    lcm_result=1
    while(i<=limit):
        lcm_result = math.lcm(lcm_result,i) 
        i+=1 #in java c c++ you can do the increment counter i++
    return lcm_result    


def execution(name, func, *args):
    start = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - start

    print(f"{name}")
    print(f"LCM = {result}")
    print(f"{elapsed:.6f} seconds\n")


def main():
    limit = int(input("Enter number: "))
    execution("Iterative GCD", lcm_upto, limit, gcd_iterative)
    execution("Euclidean GCD", lcm_upto, limit, gcd_euclidean)
    execution("Built-in LCM", built_in_lcm, limit)

if __name__ == "__main__":
    main()

"""
I reduced many lines of codes written in 72-92 to:
lines 65-69 and 55 - 62
DRY Principle
"""    
# # Iterative HCF
# print("Iterative HCF")
# start = time.perf_counter()
# print("LCM =", lcm_upto(limit, gcd_iterative))
# print(f"Execution time: {(time.perf_counter() - start):.6f} seconds")

# # Euclidean HCF
# print("Euclidean HCF")
# start = time.perf_counter()
# print("LCM =", lcm_upto(limit, gcd_euclidean))
# print(f"Execution time: {(time.perf_counter() - start):.6f} seconds")

# print('Built in function')
# start = time.perf_counter()
# print(in_built_lcm_function(limit)) #in math module
# print(f"Execution time: {(time.perf_counter() - start):.6f} seconds")


