from sys import setrecursionlimit
setrecursionlimit(10000)

britcoins = [200,100,50,20,10,5,2] #1p coins are considered run off
uscoins = [25,10,5]

def num_possibilities(amount, coins, memo = {}, firstTime = True):
    if firstTime == True:
        memo = {}

    total = 0

    for i in range(len(coins)):
        if amount - coins[i] >= 0:
            try:
                extra = memo[amount - coins[i], coins[i]]
            except:
                extra = num_possibilities(amount-coins[i], coins[i:],memo,False)
                memo[amount - coins[i], coins[i]] = extra
            total += extra
            #Only allow coins equal to or smaller than last denom
            #This prevents redundant solutions & inf. recursion

    return total + 1 #Account for using all remaining 1p coins and none larger

if __name__ == "__main__":
    print(num_possibilities(200,britcoins))
    #Just so you know, this does way more than Euler asks
