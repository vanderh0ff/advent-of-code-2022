import logging
import math
logging.basicConfig(level=logging.DEBUG)


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


def get_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)



def move_forward(position, destination, heightmap):
    if position == destination:
        return position
    moves = get_moves(position[0], position[1], heightmap)
    moves.sort(key=lambda x : get_distance(x, destination),reverse=True)
    for move in moves:
        return  [position, move_forward(position, destination, heightmap)]


starting_conditions = make_heightmap("day-12/input.txt")
heightmap = starting_conditions['heightmap']
current_position = starting_conditions['start']
destination = starting_conditions['dest']
print(move_forward(current_position, destination, heightmap))
# visited = []
# path = []
# to_visit = []
# to_visit.append(current_postion)
# while len(to_visit) > 0 and current_postion != destination:
#     current_postion = to_visit.pop()
#     moves = get_moves(current_postion[0], current_postion[1], heightmap)
#     visited.append(current_postion)
#     moves.sort(key=lambda x : get_distance(x, destination),reverse=True)
#     for move in moves:
#         if move not in visited:
#             to_visit.append(move)
#     logging.debug(f'current position: {current_postion}')
#     logging.debug(f'visited {visited}')
#     print_map(heightmap,current_postion )
# print(len(visited))
