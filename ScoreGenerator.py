from Tree import *
from AI import *

def GetPieceScore(board, position, player):

    pawnW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    knightW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    bishopW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rookW = [0.0]*3 + [0.5]*2 + [0.0]*3 + [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5]*6 + [0.5] + [1.0]*6 +[0.5] + [0.0]*8
    queenW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    kingW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    if player == 10:
        if board[position] == 10:
            return pawnW[position]
        elif board[position] == 11:
            return knightW[position]
        elif board[position] == 12:
            return bishopW[position]
        elif board[position] == 13:
            return rookW[position]
        elif board[position] == 14:
            return queenW[position]
        elif board[position] == 15:
            return kingW[position]
        else:
            return 0

    if player == 20:
        pawnB = pawnW[::-1]
        knightB = knightW[::-1]
        bishopB = bishopW[::-1]
        rookB = rookW[::-1]
        queenB = queenW[::-1]
        kingB = kingW[::-1]

        if board[position] == 20:
            return pawnB[position]
        elif board[position] == 21:
            return knightB[position]
        elif board[position] == 22:
            return bishopB[position]
        elif board[position] == 23:
            return rookB[position]
        elif board[position] == 24:
            return queenB[position]
        elif board[position] == 25:
            return kingB[position]
        else:
            return 0

def GenMoveScore(board, pos1, pos2, candidateMoves, player):
        score = 0.0
        for i in range(0, len(candidateMoves), 1):
            if board[candidateMoves[i][0][1]] != 0:
                score = score + float(board[candidateMoves[i][0][1]])
        score = score + GetPieceScore(board, pos2, player) - GetPieceScore(board, pos1, player)
        return score

def gen_evalTree(board, n, cm):
    root = tree(n)
    for i in range(0, len(cm), 1):
        j = tree(cm[i])
        root.AddSuccessor(j)
        copy = list(board)
        make_move(copy, cm[i][0][0], cm[i][0][1])
    y = root.GetSuccessors()[0]
    return y

def get_evalTree(board, n, cm):
    y = gen_evalTree(board, n, cm)
    return y

def minimax(node, depth, maxp):

    minp = 0
    if maxp == 10:
        minp = 20
    elif maxp == 20:
        minp = 10

    if depth == 0:
        return node[0]
    if maxp:
        value = -10000
        for i in node:
            value = max(value, minimax(i, depth-1, minp))
        return value
    else:
        value = 10000
        for i in node:
            value = min(value, minimax(i, depth-1, maxp))
        return value

