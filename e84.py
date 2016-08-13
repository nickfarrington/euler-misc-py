# 2016.06.22 21:44:58 EDT
#Embedded file name: e84.py
import random, pylab
ccDeck = chDeck = list(range(12))
random.shuffle(ccDeck)
random.shuffle(chDeck)

def rollDice():
    a, b = random.choice(list(range(1, 5))), random.choice(list(range(1, 5)))
    return (a + b, a == b)


def nextRailroad(currentSquare):
    return (currentSquare + 4 - (currentSquare + 4) % 10 + 5) % 40


def nextUtil(currentSquare):
    if currentSquare <= 12 or currentSquare > 28:
        return 12
    else:
        return 28


def commChest(currentSquare):
    global ccDeck
    card = ccDeck[0]
    ccDeck = ccDeck[1:] + [card]
    if card == 0:
        return 0
    if card == 1:
        return 10
    return currentSquare


def chance(currentSquare):
    global chDeck
    card = chDeck[0]
    chDeck = chDeck[1:] + [card]
    if card == 0:
        return 0
    if card == 1:
        return 10
    if card == 2:
        return 11
    if card == 3:
        return 24
    if card == 4:
        return 39
    if card == 5:
        return 5
    if card in (6, 7):
        return nextRailroad(currentSquare)
    if card == 8:
        return nextUtil(currentSquare)
    if card == 9:
        return currentSquare - 3
    return currentSquare


def doTurn(start, doubles = 0):
    roll = rollDice()
    position = start + roll[0]
    position %= 40
    if doubles == 3:
        return 10
    if roll[1] == True:
        return doTurn(start, doubles + 1)
    if position in (7, 22, 36):
        return chance(position)
    if position in (2, 17, 33):
        return commChest(position)
    if position == 30:
        return 10
    return position % 40


def runGame(numTurns = 500):
    freqs = {}
    pos = 0
    for i in range(40):
        freqs[i] = 0

    for i in range(numTurns):
        pos = doTurn(pos)
        freqs[pos] += 1

    return freqs

def sortedPlot(l):
    pairs = []
    for pair in enumerate(l):
        pairs.append(pair)
    pairs = sorted(pairs,key=lambda pair: pair[1])
##    xs,ys = [], []
    for pair in pairs:
        print(str(pair[0]), str(float(pair[1])/float(500)) + "%")
##        xs.append(pair[0]); ys.append(pair[1])
##    fig = pylab.figure()
##    ax = fig.add_subplot(111)
##    ax.plot(ys)
##    ax.set_xticklabels(xs)
##    pylab.show()

if __name__ == '__main__':
    freqs = [0] * 40
    for i in range(100):
        newFreqs = runGame()
        for i in range(40):
            freqs[i] += newFreqs[i]
    sortedPlot(freqs)


##    pylab.bar(range(0,40),freqs)
##    pylab.show()








