""" 
triangle number     sum calc    

Sum Calc    Trinagle_number	    Factors
1	            1	               1
1+2	            3	               1 3
1+2+3	        6	               1 2 3 6
1+2+3+4	        10	               1 2 5 10

"""
import math
i = 1
triangle_number = 0
while True:
    counter = 0
    triangle_number = triangle_number + i # avoids sum calc by formula and for loop
    """ when I ran the div for loop till triangle_number it became indefinetly slow
        so I used the same method I used in prime numbers and 
        reduced O(N) -----> O(N ^ 0.5)
     
     """
    for div in range(1, int(math.isqrt(triangle_number)) + 1): 
        if triangle_number % div ==0:
            if div is not triangle_number:
                counter = counter + 2
            else:
                counter = counter + 1
    if counter > 500 :
        print(triangle_number)
        break
        
    i = i + 1