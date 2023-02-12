import sys
sys.path.insert(0, "backend")
import pytest
import ikeaAPI

@pytest.fixture
def app():
    app = ikeaAPI.create_app()
    return app