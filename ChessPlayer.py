from ChessHelpers import *

def chessPlayer(board, player):
    candidateMoves = gen_candidateMoves(board, player)
    evalTree = gen_evalTree(board, player)
    scoreval = minimax(evalTree, 2, player)
    move = ChooseMove(evalTree, scoreval)
    status = True
    return [status, move, candidateMoves, evalTree]