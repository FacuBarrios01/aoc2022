with open("/home/facu/Documents/code/python/aoc2022/day1/input.in") as fin:
    data = fin.readlines()

N = len(data)
max = 0
cals = 0

for i in range(0, N):
    if data[i] != "\n":
        cals += int(data[i].strip())
    elif cals > max: 
        max = cals
        cals = 0
    else:
        cals = 0

print(max)