from disc import Disc


def test_constructor():
    one_disc = Disc(2, 1, 0)
    assert one_disc.row == 2
    assert one_disc.column == 1
    assert one_disc.color == 0
