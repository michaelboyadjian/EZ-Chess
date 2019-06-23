from ChessPlayer import *

def play():
    x = GenBoard()

    done = False
    while not done:

        white_player_moves(x)

        rval2 = chessPlayer(x, 20)
        x[rval2[1][1]] = x[rval2[1][0]]
        x[rval2[1][0]] = 0

    return True

play()
