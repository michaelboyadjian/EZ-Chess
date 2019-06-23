from LegalMoves import *

def IsPositionUnderThreat(board, position, player):
    accum = []
    for i in range(0, len(board), 1):
        if (29-player) < board[i] < (36-player):
            accum = accum + GetPieceLegalMoves(board, i)
    for i in accum:
        if i == position:
            return True
        else:
            return False
