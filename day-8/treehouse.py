from pprint import pprint
import logging
logging.basicConfig(level=logging.INFO)

test_trees = list(map(str.strip ,open('day-8/input.txt').readlines()))

# vertical sweep
sweeps = set()
# top
for i in range(len(test_trees[0])):
    m = -1
    for j in range(len(test_trees)):
        if int(test_trees[j][i]) > m:
            m = int(test_trees[j][i])
            sweeps.add((j,i,test_trees[j][i]))
# bot
for i in range(len(test_trees[0])):
    m = -1
    for j in range(len(test_trees)-1, 0, -1):
        if int(test_trees[j][i]) > m:
            m = int(test_trees[j][i])
            sweeps.add((j,i,test_trees[j][i]))
# left
for i in range(len(test_trees)):
    m = -1
    for j in range(len(test_trees[0])):
        if int(test_trees[i][j]) > m:
            m = int(test_trees[i][j])
            sweeps.add((i,j,test_trees[i][j]))
# right
for i in range(len(test_trees)):
    m = -1
    for j in range(len(test_trees[0])-1,0,-1):
        if int(test_trees[i][j]) > m:
            m = int(test_trees[i][j])
            sweeps.add((i,j,test_trees[i][j]))

print(len(sweeps))

height = len(test_trees)
width = len(test_trees[0])

def get_view(x,y):
    tree_height = int(test_trees[y][x])
    up = 1
    down = 1
    left = 1
    right = 1
    if y > 0:
        # check up
        for i in range(1, y):
            if tree_height > int(test_trees[y-i][x]):
                up += 1
            else:
                break
    if y < height:
        for i in range(1, height-y):
            if tree_height > int(test_trees[y+i][x]):
                down += 1
            else:
                break
        # check down
    if x > 0 :
        # check left
        for i in range(1, x):
            if tree_height > int(test_trees[y][x-i]):
                logging.info(x-i)
                left += 1
            else:
                break
    if x < width:
        for i in range(1, width-x):
            if tree_height > int(test_trees[y][x+i]):
                logging.info(x+i)
                right += 1
            else:
                break
        # check right
    return up * down * left * right

for y in range(len(test_trees)):
    max_tree = (0, 0, 0)
    for x in range(len(test_trees[y])):
        v = get_view(x, y)
        logging.info(f"checking {x} {y} got height {v}")
        if v > max_tree[0]:
            max_tree = (v, x, y)

print(max_tree)