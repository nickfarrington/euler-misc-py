import math

def sumFact(n):
    digits = str(math.factorial(n))
    count = 0
    for digit in digits: count += int(digit)
    return count

if __name__ == "__main__":
    print(sumFact(100))
