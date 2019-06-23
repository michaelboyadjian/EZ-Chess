from GenBoard import *
from LegalMoves import *
from IsPositionUnderThreat import *

def white_player_moves(x):
    # white player moves
    PrintBoard(x)
    pieceW = int(input("White player - which piece would you like to move?\n"))
    moveW = int(input("Where would you like to move it?\n"))
    a = GetPieceLegalMoves(x, pieceW)
    print(a)
    for i in a:
        if moveW == i:
            acc = [i]
            x[moveW] = x[pieceW]
            x[pieceW] = 0
            break
    if acc == []:
        print("Invalid move! Choose again!")
        return white_player_moves(x)

def black_player_moves(x):
    # black player moves
    PrintBoard(x)
    pieceB = int(input("Black player - which piece would you like to move?\n"))
    moveB = int(input("Where would you like to move it?\n"))
    b = GetPieceLegalMoves(x, pieceB)
    print(b)
    for i in b:
        if moveB == i:
            acc = [i]
            x[moveB] = x[pieceB]
            x[pieceB] = 0
            print(acc)
            break
    if acc == []:
        print("Invalid move! Choose again!")
        return black_player_moves(x)

def main3():

    # initialize the board
    x = GenBoard()

    done = False
    while not done:

        white_player_moves(x)
        black_player_moves(x)

main3()



