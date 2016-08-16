def load_words(input_file):
    with open(input_file) as f:
        return set(word[1:-1] for word in f.readline().strip().split(","))

def load_cipher(input_file):
    with open(input_file) as f:
        return [int(num) for num in f.readline().strip().split(",")]

good_words = load_words("p042_words.txt")
cipher = load_cipher("p059_cipher.txt")


codes = []
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            ac = chr(a)
            bc = chr(b)
            cc = chr(c)
            codes.append(ac + bc + cc)

def decrypt_cipher(pw, cipher):
    response = []
    for i in range(len(cipher)):
        xorer = ord(pw[(i + 1) % len(pw)])
        response += chr(cipher[i] ^ xorer)
    return "".join(response)

def get_tot_word_val(s):
    return sum([ord(c) for c in s])

best_accuracy = 0
best_words = 0

for code in codes:
    words = decrypt_cipher(code,cipher).split(" ")
    if len(words) < 20:
        continue
    accuracy = 0
    for word in words:
        if word.strip('!,?." ()').upper() in good_words:
            accuracy += 1
        elif word.strip("1234567890") == "":
            accuracy += 1
    accuracy /= len(words)

    if accuracy >= .60:
        best_accuracy,best_words = accuracy, words

print("Best Fit\n--------")
print(" ".join(best_words))

print(get_tot_word_val(" ".join(best_words)))











