
oponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "sissors"
}

player_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "sissors"
}

strategy = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

score_value = {
    "rock" : 1,
    "paper" : 2,
    "sissors": 3
}

winning_move = {
    "rock" : "paper",
    "paper" : "sissors",
    "sissors" : "rock"
}

moves = {
    "rock" : {"win":"paper",
              "lose":"sissors",
              "draw": "rock"},
    "paper" : {"draw":"paper",
              "win":"sissors",
              "lose": "rock"},
    "sissors" : {"lose":"paper",
              "draw":"sissors",
              "win": "rock"},
}


def calculate_score(game):
    moves = game.strip().split(" ")
    score = ord(moves[1])-ord('W')
    o = oponent_moves[moves[0]]
    p = player_moves[moves[1]]
    if o == p:
        score += 3
    elif winning_move[o] == p:
        score += 6
    return score

def calculate_score_complex(game):
    inputs = game.strip().split(" ")
    o = oponent_moves[inputs[0]]
    p = moves[o][strategy[inputs[1]]]
    score = score_value[p]
    if o == p:
        score += 3
    elif winning_move[o] == p:
        score += 6
    return score

with open("input.txt") as i:
    s = 0
    for line in i:
        s += calculate_score_complex(line)
print(s)