validPassports1 = 0
validPassports2 = 0
key = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
input = open("day-4.in", "r").read().split("\n\n")
for line in input:
    passportFields = line.split()
    ctFields = [False] * 7
    for entry in passportFields:
        field = entry.split(":")[0]
        param = entry.split(":")[1]
        if field in key:
            if field == "byr" and int(param) >= 1920 and int(param) <= 2002:
                ctFields[key.index(field)] = True
            elif field == "iyr"  and int(param) >= 2010 and int(param) <= 2020:
                ctFields[key.index(field)] = True
            elif field == "eyr"  and int(param) >= 2020 and int(param) <= 2030:
                ctFields[key.index(field)] = True
            elif field == "hgt":
                if param[-2:] == "cm":
                    if int(param[0:-2]) >= 150 and int(param[0:-2]) <= 193:
                        ctFields[key.index(field)] = True
                elif param[-2:] == "in":
                    if int(param[0:-2]) >= 59 and int(param[0:-2]) <= 76:
                        ctFields[key.index(field)] = True
            elif field == "hcl" and len(param) == 7 and param[0] == "#":
                ctFields[key.index(field)] = True
                for char in param[1:]:
                    if char not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
                        ctFields[key.index(field)] = False
            elif field == "ecl" and param in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                ctFields[key.index(field)] = True
            elif field == "pid" and len(param) == 9:
                ctFields[key.index(field)] = True






    indicator = True
    print(passportFields)
    for bool in ctFields:
        print(bool)
        indicator = indicator and bool

    if indicator:
        validPassports1 += 1
print(validPassports1)
