import logging
import heapq
import copy
import os
from termcolor import colored

from node import Node, Position
logging.basicConfig(level=logging.DEBUG)

def get_path(n, path):
    if n.parent is None:
        path.append(n)
        return path
    path.append(n)
    return get_path(n.parent, path)

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
            "start": Position(x=start_x, y=start_y, z=1),
            "dest": Position(x=dest_x, y=dest_y, z=26)}


def print_map(heightmap,position):
    heightmap[position.x,position.y] = 'X'
    for y in heightmap:
        print(y)

def print_path(current, path):
    global heightmap
    hm = copy.deepcopy(heightmap)
    for node in path:
        hm[node.position.y][node.position.x] = colored("*", 'red')
    hm[current.position.y][current.position.x] = colored('X', 'red')
    for line in hm:
        print("".join(line))
        



def get_possible_moves(current):
    global heightmap
    global visited
    global destination
    max_x = len(heightmap[0])
    max_y = len(heightmap)
    min_x = -1
    min_y = -1
    possible_moves = []
    for pos_x,pos_y in [(current.position.x-1, current.position.y),
                        (current.position.x, current.position.y-1),
                        (current.position.x, current.position.y+1),
                        (current.position.x+1, current.position.y)
                        ]:
        if max_x > pos_x > min_x and max_y > pos_y > min_y:
            height = ord(heightmap[pos_y][pos_x] )+1 - ord('a')
            if height <= current.position.z + 1:
                pm = Node(Position(pos_x,pos_y,height),parent=current) 
                pm.calc_values(destination)
                if pm in visited:
                    old_loc = visited.index(pm)
                    #old = visited[old_loc]
                    #if pm.g < old.g:
                    #    visited.remove(old)
                    #    visited.append(pm)
                possible_moves.append(Position(pos_x,pos_y, height))
    return possible_moves


def push_moves_to_heap(moves, current):
    global start
    global destination
    global to_visit
    for move in moves:
        possible =  Node(move, parent=current)
        possible.calc_values(destination)
        if possible in visited:
            logging.debug(f"found possible node already visited {possible}")
            old =  visited[visited.index(possible)]
            logging.debug(f"new g: {possible.g}  old g: {old.g}")
            if possible.g < old.g:
                visited.remove(old)
                heapq.heappush(to_visit, possible)
        else:
            logging.debug(f"pushing new Node to heap {possible}")
            if possible not in to_visit:
                heapq.heappush(to_visit, possible)
    


# load height map and make variables 
starting_conditions = make_heightmap("day-12/input.txt")
heightmap = starting_conditions['heightmap']
start = starting_conditions['start']
destination = starting_conditions['dest']
root_node = Node(start)
root_node.calc_values(destination)
path = []
visited = []
to_visit = []

# start the pathfinding logic by initilizing the heap with the starting node
# then keep searching for valid moves and adding them to the heap
# evaluating the nodes with the lowest available metrics first
# end when our current positiion is the desitination
heapq.heappush(to_visit,root_node)
while len(to_visit) > 0:
    os.system('clear')
    logging.debug("*"*40)
    logging.debug("start of loop")
    logging.debug("*"*40)
    current = heapq.heappop(to_visit)
    logging.debug(print_path(current, get_path(current, [])))
    if  current.position == destination :
        print(get_path(current,[]))
        print(len(get_path(current,[])))
        break
    visited.append(current)
    possible_moves = get_possible_moves(current)
    push_moves_to_heap(possible_moves, current)
    logging.debug(current)
    logging.debug(f'to_visit_length: {len(to_visit)}')
    #logging.debug(f'to_visit: {to_visit}')
    logging.debug(f'visited_length: {len(visited)}')






