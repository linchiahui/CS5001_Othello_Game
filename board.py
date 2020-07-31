from disc import Disc
from config import BLACK, WHITE, VALID_MOVE


ROW_SIZE = 8
COL_SIZE = 8


class Board():
    def __init__(self, w, h, gc):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

        self.width = w
        self.hight = h
        self.gc = gc

        self.board[3][3] = Disc(3, 3, WHITE)
        self.board[4][4] = Disc(4, 4, WHITE)
        self.board[3][4] = Disc(3, 4, BLACK)
        self.board[4][3] = Disc(4, 3, BLACK)

        self.turn = BLACK
        self.get_valid_place(self.turn)
        self.show_possible_move()
        self.both_side_no_valid_move = False

    def display(self):
        self.black_count = 0
        self.white_count = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    self.board[row][col].display()
                    if self.board[row][col].color == BLACK:
                        self.black_count += 1
                    elif self.board[row][col].color == WHITE:
                        self.white_count += 1
        self.game_result(self.black_count, self.white_count)

    def game_result(self, bc, wc):
        """Deal with the game is over, and decide who win the game"""

        if self.both_side_no_valid_move:

            # -----------------------------------------------------------

            fill(254, 128, 0)
            textSize(70)
            final_count = "black: " + str(bc) + " white: " + str(wc)
            text(final_count, 90, 300)

            # there are 4 lines call fill show the count of discs,
            # it will arise pytest wrong. Thus if TA want to test this func.
            # please comment my 4 lines in game_result(). thanks!
            # -----------------------------------------------------------

            if bc > wc:
                self.gc.black_wins = True
            elif bc < wc:
                self.gc.white_wins = True
            else:
                self.gc.tie = True

    def place(self, pos_x, pos_y):
        """place the disc if the move is in valid list"""
        x_index = pos_x // (self.width // COL_SIZE)
        y_index = pos_y // (self.hight // ROW_SIZE)

        if (y_index, x_index) in self.valid_move:

            self.board[y_index][x_index] = Disc(
                y_index, x_index, self.turn)

            # flip the disk in 8 directions
            for direct in range(1, 9):
                self.flip(direct, (y_index, x_index), self.turn)

            # ------------------------------------------------------------
            # call display itself is because I don't want time delay
            # for show the player move
            self.display()
            # In place() there is a line call self.display(),
            # it will arise pytest wrong. Thus if TA want to test this func.
            # please comment my self.display line. thanks!
            # ------------------------------------------------------------

            if self.turn == WHITE:
                self.turn = BLACK
            elif self.turn == BLACK:
                self.turn = WHITE

            self.get_valid_place(self.turn)
            self.show_possible_move()

            # deal with if there are no more legal moves,
            # switch back to the opponent.
            if not self.valid_move:
                print("Oh, there is no any valid move!")
                if self.turn == WHITE:
                    self.turn = BLACK
                    print("Black turn!")
                elif self.turn == BLACK:
                    self.turn = WHITE
                    print("White turn!")
                self.get_valid_place(self.turn)
                self.show_possible_move()
                if not self.valid_move:
                    # If there are no more legal moves at all, end the game.
                    print("That's all, Good game...")
                    self.both_side_no_valid_move = True

    def get_valid_place(self, color):
        """traversal all the valid move for the player or com.
        depend on the turn color"""

        places = []

        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if self.board[i][j] != 0 and self.board[i][j].color == color:
                    places += self.look_for_valid_move(i, j, color)

        places = list(set(places))
        self.valid_move = places

    def look_for_valid_move(self, row, col, color):
        """look for specific position,
        and BFS the valid position for that position"""

        if color == BLACK:
            opponent = WHITE
        else:
            opponent = BLACK

        places = []

        # invalid row or column, then return places
        if (row < 0 or row > 7 or col < 0 or col > 7):
            return places

        # For 8 direction looking for possible positions
        # to put a disk that append in list

        # north
        i = row - 1
        if i >= 0 and self.check_disc(i, col, opponent):
            i = i - 1
            while i >= 0 and self.check_disc(i, col, opponent):
                i = i - 1
            if i >= 0 and (self.board[i][col] == 0 or
                           self.check_disc(i, col, VALID_MOVE)):
                places.append((i, col))

        # south
        i = row + 1
        if i < ROW_SIZE and self.check_disc(i, col, opponent):
            i = i + 1
            while i < ROW_SIZE and self.check_disc(i, col, opponent):
                i = i + 1
            if i < ROW_SIZE and (self.board[i][col] == 0 or
                                 self.check_disc(i, col, VALID_MOVE)):
                places.append((i, col))

        # east
        j = col + 1
        if j < COL_SIZE and self.check_disc(row, j, opponent):
            j = j + 1
            while j < COL_SIZE and self.check_disc(row, j, opponent):
                j = j + 1
            if j < COL_SIZE and (self.board[row][j] == 0 or
                                 self.check_disc(row, j, VALID_MOVE)):
                places.append((row, j))

        # west
        j = col - 1
        if j >= 0 and self.check_disc(row, j, opponent):
            j = j - 1
            while j >= 0 and self.check_disc(row, j, opponent):
                j = j - 1
            if j >= 0 and (self.board[row][j] == 0 or
                           self.check_disc(row, j, VALID_MOVE)):
                places.append((row, j))

        # northeast
        i = row - 1
        j = col + 1
        if i >= 0 and j < COL_SIZE and self.check_disc(i, j, opponent):
            i = i - 1
            j = j + 1
            while i >= 0 and j < COL_SIZE and self.check_disc(i, j, opponent):
                i = i - 1
                j = j + 1
            if i >= 0 and j < COL_SIZE and (self.board[i][j] == 0 or
                                            self.check_disc(i, j, VALID_MOVE)):
                places.append((i, j))

        # northwest
        i = row - 1
        j = col - 1
        if i >= 0 and j >= 0 and self.check_disc(i, j, opponent):
            i = i - 1
            j = j - 1
            while i >= 0 and j >= 0 and self.check_disc(i, j, opponent):
                i = i - 1
                j = j - 1
            if i >= 0 and j >= 0 and (self.board[i][j] == 0 or
                                      self.check_disc(i, j, VALID_MOVE)):
                places.append((i, j))

        # southeast
        i = row + 1
        j = col + 1
        if i < ROW_SIZE and j < COL_SIZE and self.check_disc(i, j, opponent):
            i = i + 1
            j = j + 1
            while i < ROW_SIZE and j < COL_SIZE and self.check_disc(i, j, opponent):
                i = i + 1
                j = j + 1
            if i < ROW_SIZE and j < COL_SIZE and (self.board[i][j] == 0 or
                                                  self.check_disc(i, j, VALID_MOVE)):
                places.append((i, j))

        # southwest
        i = row + 1
        j = col - 1
        if i < ROW_SIZE and j >= 0 and self.check_disc(i, j, opponent):
            i = i + 1
            j = j - 1
            while i < ROW_SIZE and j >= 0 and self.check_disc(i, j, opponent):
                i = i + 1
                j = j - 1
            if i < ROW_SIZE and j >= 0 and (self.board[i][j] == 0 or
                                            self.check_disc(i, j, VALID_MOVE)):
                places.append((i, j))

        return places

    def flip(self, direction, position, color):
        """ Flips the discs of the given color in the given direction
        (1=North,2=Northeast...) from position. """

        if direction == 1:
            # North
            row_dir = -1
            col_dir = 0
        elif direction == 2:
            # Northeast
            row_dir = -1
            col_dir = 1
        elif direction == 3:
            # East
            row_dir = 0
            col_dir = 1
        elif direction == 4:
            # Southeast
            row_dir = 1
            col_dir = 1
        elif direction == 5:
            # South
            row_dir = 1
            col_dir = 0
        elif direction == 6:
            # Southwest
            row_dir = 1
            col_dir = -1
        elif direction == 7:
            # West
            row_dir = 0
            col_dir = -1
        elif direction == 8:
            # Northwest
            row_dir = -1
            col_dir = -1

        # discs to flip
        places = []
        i = position[0] + row_dir
        j = position[1] + col_dir

        if color == WHITE:
            opponent = BLACK
        else:
            opponent = WHITE

        if i in range(ROW_SIZE) and j in range(COL_SIZE) and self.check_disc(i, j, opponent):
            # assures there is at least one disc to flip
            places.append((i, j))
            i = i + row_dir
            j = j + col_dir
            while i in range(ROW_SIZE) and j in range(COL_SIZE) and self.check_disc(i, j, opponent):
                # search for more pieces to flip
                places.append((i, j))
                i = i + row_dir
                j = j + col_dir
            if i in range(ROW_SIZE) and j in range(COL_SIZE) and self.check_disc(i, j, color):
                # found a piece of the right color to flip the pieces between
                for pos in places:
                    # flips
                    self.board[pos[0]][pos[1]].color = color

    def show_possible_move(self):
        """ Show the circle that not fill with color to hint player where is
        valid position to place disc. """
        for index_x, index_y in self.valid_move:
            self.board[index_x][index_y] = Disc(index_x, index_y, VALID_MOVE)
        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if self.check_disc(i, j, VALID_MOVE) and (i, j) not in self.valid_move:
                    self.board[i][j] = 0

    def check_disc(self, i, j, color):
        """ Create this method to decide the disc condition true or false
            check the position is what color disc I want"""
        return self.board[i][j] != 0 and self.board[i][j].color == color
