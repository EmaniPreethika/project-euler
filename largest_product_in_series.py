#https://projecteuler.net/problem=8
from math import prod
def largest_product(number,window_size):
    n_adjacent_digits = 0
    left,right = 1,window_size + 1
    #below splitting the number into an array of its digits
    number = [int(digit) for digit in str(number)]
    max_product = prod(number[:window_size])

    while right <= len(number):
        product = 1
        product = prod(number[left:right])
        if product > max_product:
            max_product = product
            n_adjacent_digits = number[left:right]
            #the below converts array to number form
            n_adjacent_digits =  int("".join(map(str, n_adjacent_digits)))
        left,right = left + 1 , right + 1  
    print(f"The number is: {n_adjacent_digits}")    
    return max_product    


number = int(input("Number: "))
window_size = int(input("N digits: "))
print(f"The product of the number is: {largest_product(number, window_size)}")    

