def load_words(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            return [word[1:-1] for word in line.split(",")]

words = load_words("p022_names.txt")

def get_let_val(word):
    return sum([ord(char) % 32 for char in word])

print(sum((i + 1) * get_let_val(word) for i, word in enumerate(sorted(words))))
