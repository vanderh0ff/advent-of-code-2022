def reconstruct_path(cameFrome, current):
    total_path = [current]
    while current in cameFrome:
        current = cameFrome[current]
        total_path = [current] + total_path
    return total_path

def A_star(start, goal, h):
    openSet = [start]
    cameFrom = {}
    gScore = {}
    fScore = {}
    gScore[start] = 0
    fScore[start] = h(start)
    
    while len(openSet) > 0:
        current = openSet.pop()
        if current == goal:
            return reconstruct_path(cameFrom, current)
        openSet.remove(current)
        for 







with open('input.txt') as f:
    
