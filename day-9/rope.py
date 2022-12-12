import logging
# logging.basicConfig(level=logging.DEBUG)

class vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, othervec):
        return vector( self.x + othervec.x, self.y + othervec.y)
    
    def __sub__(self, othervec):
        return vector(self.x - othervec.x, self.y - othervec.y)
    
    def __repr__(self):
        return f"vector x:{self.x}, y:{self.y}"
    
    def __hash__(self):
        return hash((self.x, self.y))

    def copy(self):
        return vector(self.x, self.y)
    
    def delta(self, othervec):
        return abs(self.x - othervec.x) + abs(self.y - othervec.y)
    
    def normalize(self):
        if self.x != 0:
            self.x = self.x // abs(self.x)
        if self.y != 0:
            self.y = self.y // abs(self.y)

rope = [
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    vector(0, 0),
    ]
directions = {
    "U": vector(0, 1),
    "D": vector(0, -1),
    "L": vector(-1, 0),
    "R": vector(1, 0)
}
trail = set()
moves = 0

def render():
    global rope
    head = rope[0]
    tail = rope[-1]
    global trail
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    for k in range(len(rope)):
        maxx = rope[k].x if rope[k].x > maxx else maxx
        minx = rope[k].x if rope[k].x < minx else minx
        maxy = rope[k].y if rope[k].y > maxy else maxy
        miny = rope[k].y if rope[k].y < miny else miny
    for k in trail:
        maxx = k.x if k.x > maxx else maxx
        minx = k.x if k.x < minx else minx
        maxy = k.y if k.y > maxy else maxy
        miny = k.y if k.y < miny else miny
    width = (maxx - minx) + 1
    height = (maxy - miny) + 1
    canvas = []
    for i in range(height):
        canvas.append(["."]*width)
    for i in trail:
        canvas[i.y+abs(miny)][i.y+abs(minx)] = "#"
    for k in range(len(rope)):
        canvas[rope[k].y+abs(miny)][rope[k].x+abs(minx)] = f"{k}" 
    for row in canvas:
        print("".join(row))
    print(" ")

def move(direction:str, knot: vector):
    return knot + directions[direction]

# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
# Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
# You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.
def update(head, tail):
    delta = head - tail
    if abs(delta.y) > 1 or abs(delta.x) > 1:
        delta.normalize()
        tail = tail + delta
    return tail

def move_rope(direction):
    global rope
    rope[0] = move(direction, rope[0])
    logging.debug(f"moving head segment {direction}")
    for i in range(len(rope) - 1):
        logging.debug(f"updating rope segment {rope[i]},{rope[i+1]}")
        rope[i+1] = update(rope[i], rope[i+1])
        logging.debug(f"updated rope segment {rope[i]},{rope[i+1]}")
    logging.debug(rope)

def read_instructions(instruction_file: str):
    with open(instruction_file) as instructions:
        for instruction in instructions:
            parts = instruction.strip().split(' ')
            direction = parts[0]
            count = int(parts[1])
            for x in range(count):
                move_rope(direction)
                trail.add((rope[-1].x,rope[-1].y))



read_instructions("day-9/input.txt")
print(len(trail))
print(moves)
