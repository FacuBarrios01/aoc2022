with open("/home/facu/Documents/code/python/aoc2022/day1/input.in") as fin:
    data = fin.readlines()

N = len(data)
max = 0
cals = 0
cals_list = []

for i in range(0, N):
    if data[i] != "\n":
        cals += int(data[i].strip())
    elif cals > max: 
        cals_list.append(cals)
        cals = 0
    else:
        cals = 0

for i in sorted(cals_list, reverse=True)[:3]:
    max += i

print(max)