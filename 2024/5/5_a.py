


input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

[rules, prints] = input.split("\n\n")

rules = [x.split("|") for x in rules.split("\n")]
prints = [x.split(",") for x in prints.split("\n")]

print(prints)

results = [True] * len(prints)

def valid(line: list[str], rule:list[str]):
    [a,b] = rule
    print(line, rule)
    if not (a in line and b in line):
        return True
    
    pos_a = line.index(a)
    pos_b = line.index(b)
    return pos_b > pos_a

correct_lines = []
for line in prints:
    if all([valid(line, rule) for rule in rules]):
        correct_lines.append(line)

print(correct_lines)

sum = 0
for i, line in enumerate(correct_lines):
    sum += int(line[len(line)//2])
        
print(sum)