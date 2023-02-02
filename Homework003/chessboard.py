
class ChessBoard:
    """This class sets up the initial chessboard layout, and it prints the board"""

    def __init__(self):
        self.board = [
            [" ", "a ", "b ", "c ", "d ", "e ", "f ", "g ", "h "],
            ['8', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', '8'],
            ['7', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', '7'],
            ['6', '__', '__', '__', '__', '__', '__', '__', '__', '6'],
            ['5', '__', '__', '__', '__', '__', '__', '__', '__', '5'],
            ['4', '__', '__', '__', '__', '__', '__', '__', '__', '4'],
            ['3', '__', '__', '__', '__', '__', '__', '__', '__', '3'],
            ['2', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '2'],
            ['1', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', '1'],
            [' ', "a ", "b ", "c ", "d ", "e ", "f ", "g ", "h ", ' '],
        ]
        for row in self.board:
            print(" ".join(row).center(20, " "))