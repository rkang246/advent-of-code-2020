def solve(right, down):
    r = 0
    c = 0
    trees = 0
    while r < len(input):
        if input[r][c] == "#":
            trees += 1

        r += down
        c += right
        if (c >= len(input[0])):
            c -= len(input[0])
    return trees

input = open("day-3.in", "r").read().splitlines()
print(solve(3, 1))

print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
