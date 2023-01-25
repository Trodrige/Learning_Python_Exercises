from chessfigure import ChessFigure


class Bishop(ChessFigure):

    def __init__(self, color, title, chess_position):
        super().__init__(color, title, chess_position)

    def move_piece(self, new_position, board):
        # check if there's an opponent chess in the position
        opponent = super().get_piece_from_position(new_position, board)
        if opponent[0] == '_':
            super().move(new_position, board)
        else:
            print("Not a valid move, try beat() instead")

    def beat(self, new_position, board):
        # check if there's an opponent chess in the position
        opponent = super().get_piece_from_position(new_position, board)

        if opponent[0] == '_':
            print("Not a valid move, try move_piece() instead")

        else:
            if not self.color.lower() == opponent[0]:
                super().move(new_position, board)
            else:
                print("Not a valid move, use move_piece() instead")

