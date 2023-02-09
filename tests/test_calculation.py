from calculation.calculation import addition

def test_addition():
    arg1, arg2 = 3, 10
    assert(addition(arg1, arg2) == 3 + 10)
