with open("./input.in") as fin:
    data = fin.read().strip().split()

data_leng = len(data)

for i in range(0, 3):
    line = data[i]
    line_length = len(line)//2
    first_half = set(line[:line_length])
    print(first_half)
