max = 0
bucket = [False] * 1032
with open("day-5.in", "r") as input:
    for line in input:
        floor = 0
        ceil = 128
        for i in range(0, 7):
            mid = int((ceil - floor) / 2) + floor
            if line[i] == "F":
                ceil = mid
            elif line[i] == "B":
                floor = mid
        row = int((ceil - floor)/ 2) + floor
        floor = 0
        ceil = 8
        for i in range(7, 10):
            mid = int((ceil - floor) / 2) + floor
            if line[i] == "L":
                ceil = mid
            elif line[i] == "R":
                floor = mid
        col = int((ceil - floor)/ 2) + floor
        id = row * 8 + col
        if id > max:
            max = id
        bucket[id] = True
print(max)
for i in range(1, len(bucket) - 1):
    if not bucket[i] and bucket[i - 1] and bucket[i + 1]:
        print(i)
        break
