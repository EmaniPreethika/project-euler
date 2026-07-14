"""
   I have used stacks just to play around with DSA
   You will not be expected to code this solution as it can be done with O(1)complexity
"""


def is_palindrome(number):
    stack = []
    temp = number
    #or temp =str(number) 

    # Push each digit onto the stack
    while temp > 0:
        stack.append(temp % 10)
        temp //= 10

    # Compare with popped digits
    while number > 0:
        digit = number % 10
        if digit != stack.pop():
            return False
        number //= 10

    return True


def largest_palindrome_product(num_digits):
    smallest = 10 ** (num_digits - 1)
    largest = 10**num_digits - 1

    max_palindrome = 0

    for i in range(largest, smallest - 1, -1):
        for j in range(largest, smallest - 1, -1):
            product = i * j

            if is_palindrome(product):
                max_palindrome = max(max_palindrome, product)

    return max_palindrome


num_digits = int(input("Enter the number of digits: "))
print(largest_palindrome_product(num_digits))
