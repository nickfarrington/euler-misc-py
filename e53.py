def fact(n, memo = {0:1, 1: 1}):
    try:
        return memo[n]
    except KeyError:
        result = n * fact(n - 1)
        memo[n] = result
        return result

'''
def fact_no_memo(n):
    result = 1
    for i in range(1,n + 1): Ended up more or less doubling speed to implement memo
        result *= i
    return result
'''

def ncr(n,r):
    return fact(n) / (fact(r) * fact(n - r))

count = 0
for n in range(1,101):
    for r in range(1,n + 1):
        if ncr(n,r) > 1000000:
            count += 1

print(count)
