#https://medium.com/p/f57aadbcac14?postPublishedType=initial

def pythogoras_triplet(n):
    for a in range(1, n // 2):
        numerator = n * (n - 2 * a)
        denominator = 2 * (n - a)

        if numerator % denominator != 0:#b should be a int
            continue

        b = numerator // denominator
        if not b > a:
            continue
        c = n - a - b

        if b < c:
            return a * b * c
n = int(input()) 
print(pythogoras_triplet(n))            