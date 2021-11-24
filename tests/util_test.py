from jinjalint.util import flatten


def test_flatten():
    assert list(flatten(())) == []
    assert list(flatten([])) == []
    assert list(flatten((1,))) == [1]
    assert list(flatten([2, [], (), [3, [(4, 5), (6,)]]])) == [2, 3, 4, 5, 6]
