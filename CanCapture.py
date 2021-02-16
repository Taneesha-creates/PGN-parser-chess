import CanMoveToPos.py as pos


def pawn_capture(pos1, pos2):
    return int(pos1[1]) - int(pos2[1]) == 1 and abs(pos.alpha_positions[pos1[0]] -
                                                    pos.alpha_positions[pos2[0]]) == 1


def can_piece_capture(piece, pos1, pos2):
    if pos1 == pos2 or not(len(pos1) == len(pos2) == 2):
        return False
    if not pos.is_pos_inside_board(pos1) or not pos.is_pos_inside_board(pos2):
        return False
    if piece == 'p':
        return pawn_capture(pos1, pos2)
    if piece == 'P':
        return pawn_capture(pos1, pos2)
    return pos.piece_functions[piece.lower()](pos1, pos2)
