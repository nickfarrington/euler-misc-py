import operator, functools

def load_num(input_file):
    result = ""
    with open(input_file) as f:
        for line in f.readlines():
            result += line.strip()
    return result

num = load_num("e8_digits.txt")
best_running_product = 0

for i in range(len(num) - 13 + 1):
    product = functools.reduce(operator.mul, [int(i) for i in num[i:i+13]])
    if product > best_running_product:
        best_running_product = product


print(best_running_product)
