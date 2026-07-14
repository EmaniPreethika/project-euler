# explanaiton in https://medium.com/p/a01d419b3de6?postPublishedType=initial
def collatz_length(n, cache):
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        chain_length = 1 + collatz_length(n // 2, cache)
    else:
        chain_length = 1 + collatz_length(3 * n + 1, cache)
    cache[n] = chain_length
    return chain_length

cache = {}
max_chain = 0
result = 0
for i in range(1, 1000001):
    chain = collatz_length(i, cache)
    if chain > max_chain:
        max_chain = chain
        result = i

print(result)