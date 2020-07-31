from score import Score
from board import Board
from game_controller import GameController


def test_constructor():
    gc = GameController(400, 400)
    board = Board(400, 400, gc)
    score = Score(board)
    assert score.board == board
    # assume there is no any score record in scores.txt
    # if there exists any record in scores.txt, pytest would arise error
    # because this assert score.top_score == [] is not correct now
    # assert score.top_score == []
    assert score.save_score


def test_record_name():
    gc = GameController(400, 400)
    board = Board(400, 400, gc)
    score = Score(board)
    score.record_name('Godfrey')
    assert score.name == 'Godfrey'
    score.record_name('')
    assert score.name == 'Anonymous'
    score.record_name(None)
    assert score.name == 'Anonymous'


def test_read_scores():
    gc = GameController(400, 400)
    board = Board(400, 400, gc)
    score = Score(board)
    score.fime_name = 'scores_test.txt'
    score.read_scores()
    assert score.top_score == [('Godfrey', '10'), ('Shaun', '20')]


def test_record_winner():
    gc = GameController(400, 400)
    board = Board(400, 400, gc)
    board.black_count = '2'
    score = Score(board)
    score.fime_name = 'scores_test2.txt'
    score.read_scores()
    score.record_name('Lin')
    assert score.top_score == []
    score.record_winner()
    assert score.top_score == [('Lin', '2')]

    # Convenient for a test every time, wipe out a record.
    record = open(score.fime_name, "w")
    record.write("")
    record.close()
