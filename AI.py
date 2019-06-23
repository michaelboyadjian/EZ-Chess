from ChessHelpers import *
import random

def white_player_moves(x):
    # white player moves
    PrintBoard(x)
    pieceW = int(input("White player - which piece would you like to move?\n"))
    moveW = int(input("Where would you like to move it?\n"))
    a = GetPieceLegalMoves(x, pieceW)
    acc = []
    for i in a:
        if moveW == i:
            acc = acc + [i]
            x[moveW] = x[pieceW]
            x[pieceW] = 0
            break
    if acc == []:
        print("Invalid move! Choose again!")
        return white_player_moves(x)

def black_player_moves(x):
    # black player moves
    moves = random.choice(move_generator(x, 20))
    pieceB = moves[0]
    moveB = moves[1][0]
    x[moveB] = x[pieceB]
    x[pieceB] = 0

def move_generator(board, player):
    accum = []
    L = GetPlayerPositions(board, player)
    for i in L:
        j = GetPieceLegalMoves(board, i)
        for h in j:
            k = IsPositionUnderThreat(board, h, player)
            if not k:
                accum = accum + [[i, [h, k]]]
    return accum

def gen_candidateMoves(board, player):
    candidateMoves = []
    m = move_generator(board, player)
    for i in m:
        cm = [[i[0], i[1][0]], 0]
        candidateMoves = candidateMoves + [cm]
    return candidateMoves

def make_move(board, fro, to):
    board[to] = board[fro]
    board[fro] = 0
    return True
