import sys
sys.path.insert(0, "calculation")
sys.path.insert(0, "../calculation/")
from calculation import addition

def test_addition():
    arg1, arg2 = 3, 10
    assert(addition(arg1, arg2) == 3 + 10)
