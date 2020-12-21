map = {}
dfs = {}
cap = {}
with open("day-7.in", "r") as input:
    for rule in input:
        key = rule.split("contain")[0].strip()[:rule.split("contain")[0].index("bag") - 1]
        pair = (rule.split("contain")[1]).split(",")
        map[key] = []
        dfs[key] = 0
        cap[key] = []
        for elt in pair:
            map[key].append(elt.strip()[2:elt.index("bag") - 2])
            ct = elt.strip().split()[0]
            cap[key].append(int(ct) if ct.isnumeric() else 0)

def solve(bag):
    if bag not in dfs.keys():
        return 0

    if dfs[bag] != 0:
        return dfs[bag]
    if "shiny gold" in map[bag]:
        dfs[bag] += 1
        return 1

    for subbag in map[bag]:
        ret = solve(subbag)
        if ret != 0:
            dfs[bag] += 1
            return 1 + ret
    return 0

sol = 0
for bag in map.keys():
    slv = solve(bag)
    if slv != 0:
        sol += 1
print(sol)

def solve2(bag):
    ct = 0
    for i in range(0, len(map[bag])):
        if map[bag][i] in map.keys():
            ct += cap[bag][i]
            ct += cap[bag][i] * solve2(map[bag][i])
    return ct

print(solve2("shiny gold"))


