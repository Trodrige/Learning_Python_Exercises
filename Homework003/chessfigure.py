# from chessboard import ChessBoard
# from position import Position

class ChessFigure:
    """This class takes in the color, title and tile position of the chess figure,
    and it has a move method that takes in a new position and the board,
    it deletes the chess figure from the current position and places it in
    the new position."""

    def __init__(self, color, title, chess_position):
        self.color = color
        self.title = title
        self.position = chess_position
        self.row = chess_position.row
        self.column = chess_position.column
        self.replace_tile = False

    # get the chess piece from the new position
    def get_piece_from_position(self, new_position, board):

        global piece
        for row_num, row in enumerate(board):
            if row_num == int(new_position.row):
                for column_num, column in enumerate(row):
                    if column_num == int(new_position.column):
                        piece = column
        return piece

    # move piece from position to new position
    def move(self, new_position, board):

        # check if piece is empty
        if self.get_piece_from_position(self.position, board) == '__':
            print("invalid move, can not move an empty piece")

        else:
            global piece_to_move
            self.board = board
            self.new_position = new_position

            # delete piece from current position and place in new position
            for row_num, row in enumerate(board):
                if row_num == int(self.row):
                    for column_num, column in enumerate(row):
                        if column_num == self.column:
                            piece_to_move = column
                            row[column_num] = "__"
                            self.replace_tile = True

            if self.replace_tile:
                for row_num, row in enumerate(board):
                    if row_num == int(new_position.row):
                        for column_num, column in enumerate(row):
                            if column_num == new_position.column:
                                row[column_num] = piece_to_move

            for row in self.board:
                print(" ".join(row).center(20, " "))
