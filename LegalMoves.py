def GetPieceLegalMoves(board, position):
    if 9 < board[position] < 16:
        player = 10
    elif 19 < board[position] < 26:
        player = 20

    if board[position] == 10 or board[position] == 20:
        return GetPawnLegalMoves(board, position, player)
    elif board[position] == 11 or board[position] == 21:
        return GetKnightLegalMoves(board, position, player)
    elif board[position] == 12 or board[position] == 22:
        return GetBishopLegalMoves(board, position, player)
    elif board[position] == 13 or board[position] == 23:
        return GetRookLegalMoves(board, position, player)
    elif board[position] == 14 or board[position] == 24:
        return GetQueenLegalMoves(board, position, player)
    elif board[position] == 15 or board[position] == 25:
        return GetKingLegalMoves(board, position, player)
    else:
        return [-1, 'There is no piece here']

def GetPawnLegalMoves(board, position, player):
    accum = []
    if player == 10:
        if board[position+8] == 0:
            accum = accum + [position+8]
        if board[position] % 8 == 0 and (29-player) < board[position+9] < (36-player):
            accum = accum + [position+9]
        if board[position] % 8 == 7 and (29-player) < board[position+7] < (36-player):
            accum = accum + [position+7]
        else:
            if (29-player) < board[position+7] < (36-player):
                accum = accum + [position+7]
            if (29-player) < board[position+9] < (36-player):
                accum = accum + [position+9]
        return accum
    if player == 20:
        if board[position-8] == 0:
            accum = accum + [position-8]
        if board[position] % 8 == 0 and (29-player) < board[position-7] < (36-player):
            accum = accum + [position-7]
        if board[position] % 8 == 7 and (29-player) < board[position-9] < (36-player):
            accum = accum + [position-9]
        else:
            if (29-player) < board[position-7] < (36-player):
                accum = accum + [position-7]
            if (29-player) < board[position-9] < (36-player):
                accum = accum + [position-9]
        return accum

