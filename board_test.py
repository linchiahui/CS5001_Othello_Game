from board import Board
from game_controller import GameController
from disc import Disc
from config import WIDTH, HEIGHT, BLACK, WHITE


def test_constructor():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    assert len(cur_board.board) == 8
    assert len(cur_board.board[0]) == 8
    assert cur_board.width == WIDTH
    assert cur_board.hight == HEIGHT
    assert cur_board.gc == gc

    # test init four discs on the center of board
    assert cur_board.board[3][3]
    assert cur_board.board[4][4]
    assert cur_board.board[4][3]
    assert cur_board.board[3][4]

    assert cur_board.turn == BLACK
    assert not cur_board.both_side_no_valid_move
    # init will get 4 valid move
    assert len(cur_board.valid_move) == 4

    count = 0
    for i in range(len(cur_board.board)):
        for j in range(len(cur_board.board[0])):
            if cur_board.board[i][j] != 0:
                count += 1
    #  init there will 8 object on the board
    # 2 white discs, 2 black discs, and 4 valid move discs
    assert count == 8


def test_game_result():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    cur_board.both_side_no_valid_move = True

    # In game_result() there are 4 lines call fill show the count of discs,
    # it will arise pytest wrong. Thus if TA want to test this func.
    # please comment my 4 lines in game_result(). thanks!
    # ---------------------------------------------

    # cur_board.game_result(20, 10)
    # assert gc.black_wins
    # cur_board.game_result(10, 20)
    # assert gc.white_wins
    # cur_board.game_result(10, 10)
    # assert gc.tie
    # ---------------------------------------------


def test_place():
    '''In place() method there is a line call board.display(),
       it will arise pytest error. Thus if TA want to test this func.
       please comment my display line in board class. thanks!'''
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)

    cur_board.place(101, 201)
    black_count = 0
    for i in range(len(cur_board.board)):
        for j in range(len(cur_board.board[0])):
            if cur_board.check_disc(i, j, BLACK):
                black_count += 1
    assert black_count == 2
    # because it is not a valid move, so the black is not placed on board
    # the total count of black discs is still 2

    # ---------------------------------------------------------------------------

    # # Code followeing need to comment self.display() line in place() method
    # # to execute pytest.
    # cur_board.place(301, 201)
    # black_count = 0
    # for i in range(len(cur_board.board)):
    #     for j in range(len(cur_board.board[0])):
    #         if cur_board.check_disc(i, j, BLACK):
    #             black_count += 1
    # assert black_count == 4
    # # because it is a valid move, so the black is placed (3,2) on board
    # # the total count of black discs is 4, including flip after placed.

    # assert cur_board.turn == WHITE
    # # after valid placed, turn another player
    # for i in range(len(cur_board.board)):
    #     for j in range(len(cur_board.board[0])):
    #         if i == 0 and j == 7:
    #             continue
    #         else:
    #             cur_board.board[i][j] = Disc(i, j, BLACK)
    # cur_board.board[0][0] = Disc(0, 0, WHITE)
    # cur_board.get_valid_place(WHITE)
    # cur_board.place(701, 1)
    # assert cur_board.both_side_no_valid_move
    # # Assume the board is full after white place
    # # the flag both_side_no_valid_move will turn on.
    # # Because there is no any valid move for both sides

    # ---------------------------------------------------------------------------


def test_get_valid_place():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    cur_board.get_valid_place(cur_board.turn)
    assert len(cur_board.valid_move) == 4
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, V, 0, 0, 0, 0],
    #  [0, 0, V, W, B, 0, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, 0, V, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]

    cur_board.board[3][3] = Disc(3, 3, BLACK)
    cur_board.get_valid_place(cur_board.turn)
    assert len(cur_board.valid_move) == 3
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, B, B, 0, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, 0, V, V, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    cur_board.get_valid_place(WHITE)
    assert len(cur_board.valid_move) == 3
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, V, 0, V, 0, 0, 0],
    #  [0, 0, 0, B, B, 0, 0, 0],
    #  [0, 0, V, B, W, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]

    cur_board.board[4][4] = Disc(4, 4, BLACK)
    cur_board.get_valid_place(cur_board.turn)
    assert len(cur_board.valid_move) == 0
    cur_board.get_valid_place(WHITE)
    assert len(cur_board.valid_move) == 0
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, B, B, 0, 0, 0],
    #  [0, 0, 0, B, B, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]


