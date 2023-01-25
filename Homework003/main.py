from chessboard import ChessBoard
from position import Position
# from chessfigure import ChessFigure
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King


board = ChessBoard().board   # create an instance of the chessboard and draw chessboard
position = Position("b7")    # select a particular piece position on the chessboard
new_position = Position("c5")  # select a new position on the chessboard
pawn = Pawn("white", "pawn", position)  # getting hold of a pawn piece on the selected position
print("\n\n")
pawn.move_piece(new_position, board)  # moving the pawn piece to the new position

rook = Rook("black", "rook", position)  # getting hold of a rook piece on the selected position
print("\n\n")
rook.move_piece(new_position, board)

knight = Knight("white", "knight", position)  # getting hold of a knight piece on the selected position
print("\n\n")
knight.move_piece(new_position, board)

bishop = Bishop("black", "bishop", position)  # getting hold of a bishop piece on the selected position
print("\n\n")
bishop.move_piece(new_position, board)

queen = Queen("white", "queen", position)  # getting hold of a queen piece on the selected position
print("\n\n")
queen.move_piece(new_position, board)

king = King("black", "king", position)  # getting hold of a king piece on the selected position
print("\n\n")
king.move_piece(new_position, board)
