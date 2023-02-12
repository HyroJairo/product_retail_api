import sys
sys.path.insert(0, "backend/products")
from io import StringIO
from contextlib import contextmanager
from main import get_user_input

@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig

def test_get_user_input_positive():
    input_test = "0"
    with replace_stdin(StringIO(input_test)):
        user_input = get_user_input()
    assert(user_input == int(input_test))
    
def test_get_user_input_infinite_negative_pos_int():
    input_test = "9"
    with replace_stdin(StringIO(input_test)):
        user_input = get_user_input()
    assert(user_input == -1)
    
def test_get_user_input_infinite_negative_str():
    input_test = "aaaa"
    with replace_stdin(StringIO(input_test)):
        user_input = get_user_input()
    assert(user_input == -1)