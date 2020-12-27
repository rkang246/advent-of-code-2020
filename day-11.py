input = open("day-11.in").read().splitlines()
seats = [list(line) for line in input]
tempSeats = [list(line) for line in input]

def printState(seats):
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            print(seats[i][j], sep='', end='')
        print()
    print()
    print()

def adjacentOccupied(i, j, seats):
    rLower = (i - 1) if i != 0 else 0
    rUpper = (i + 1) if i < len(seats) - 1 else len(seats) - 1
    cLower = (j - 1) if j != 0 else 0
    cUpper = (j + 1 if j < len(seats[0]) - 1 else len(seats[0]) - 1)

    adjOcc = 0
    for r in range(rLower, rUpper + 1):
        for c in range(cLower, cUpper + 1):
            if (r != i or c != j) and seats[r][c] == "#":
                adjOcc += 1

    return adjOcc


while (True):

    diffFlag = False
    for i in range(0, len(seats)):
        for j in range(0, len(seats[0])):
            if (seats[i][j] == "."):
                continue

            adjOcc = adjacentOccupied(i, j, seats)
            if adjOcc == 0:
                tempSeats[i][j] = "#"
                if tempSeats[i][j] != seats[i][j]:
                    diffFlag = True
            elif adjOcc >= 4:
                tempSeats[i][j] = "L"
                if tempSeats[i][j] != seats[i][j]:
                    diffFlag = True
    occ = 0
    for i in range(0, len(seats)):
        for j in range(0, len(seats[0])):
            seats[i][j] = tempSeats[i][j]
            if seats[i][j] == "#":
                occ += 1

    if (not diffFlag):
        print(occ)
        break





