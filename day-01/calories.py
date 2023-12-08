elves = {}
elf_count = 1
cal_total = 0

with open('input.txt') as input :
    for line in input:
        if line == "\n":
            elves[elf_count] = cal_total
            cal_total=0
            elf_count += 1
        else:
            cal_total += int(line)

# part 1
elves_by_cal = sorted(elves, key=elves.get, reverse=True)
print(elves[elves_by_cal[0]])

# part 2
top3 = 0
for i in elves_by_cal[0:3]:
    print(i, elves[i])
    top3 += elves[i]

print(top3)