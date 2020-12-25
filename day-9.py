import sys

input = open("day-9.in", "r").read().split()
input = [int(i) for i in input]
preamble = 25

vals = {}
for i in range(0, len(input)):
    for j in range(i + 1, len(input)):
        vals[input[i] + input[j]] = (i, j)

invalid = -1

ind = preamble
while ind < len(input):
    if input[ind] not in vals.keys() or ind - vals[input[ind]][0] > preamble or ind - vals[input[ind]][1] > preamble:
        invalid = input[ind]

        break
    ind += 1

print(invalid)

for i in range(0, len(input)):
    sum = 0
    smallest = invalid
    largest = 0
    for j in range(i, len(input)):
        if input[j] > largest:
            largest = input[j]
        if input[j] < smallest:
            smallest = input[j]
        sum += input[j]
        if sum == invalid:
            print(smallest + largest)
            sys.exit(0)
        if sum > invalid:
            break
