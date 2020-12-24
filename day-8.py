def simulate(instr):
    acc = 0
    pc = 0
    visited = [False] * len(instr)
    while not visited[pc]:
        if len(instr[pc]) == 0:
            return (acc, True)
        visited[pc] = True
        if instr[pc].split()[0] == "acc":
            acc += int(instr[pc].split()[1])

        if instr[pc].split()[0] == "jmp":
            incr = int(instr[pc].split()[1])
            pc += incr
        else:
            pc += 1
    return (acc, False)

instr = open("day-8.in", "r").read().split("\n")
print(simulate(instr)[0])


acc = 0
pc = 0
for change in range(0, len(instr)):
    origLine = instr[change]
    if instr[change].split()[0] == "nop":
        instr[change] = "jmp" + " " + instr[change].split()[1]
    elif instr[change].split()[0] == "jmp":
        instr[change] = "nop" + " " + instr[change].split()[1]
    simRes = simulate(instr)
    if simRes[1]:
        print(simRes[0])
        break
    instr[change] = origLine

