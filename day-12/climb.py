def make_heightmap(filelocation: str):
    start_x,start_y,dest_x,dest_y = 0,0,0,0
    with open(filelocation) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == "S":
                    start_x = x
                    start_y = y
                    char = 'a'
                if char == "E":
                    dest_x = x
                    dest_y = y
                    char = 'z'
        heightmap = list(map(str.strip, f.readlines()))
    return {"heightmap": heightmap,
            "start": (start_x, start_y),
            "dest": (dest_x,dest_y)}

def get_moves(x,y, heightmap):
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





heightmap = make_heightmap("day-12/tets.txt")