def test_look_for_valid_move():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    places = cur_board.look_for_valid_move(3, 4, cur_board.turn)
    assert len(places) == 2
    assert places == [(5, 4), (3, 2)]
    # for the black disc (3, 4), valid move is (5, 4), (3, 2)

    cur_board.board[3][3] = Disc(3, 3, BLACK)
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, B, B, 0, 0, 0],
    #  [0, 0, 0, B, W, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    places = cur_board.look_for_valid_move(4, 4, WHITE)
    assert len(places) == 3
    assert places == [(2, 4), (4, 2), (2, 2)]
    # for the white disc (4, 4), valid move is (2, 4), (4, 2), (2, 2)


def test_flip():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)

    cur_board.board[3][2] = Disc(3, 2, BLACK)
    # B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, B, W, B, 0, 0, 0],
    #  [0, 0, 0, B, W, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    cur_board.flip(3, (3, 2), BLACK)
    # direction 3 is flip east direction of position (3, 2)
    assert cur_board.board[3][3].color == BLACK
    # Board[3][3] will be turn to BLACK

    cur_board.board[2][4] = Disc(2, 4, WHITE)
    # B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, W, 0, 0, 0],
    #  [0, 0, B, B, B, 0, 0, 0],
    #  [0, 0, 0, B, W, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    cur_board.flip(5, (2, 4), WHITE)
    # direction 5 is flip south direction of position (2, 4)
    assert cur_board.board[3][4].color == WHITE
    # Board[3][4] will be turn to WHITE


def test_show_possible_move():
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    cur_board.show_possible_move()
    assert cur_board.board[3][2]
    assert cur_board.board[2][3]
    assert cur_board.board[4][5]
    assert cur_board.board[5][4]
    assert not cur_board.board[3][5]
    # Now, there exists a object of valid move at (3,2), (2,3), (4,5), (5,4)
    # Also, there don't exist object in board[3][5]
    # which color is not BLACK and WHITE
    # V = valid_move, B = BLACK, W = WHITE
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, V, 0, 0, 0, 0],
    #  [0, 0, V, W, B, 0, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, 0, V, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]

    cur_board.board[2][3] = Disc(2, 4, BLACK)
    for direction in range(1, 9):
        cur_board.flip(direction, (2, 3), BLACK)
    cur_board.board[2][4] = Disc(2, 4, WHITE)
    for direction in range(1, 9):
        cur_board.flip(direction, (2, 4), WHITE)
    cur_board.get_valid_place(BLACK)
    cur_board.show_possible_move()
    assert not cur_board.board[3][2]
    assert cur_board.board[2][5]
    assert cur_board.board[3][5]
    assert cur_board.board[4][5]
    # Now, there do not exist a object of valid move at (3,2)
    # The object in board[3][2] is no longer exist and replaced by 0
    # V = valid_move, B = BLACK, W = WHITE
    # But, there exist objects of valid move at(2,5), (3,5), (4,5)
    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, B, W, V, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    assert cur_board.board[2][5].color == 2
    assert cur_board.board[3][5].color == 2
    assert cur_board.board[4][5].color == 2
    # color = 2 is mean it is not BLACK and WHITE
    # It is just a valid move for player to placed


def test_check_disc():
    # check the position is what color disc I want
    gc = GameController(WIDTH, HEIGHT)
    cur_board = Board(WIDTH, HEIGHT, gc)
    assert cur_board.check_disc(3, 3, WHITE)
    assert cur_board.check_disc(3, 4, BLACK)
    assert not cur_board.check_disc(0, 0, WHITE)
