from com import Computer
from board import Board
from game_controller import GameController


def test_constructor():
    gc = GameController(400, 400)
    cur_board = Board(400, 400, gc)
    com = Computer(cur_board)
    # when board change, for com the current board also change
    assert com.board.turn == 0
    cur_board.turn = 1
    assert com.board.turn == 1


def test_behavior():
    gc = GameController(800, 800)
    cur_board = Board(800, 800, gc)
    com = Computer(cur_board)
    cur_board.turn = 1
    cur_board.get_valid_place(cur_board.turn)
    # In my method of com_behavior,It would call the board method named place()
    # and in place() there is a line call self.display(),
    # it will arise pytest wrong. Thus if TA want to test this func.
    # please comment my self.display line in board method. thanks!
    # ------------------------------------------------------------------------------

    # com.behavior()
    # # there assumes computer success place a disc on valid place of board.
    # assert (cur_board.board[4][2] != 0 or cur_board.board[5][3] != 0 or
    #         cur_board.board[2][4] != 0 or cur_board.board[3][5] != 0)

    # ------------------------------------------------------------------------------
