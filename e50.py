def tf_primelist(n):    
#Credit to Nayuki on Github for helping me through this tough spot
    result = [False] * 2 + [True] * (n - 1)
    for i in range(int(n ** .5) + 1):
        if result[i]:
            for multiple in range(2 * i, n + 1, i):
                result[multiple] = False
    return result

def primelist(cap):
    tf = tf_primelist(cap)
    primelist = []
    for i in range(3,cap+1):
        if tf[i]:
            primelist.append(i)
    return primelist

def is_prime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True
    for i in [2,3]:
        if n % i == 0:
            return False
    for i in range(6,int(n**.5), 6):
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
    return True

best_prime = (None,0)

primes = primelist(1000000)


for i in range(len(primes)):
    total = 0
    j = i
    while total < 1000000:
        try:
            total += primes[j]
        except IndexError:
            break
        j += 1
        if is_prime(total):
            if j - i > best_prime[1]:
                best_prime = (total, j - i)


print(best_prime[0])






