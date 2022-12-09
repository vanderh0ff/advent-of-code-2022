import re

def parse_map(m: list, stack_width = 4):
    m.reverse()
    supply_stacks = []
    stack_map_len = len(m[0])
    num_stacks = stack_map_len//stack_width
    for x in range(num_stacks):
        supply_stacks.append([])
        for line in m[1:]:
            if line[x*stack_width + 1] != " ":
                supply_stacks[x].append(line[x*stack_width+1])
    return supply_stacks

def execute_move(instructions: str, supply_map: list):
    num_to_move, source, destination = list(map(int, re.findall(r'\d+', instructions)))
    for i in range(num_to_move):
        supply_map[destination-1].append(supply_map[source-1].pop())

def execute_crate_move(instructions: str, supply_map: list):
    num_to_move, source, destination = list(map(int, re.findall(r'\d+', instructions)))
    source -= 1
    destination -= 1
    supply_map[destination] += supply_map[source][-num_to_move:]
    supply_map[source] = supply_map[source][0:-num_to_move]


def build_map(supply_map: list):
    for i in supply_map:
        print(i)

with open("day-5/input.txt") as inputs:
    current_supply_stack_map = []
    l = inputs.readline()
    while l != "\n":
        current_supply_stack_map.append(l)
        l = inputs.readline()
    supply_map = parse_map(current_supply_stack_map)
    l = inputs.readline()
    while l != "\n" and l != "":
        execute_crate_move(l, supply_map)
        l = inputs.readline()
    build_map(supply_map)