def GetKnightLegalMoves(board, position, player):
    if board[position] != 11 and board[position] != 21:
        return -1
    accum = []
    # corners
    if position == 0:
        for i in [10, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 7:
        for i in [6, 15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 56:
        for i in [-6, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 63:
        for i in [-10, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (up/down direction)
    elif position == 8:
        for i in [10, 17, -6]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 15:
        for i in [6, 15, -10]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 48:
        for i in [-6, -15, 10]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 55:
        for i in [-10, -17, 6]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (right/left direction)
    elif position == 1:
        for i in [10, 17, 15]:
            if not (19-player) < board[position+i] < (26-player):
                accum = accum + [position+i]
    elif position == 6:
        for i in [6, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 57:
        for i in [-6, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 62:
        for i in [-10, -17, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (diaganol direction)
    elif position == 9:
        for i in [10, 17, -6, 15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 14:
        for i in [6, 15, -10, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 49:
        for i in [-6, -15, 10, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 54:
        for i in [-10, -17, 6, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle top row
    elif 1 < position < 6:
        for i in [6, 10, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle left row
    elif 15 < position < 41 and position%8 == 0:
        for i in [-6, 10, -15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle right column
    elif 22 < position < 48 and position%8 == 7:
        for i in [6, -10, 15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle bottom row
    elif 57 < position < 62:
        for i in [-6, -10, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle second row
    elif 9 < position < 14:
        for i in [-10, -6, 6, 10, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle second column row
    elif 15 < position < 42 and position%8 == 1:
        for i in [-17, 15, -6, 10, -15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle seventh column
    elif 21 < position < 48 and position%8 == 6:
        for i in [-15, -17, 6, -10, 15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle seventh row
    elif 49 < position < 54:
        for i in [6, 10, -6, -10, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # middle 16 squares
    else:
        for i in [-6, 6, -10, 10, -15, 15, -17, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    return accum

def GetBishopLegalMoves(board, position, player):
    accum = []
    # up-left
    up_left_cnt = -9
    while True:
        if 0 <= position <= 7 or position%8 == 0:
            if not (-1+player) < board[position] < (6+player):
                accum = accum + [position]
            break
        elif 0 <= position + up_left_cnt <= 7 or (position + up_left_cnt) % 8 == 7:
            break
        elif board[position+up_left_cnt] == 0:
            accum = accum + [position+up_left_cnt]
            up_left_cnt = up_left_cnt - 9
        elif 19 < board[position+up_left_cnt] < 26:
            accum = accum + [position+up_left_cnt]
            break
        elif (-1+player) < board[position+up_left_cnt] < (6+player):
            break
    # up-right
    up_right_cnt = -7
    while True:
        if 0 <= position <= 7 or position % 8 == 7:
            break
        elif 0 <= position + up_right_cnt <= 7 or (position + up_right_cnt) % 8 == 0:
            break
        elif board[position + up_right_cnt] == 0:
            accum = accum + [position + up_right_cnt]
            up_right_cnt = up_right_cnt - 7
        elif (29-player) < board[position + up_right_cnt] < (36-player):
            accum = accum + [position + up_right_cnt]
            break
        elif (-1+player) < board[position+up_right_cnt] < (6+player):
            break
    # down-left
    down_left_cnt = 7
    while True:
        if 56 <= position <= 63 or position % 8 == 0:
            break
        elif 56 <= position + down_left_cnt <= 63 or (position + down_left_cnt) % 8 == 7:
            break
        elif board[position + down_left_cnt] == 0:
            accum = accum + [position + down_left_cnt]
            down_left_cnt = down_left_cnt + 7
        elif (29-player) < board[position + down_left_cnt] < (36-player):
            accum = accum + [position + down_left_cnt]
            break
        elif (-1+player) < board[position + down_left_cnt] < (6+player):
            break
    # down_right
    down_right_cnt = 9
    while True:
        if 56 <= position <= 63 or position % 8 == 7:
            break
        elif 56 <= position + down_right_cnt <= 63 or (position + down_right_cnt) % 8 == 0:
            if not (-1+player) < board[position] < (6+player):
                accum = accum + [position+down_right_cnt]
            break
        elif board[position + down_right_cnt] == 0:
            accum = accum + [position + down_right_cnt]
            down_right_cnt = down_right_cnt + 9
        elif (29-player) < board[position + down_right_cnt] < (36-player):
            accum = accum + [position + down_right_cnt]
            break
        elif(-1+player) < board[position+down_right_cnt] < (6+player):
            break
    return accum

def GetRookLegalMoves(board, position, player):
    # leftwards
    accum = []
    left_cnt = -1
    while True:
        if position % 8 == 0:
            break
        elif (position + left_cnt) % 8 == 7:
            break
        elif board[position + left_cnt] == 0:
            accum = accum + [position + left_cnt]
            left_cnt = left_cnt - 1
        elif (29 - player) < board[position + left_cnt] < (36 - player):
            accum = accum + [position + left_cnt]
            break
        elif (-1 + player) < board[position + left_cnt] < (6 + player):
            break
    # rightwards
    right_cnt = 1
    while True:
        if position % 8 == 7:
            break
        elif (position + right_cnt) % 8 == 0:
            break
        elif board[position + right_cnt] == 0:
            accum = accum + [position + right_cnt]
            right_cnt = right_cnt + 1
        elif (29 - player) < board[position + right_cnt] < (36 - player):
            accum = accum + [position + right_cnt]
            break
        elif (-1 + player) < board[position + right_cnt] < (6 + player):
            break
    # upwards
    up_cnt = -8
    while True:
        if 0 <= position <= 7:
            break
        elif 0 <= position + up_cnt <= 7:
            break
        elif board[position + up_cnt] == 0:
            accum = accum + [position + up_cnt]
            up_cnt = up_cnt - 8
        elif (29 - player) < board[position + up_cnt] < (36 - player):
            accum = accum + [position + up_cnt]
            break
        elif (-1 + player) < board[position + up_cnt] < (6 + player):
            break
    # downwards
    down_cnt = 8
    while True:
        if 56 <= position <= 63:
            break
        elif 56 <= position + down_cnt <= 63:
            break
        elif board[position + down_cnt] == 0:
            accum = accum + [position + down_cnt]
            down_cnt = down_cnt + 8
        elif (29 - player) < board[position + down_cnt] < (36 - player):
            accum = accum + [position + down_cnt]
            break
        elif (-1 + player) < board[position + down_cnt] < (6 + player):
            break
    return accum

def GetQueenLegalMoves(board, position, player):
    return GetRookLegalMoves(board, position, player)+GetBishopLegalMoves(board, position, player)

def GetKingLegalMoves(board, position, player):
    if board[position] != 15 and board[position] != 25:
        return -1
    accum = []
    # top-left corner case
    if position == 0:
        for i in [1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # top-right corner case
    elif position == 7:
        for i in [-1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom-left corner case
    elif position == 56:
        for i in [1, -7, -8]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom-right corner case
    elif position == 63:
        for i in [-1, -8, -9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # left of board case
    elif 1 < position < 55 and position%8 == 0:
        for i in [-8, -7, 1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # top of board case
    elif 0 < position < 7:
        for i in [-1, 1, 7, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # right of board case
    elif 7 < position < 63 and position%8 == 7:
        for i in [-8, -9, 7, 8, 1]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom of board case
    elif 56 < position < 63:
        for i in [-1, 1, -7, -8, -9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    else:
        for i in [-9, -8, -7, -1, 1, 7, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position + i]
    return accum