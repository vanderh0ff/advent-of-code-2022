"""
this program sorts rucsacks
each rucksack has two compartments
all items of a type are ment to go in one compartment per rucksack
each rucksack is represented as one string, the compartment devides at the mid point

elves are also in groups of three each having common items
you must detirmine the itmes and priority of the group arrangemnt
"""



# rucksacks = ["vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"
# ]

def split_sack(rucksack: str):
    mid_point = len(rucksack)//2
    return rucksack[0:mid_point], rucksack[mid_point:]

def find_common(c1: str, c2: str):
    common = []
    for item in c1:
        if item in c2 and item not in common:
            common.append(item)
    return common

def get_priority(common):
    s = 0
    for item in common:
        value = ord(item)
        if value >= 97:
            value -= 96
        else:
            value -= 38 
            # ord of A is 65, but we want the value to be 26 grater than its position
        s += value
    return s

def get_rucksac_priorities():
    priority_rearrangement = 0
    with open("input.txt") as rucksacks:
        for r in rucksacks:
            c1, c2 = split_sack(r)
            priority_rearrangement += get_priority(find_common(c1, c2))
    print(priority_rearrangement)

def find_group_item(ruks: list):
    e1, e2, e3 = ruks[0], ruks[1], ruks[2]
    for item in e1:
        if item in e2 and item in e3:
            return item

def get_group_priorities():
    group_priorities = 0
    with open("input.txt") as groups:
        ruks = ["", "", ""]
        for line, rucksack in enumerate(groups):
            ruks[line%3] = rucksack
            if line%3 == 2:
                group_item = find_group_item(ruks)
                group_priorities += get_priority(group_item)
    return group_priorities

print(get_group_priorities())




