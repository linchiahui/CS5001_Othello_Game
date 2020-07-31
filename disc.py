from config import BLACK, WHITE

COLOR_MAX = 255


class Disc():
    def __init__(self, row, col, color):
        self.row = row
        self.column = col
        self.color = color

    def display(self):
        """Show the disc on the right position"""

        if self.color == WHITE:
            # white
            fill(COLOR_MAX - self.color)
        elif self.color == BLACK:
            # black
            fill(self.color)
        else:
            noFill()
        ellipse(self.column * 100 + 50, self.row * 100 + 50, 90, 90)

    def __repr__(self):
        row = str(self.row)
        col = str(self.column)
        color = str(self.color)
        info = "(" + row + "," + col + "," + color + ")"
        return info
