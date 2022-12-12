from pprint import pprint
import logging
logging.basicConfig(level=logging.INFO)

test_trees = list(map(str.strip ,open('day-8/input.txt').readlines()))
# test_trees = ["30373",
# "25512",
# "65332",
# "33549",
# "35390"]
# vertical sweep
sweeps = set()
# top
# left to right
for i in range(len(test_trees[0])):
    m = -1
    # top to bottom
    for j in range(len(test_trees)):
        if int(test_trees[j][i]) > m:
            m = int(test_trees[j][i])
            sweeps.add((j,i,test_trees[j][i]))
# left to right
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
    up = 0
    down = 0
    left = 0
    right = 0
    if y > 0:
        # check up
        for i in range(1, y+1):
            if tree_height >= int(test_trees[y-i][x]):
                up = up + 1
                if tree_height == int(test_trees[y-i][x]):
                    break
            else:
                break
    if y < height:
        for i in range(1, (height-y)):
            if tree_height >= int(test_trees[y+i][x]):
                down = down + 1
                if tree_height == int(test_trees[y+i][x]):
                    break
            else:
                break
        # check down
    if x > 0 :
        # check left
        for i in range(1, x+1):
            if tree_height >= int(test_trees[y][x-i]):
                left += 1
                if tree_height == int(test_trees[y][x-i]):
                    break
            else:
                break
    if x < width:
        for i in range(1, (width-x)):
            if tree_height >= int(test_trees[y][x+i]):
                right += 1
                if tree_height == int(test_trees[y][x+i]):
                    break
            else:
                break
        # check right
    return up * down * left * right

max_tree = (0, 0, 0)
for y in range(len(test_trees)):
    for x in range(len(test_trees[y])):
        v = get_view(x, y)
        logging.info(f"checking {x} {y} got height {v}")
        if v > max_tree[0]:
            max_tree = (v, x, y)

print(max_tree)