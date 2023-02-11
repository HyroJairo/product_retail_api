import sys
sys.path.insert(0, "backend")
import settings

def test_init():
    settings.init()
    assert(settings.logged_in == False)