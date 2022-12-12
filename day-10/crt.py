# Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:
#
#    addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
#    noop takes one cycle to complete. It has no other effect.
#
# The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.


def add(value):
    global x
    global time
    time += 2
    x += value

def noop():
    global time
    time += 1

def get_sums():
    global values
    found = []
    for i in range(20, time, 40):
        if i in values:
            found.append(values[i]*i)
        else:
            found.append(values[i-1]*i)
        print(i, found[-1])
    return sum(found)
            
def get_pixels():
    output = ""
    for i in range(1, 240):
        char = "."
        if i in values:
            if i%40 - 1 <= values[i] <= i%40 + 1:
                char = "#"
        output += char
    for x in range(0, 240, 40):
        print(output[x:x+41])


x = 1
time = 1
values = {1: 1}

with open("day-10/input.txt") as instructions:
    for instruction in instructions:
        if instruction.strip()[0] == 'a':
            add(int(instruction.strip().split( )[1]))
            values[time-1] = x
            values[time] = x
        else:
            noop()
            values[time] = x

print(values)
print(get_pixels())