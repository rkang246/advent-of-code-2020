acc = 0
pc = 0
instr = open("day-8.in", "r").read().split("\n")
visited = [False] * len(instr)
while not visited[pc]:
    visited[pc] = True
    if instr[pc].split()[0] == "acc":
        acc += int(instr[pc].split()[1])

    if instr[pc].split()[0] == "jmp":
        pc += int(instr[pc].split()[1])
    else:
        pc += 1
print(acc)

#todo part 2