input = open("day-9.in", "r").read().split()
input = [int(i) for i in input]
preamble = 25

vals = {}
for i in range(0, len(input)):
    for j in range(i + 1, len(input)):
        vals[input[i] + input[j]] = (i, j)

ind = preamble
while ind < len(input):
    if input[ind] not in vals.keys() or ind - vals[input[ind]][0] > preamble or ind - vals[input[ind]][1] > preamble:
        print(input[ind])

        break
    ind += 1