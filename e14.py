def collatz(start, memo = {}):
    assert start > 0
    count = 0
    n = start
    if n == 1:
        return [1]

    if n%2 == 0:
        nextTerm = n / 2
    else:
        nextTerm = 3 * n + 1

    try:
        path = [start] + memo[nextTerm]
    except KeyError:
        path = [start] + collatz(nextTerm)
        memo[nextTerm] = path[1:]
    return path
    
    


if __name__ == "__main__":
    best = [None,0]
    for i in range(1,1000000):
        if i % 100000 == 0:
            print("{} out of 1 million iterations completed".format(i))
        sequence = collatz(i)
        if len(sequence) > best[1]:
            best = [i,len(sequence)]
    print("The longest Goldbach sequence is:" + str(best[0]))
