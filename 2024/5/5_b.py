from pathlib import Path
input = Path("./input.txt").read_text()


[rules, prints] = input.split("\n\n")

rules = [x.split("|") for x in rules.split("\n")]
prints = [x.split(",") for x in prints.split("\n")]

results = [True] * len(prints)

def valid(line: list[str], rule:list[str]):
    [a,b] = rule
    if not (a in line and b in line):
        return True
    
    pos_a = line.index(a)
    pos_b = line.index(b)
    return pos_b > pos_a



wrong_lines = []
for i, line in enumerate(prints):
    if False in [valid(line, rule) for rule in rules]:
            wrong_lines.append(line)


print(len(wrong_lines))

def sort_line(line: list):
    relevant_rules = []
    for [a,b] in rules:
        if a in line and b in line:
            relevant_rules.append([a,b])

    found_invalid = True
    while found_invalid:
        found_invalid = False
        for [a,b] in relevant_rules:
            pos_a = line.index(a)
            pos_b = line.index(b)
            if pos_a > pos_b:
                found_invalid = True
                line[pos_a], line[pos_b] = line[pos_b], line[pos_a]
    
    return line

sorted_lines = []

for line in wrong_lines:
    sorted_lines.append(sort_line(line))

print(sorted_lines)
print(len(sorted_lines))

sum = 0
for i, line in enumerate(sorted_lines):
    sum += int(line[len(line)//2])
        
print(sum)