def EmptyBoard():
    emptyboard = [0]*64
    return emptyboard

def GenBoard():
    x = EmptyBoard()
    white = 10
    black = 20
    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    king = 5
    for i in range(8, 16, 1):
        x[i] = white+pawn
    for i in range(48, 56, 1):
        x[i] = black+pawn
    x[0:8] = [white+rook, white+knight, white+bishop, white+king, white+queen, white+bishop, white+knight, white+rook]
    x[56:] = [black+rook, black+knight, black+bishop, black+king, black+queen, black+bishop, black+knight, black+rook]
    return x

def PrintBoard(x):
    print("----------------WHITE----------------")
    space = ' '
    a = 0
    b = 0
    while b < 8:
        while True:
            if x[a] > 9:
                print(str(x[a])+3*space, end = '')
            else:
                print(str(x[a])+4*space, end = '')
            a=a+1
            if a%8 == 0:
                break
        print("")
        b = b+1
    print("----------------BLACK----------------")
    return True

def GetPlayerPositions(board, player):
    accum = []
    for i in range(0, len(board), 1):
        if (-1+player) < board[i] < (6+player):
            accum = accum + [i]
    return accum