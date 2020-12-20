input = open("day-6.in", "r").read().split("\n\n")
sum1 = 0
sum2 = 0
for line in input:
    bucket = [0] * 26
    groupCt = 1
    for char in line:
        if not char.isspace():
            bucket[ord(char) - ord('a')] += 1
        else:
            groupCt += 1
    print(line, ":")
    print(groupCt, "members")
    for indicator in bucket:
        if indicator != 0:
            sum1 += 1
        if indicator == groupCt:
            print("adding")
            sum2 += 1
        print(indicator)
print(sum1)
print(sum2)
