with open("day2/input.in") as fin:
    data = fin.read().strip().split("\n")

score = 0

for match in data:
    opponents = match.split()
    match opponents[1]:
        case 'X':
            #Rock(X):
            # A Draw +3
            # B loss +0
            # C Win  +6
            
            score += 1
            match opponents[0]:
                case 'A': score += 3
                case 'B': score += 0
                case 'C': score += 6

        case 'Y':
            #Paper(Y):
            # A win  +6
            # B draw +3
            # C loss +0

            score += 2
            match opponents[0]:
                case 'A': score += 6
                case 'B': score += 3
                case 'C': score += 0
        case 'Z':
            #Scissors(Z):
            #  A loss +0
            #  B win  +6
            #  C draw +3

            score += 3
            match opponents[0]:
                case 'A': score += 0
                case 'B': score += 6
                case 'C': score += 3

print(score)