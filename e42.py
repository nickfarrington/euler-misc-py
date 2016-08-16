def load_words(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            words = [word[1:-1] for word in line.split(',')]

    return words

def enum_tris(cap):
    l = []
    n = 1
    while True:
        tri = n * (n + 1) // 2
        if tri > cap:
            break
        else:
            n += 1
            l.append(tri)

    return l


words = load_words("p042_words.txt")

longest = 0
for word in words:
    if len(word) > longest:
        print(word)
        longest = len(word)

tris = set(enum_tris(longest*26))#highest value is the longest word with z as all chars

def in_ord_list(l, i): #Binary search, since 'in' is less efficient
                        #TODO make this work. I smell a fencepost
    low, high = 0, len(l)
    while (low - high) ** 2 > 1:
        guess = (low + high) // 2
        answer = l[guess]
        print(low,high,guess)
        if i == answer:
            return True
        elif i < answer:
            high = guess
        else:
            low = guess
    return False

def get_word_val(word):
    total = 0
    for char in word:
        total += ord(char) % 32 #Convert to ASCII value modulo 32, works both cases

    return total 

count = 0
for word in words:
    if get_word_val(word) in tris:
        count += 1
print(count)
