alpha_positions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
white_home = 2
black_home = 7


def rook(pos1, pos2):
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def bishop(pos1, pos2):
    return abs(alpha_positions[pos1[0]] - alpha_positions[pos2[0]]) == abs(int(pos1[1]) - int(pos2[1]))


def knight(pos1, pos2):
    valid_pos = {2: 1, 1: 2}
    diff_horizontal = abs(alpha_positions[pos1[0]] - alpha_positions[pos2[0]])
    return abs(int(pos1[1]) - int(pos2[1])) == valid_pos[diff_horizontal] if diff_horizontal in valid_pos else False


def king(pos1, pos2):
    return abs(int(pos1[1]) == int(pos2[1])) in [0, 1] or abs(alpha_positions[pos1[0]] == alpha_positions[pos2[0]]) in \
           [0, 1]


def queen(pos1, pos2):
    return bishop(pos1, pos2) or rook(pos1, pos2)


def pawn(pos1, pos2):
    return abs(int(pos2[1]) - int(pos1[1])) == 1


def pawn_black(pos1, pos2):
    if (int(pos1[1]), int(pos2[1])) == (black_home, black_home - 2) and pos1[0] == pos2[0]:
        return True
    return pawn(pos1, pos2)


def pawn_white(pos1, pos2):
    if (int(pos1[1]), int(pos2[1])) == (white_home, white_home + 2) and pos1[0] == pos2[0]:
        return True
    return pawn(pos2, pos1)


def is_pos_inside_board(pos):
    return pos[0] in alpha_positions and pos[1] in alpha_positions.values()


piece_functions = {'k': king, 'q': queen, 'r': rook, 'b': bishop, 'n': knight,}


def is_valid_move(piece, pos1, pos2):
    if pos1 == pos2 or not(len(pos1) == len(pos2) == 2):
        return False
    if not is_pos_inside_board(pos1) or not is_pos_inside_board(pos2):
        return False
    if piece == 'p':
        return pawn_black(pos1, pos2)
    if piece == 'P':
        return pawn_white(pos1, pos2)
    return piece_functions[piece.lower()](pos1, pos2)
