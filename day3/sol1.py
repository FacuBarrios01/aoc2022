import string

with open("./input.in") as fin:
    data = fin.read().strip().split()

data_leng = len(data)
sum = 0

def calculate_points(letter):
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    points = dict(zip(letters, range(1, 53)))
    return points.get(letter)


for i in range(0, data_leng):
    line = data[i]
    line_length = len(line)//2
    first_half = set(line[:line_length])
    match = first_half.intersection(line[line_length:]).pop()
    sum += calculate_points(match)
print(sum)