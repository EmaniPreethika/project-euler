
import math
def pythogoras_triplet(n):
    ''''
       Used the property of triangle where sum of 2 sides of a
       triangle is always greater than the third side
       https://chatgpt.com/share/6a47b920-18f8-83e8-a5e5-4c679b58db2a 
    '''
    for i in range(1,n//2):
        for j in range(i+1,n//2):
            hypotenuse_square = i**2 + j**2
            # hypotenuse = int(math.sqrt(hypotenuse_square)) 
            # above cant be used as it ignores the decimal point
            hypotenuse = math.sqrt(hypotenuse_square)
            
            if hypotenuse + i + j == 1000.0 and i<j<hypotenuse:
                print(i," ",j," ",int(hypotenuse))
                return int(hypotenuse * i * j)

n = int(input())
print(pythogoras_triplet(n))