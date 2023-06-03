from multiply import multiply


def test_multiply():
    assert 6 == multiply(3, 2)
    assert 4 == multiply(2, 2)
    assert 12 == multiply(2, 6)
    assert 12 == multiply(2, 4)