def is_palindrome(n):
    s = str(n)
    result = True
    while len(s) > 1:
        if s[0] != s[-1]:
            result = False
            break
        else:
            s = s[1:-1]
    return result

def advance(n):
    return n + int(str(n)[::-1])

def lychrel_seq(n, maxiters = 50, verbose = False):
    current = n
    for i in range(maxiters):
        if verbose:
            print(current)
        current = advance(current)
        if is_palindrome(current):
            break
        elif i == maxiters - 1:
            i = None

    return i


if __name__ == "__main__":
    lychrels = 0

    for i in range(1,10001):
        a = lychrel_seq(i)
        if a == None:
            lychrels += 1

    print(lychrels)
