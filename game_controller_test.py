from game_controller import GameController


def test_constructor():
    gc = GameController(400, 600)
    assert gc.WIDTH == 400
    assert gc.HEIGHT == 600
    assert gc.black_wins is False
    assert gc.white_wins is False
    assert gc.tie is False
