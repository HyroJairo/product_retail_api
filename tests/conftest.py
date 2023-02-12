# import os
import sys
sys.path.insert(0, "backend")
import pytest
import ikeaAPI

# def pytest_runtest_setup(item):
#     if os.path.exists("backend/products/database/productDatabase.db"):
#         os.remove("backend/products/database/productDatabase.db")
#     if os.path.exists("backend/user_data/database/userData.db"):
#         os.remove("backend/user_data/database/userData.db")

@pytest.fixture
def app():
    app = ikeaAPI.create_app()
    return app