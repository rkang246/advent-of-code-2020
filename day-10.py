input = open("day-10.in", "r").read().split()
jolts = [int(i) for i in input]

jolts.sort()

oneDiff = 0
threeDiff = 1

prevJolt = 0
for i in range(0, len(jolts)):
    if (jolts[i] - prevJolt == 1):
        oneDiff += 1
    elif (jolts[i] - prevJolt == 3):
        threeDiff += 1
    prevJolt = jolts[i]
print(oneDiff * threeDiff)

memo = [0] * (jolts[len(jolts) - 1] + 1)
memo[0] = 1
for i in range(0, len(jolts)):
    a = jolts[i] - 3
    b = jolts[i] - 2
    c = jolts[i] - 1
    memo[jolts[i]] = (0 if a < 0 else memo[a]) + (0 if b < 0 else memo[b]) + (0 if c < 0 else memo[c])
print(memo[len(memo) - 1])

