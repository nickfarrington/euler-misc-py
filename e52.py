def check(n):
    result = True
    toCompare = sorted(str(n))
    for i in range(2,7):
        if toCompare != sorted(str(n * i)):
            result = False
            break
    return result
        
if __name__ == "__main__":
    digs = 1
    toBreak = False

    while True:
        for i in range(10 ** digs, (10 ** (digs + 1)) // 6):
            if check(i):
                toBreak = True
                break
        if toBreak:
            break
        digs += 1
##        print(digs)
    print(i)
