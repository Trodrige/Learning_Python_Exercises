
class Position:
    """This class takes in a coordinate (e.g. "d2"), and it converts the column letter to a number,
     and assigns the row value to the class properties."""

    def __init__(self, coordinate):
        self.columns = "abcdefgh"
        self.rows = "9876543210"
        self.column = coordinate[0]
        self.row = self.rows[int(coordinate[1])]

        # Get column number from letter
        for num, elt in enumerate(self.columns):
            if elt == self.column:
                self.column = num + 1

