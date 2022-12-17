import logging
import math
logging.basicConfig(level=logging.DEBUG)

class node():
    def __init__(self,x,y,parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        
    def __repr__(self):
        return f'{self.x} {self.y}'
    
    def __eq__(self, o):
        if self.x == o.x and self.y == o.y:
            return True
        return False

    def __eq__(self, o: tuple):
        if self.x == o[0] and self.y == o[1]:
            return True
        return False

    def get_distance(self, dest):
        dx = self.x - p2[0]
        dy = self.y - p2[1]
        return dx ** 2 + dy ** 2

def get_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx ** 2 + dy ** 2

def make_heightmap(filelocation: str):
    start_x,start_y,dest_x,dest_y = 0,0,0,0
    heightmap = []
    with open(filelocation) as f:
        for y, line in enumerate(f):
            heightmap.append([])
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start_x = x
                    start_y = y
                    char = 'a'
                if char == "E":
                    dest_x = x
                    dest_y = y
                    char = 'z'
                heightmap[y].append(char)
    return {"heightmap": heightmap,
            "start": (start_x, start_y),
            "dest": (dest_x,dest_y)}


def get_moves_diagonal(x,y, heightmap):
    value = heightmap[y][x]
    max_x = len(heightmap[0])
    max_y = len(heightmap)
    min_x = 0
    min_y = 0
    possible_moves = []
    for pos_x in [x-1, x, x+1]:
        for pos_y in [y-1, y, y+1]:
            if max_x > pos_x > min_x and max_y > pos_y > min_y:
                if ord(heightmap[pos_y][pos_x]) - ord(heightmap[y][x]) <= 1:
                    possible_moves.append((pos_x,pos_y))
    return possible_moves


def print_map(heightmap,position):
    heightmap[position[1]][position[0]] = 'X'
    for y in heightmap:
        print(y)


def get_moves(x,y, heightmap):
    value = heightmap[y][x]
    max_x = len(heightmap[0])
    max_y = len(heightmap)
    min_x = -1
    min_y = -1
    possible_moves = []
    for pos_x,pos_y in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
            if max_x > pos_x > min_x and max_y > pos_y > min_y:
                logging.debug(f'height diff of step {ord(heightmap[pos_y][pos_x]) - ord(heightmap[y][x])}')
                if ord(heightmap[pos_y][pos_x]) - ord(heightmap[y][x]) <= 1:
                    possible_moves.append((pos_x,pos_y))
    return possible_moves





# def move_forward(position, destination, heightmap):
#     if position == destination:
#         return position
#     moves = get_moves(position[0], position[1], heightmap)
#     moves.sort(key=lambda x : self.get_distance(destination),reverse=True)
#     for move in moves:
#         return  [position, move_forward(position, destination, heightmap)]


starting_conditions = make_heightmap("day-12/input.txt")
heightmap = starting_conditions['heightmap']
current_position = starting_conditions['start']
destination = starting_conditions['dest']
# print(move_forward(current_position, destination, heightmap))
visited = []
path = []
to_visit = []
to_visit.append(node(current_position[0], current_position[1]))
while len(to_visit) > 0 and current_position != destination:
    current_position = to_visit.pop()
    visited.append(current_position)
    moves = get_moves(current_position.x, current_position.y, heightmap)
    moves.sort(key=lambda x : get_distance(x, destination),reverse=True)
    for move in moves:
        if move not in visited:
            to_visit.append(node(move[0], move[1], current_position))
    logging.debug(f'current position: {current_position}')
    logging.debug(f'visited {visited}')

def get_path(n, path):
    if n.parent is None:
        path.append(n)
        return path
    path.append(n)
    return get_path(n.parent, path)


path = get_path(current_position, [])
print(len(path)) 

