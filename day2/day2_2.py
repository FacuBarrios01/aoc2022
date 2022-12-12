with open("day2/input.in") as fin:
    data = fin.read().strip().split("\n")

score = 0

for match in data:
    opponents = match.split()
    match opponents[0]:
        case 'A':
            #Rock(A):  
            # X loss Scissors   +0 +3 = 3
            # Y Draw rock       +3 +1 = 4
            # Z Win  paper      +6 +2 = 8
            match opponents[1]:
                case 'X': score += 3
                case 'Y': score += 4
                case 'Z': score += 8

        case 'B':
            #Paper(B):
            # X loss rock       +0 +1 = 1
            # Y draw Paper      +3 +2 = 5
            # Z win  Scissors   +6 +3 = 9
            
            match opponents[1]:
                case 'X': score += 1
                case 'Y': score += 5
                case 'Z': score += 9
        case 'C':
            #Scissors(C):
            # X loss Paper      +0  +2 = 2
            # Y draw Scissors   +3  +3 = 6
            # Z win  rock       +6  +1 = 7
            match opponents[1]:
                case 'X': score += 2
                case 'Y': score += 6
                case 'Z': score += 7

print(score)