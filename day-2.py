numValidPasswords1 = 0
numValidPasswords2 = 0
with open("day-2.in", "r") as input:
    for line in input:
        fields = line.split(' ')
        minMax = fields[0].split("-")
        min = int(minMax[0])
        max = int(minMax[1])
        char = fields[1][0]
        password = fields[2]

        ct = 0
        for i in range(0, len(password)):
            if password[i] == char:
                ct += 1
            if ct > max:
                break

        if ct >= min and ct <= max:
            numValidPasswords1 += 1

        if (password[min - 1] == char and password[max - 1] != char) or (password[min - 1] != char and password[max - 1] == char):
            numValidPasswords2 += 1
print(numValidPasswords1)
print(numValidPasswords2)
