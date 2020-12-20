def solve(sum, ignore):
    map = [None] * (sum + 1)
    for i in range(0, len(input)):
        if i != ignore and int(input[i]) < len(map):
            if map[int(input[i])]:
                return int(input[i]) * (sum - int(input[i]))
            map[sum - int(input[i])] = True
    return -1

input = open("day-1.in", "r").read().splitlines()
print(solve(2020, -1))


for i in range(0, len(input)):
    #print(input[i], 2020 - int(input[i]))
    sol = solve(2020 - int(input[i]), i)
    if sol != -1:
        print(sol * int(input[i]))
        break
