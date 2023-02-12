import os
import sys
sys.path.insert(0, "backend")
import pytest
import sqlite3
import ikeaAPI

def remove_all_database_records(connection_path):
    conn = sqlite3.connect(connection_path)
    for row in conn.execute("""SELECT name FROM sqlite_schema
                                WHERE type='table'
                                ORDER BY name;"""):
        with conn:
            conn.execute(f"DELETE FROM {row[0]}")
    conn.close()

def pytest_runtest_setup(item):
    if os.path.exists("backend/products/database/productDatabase.db"):
        remove_all_database_records("backend/products/database/productDatabase.db")
    if os.path.exists("backend/user_data/database/userData.db"):
        remove_all_database_records("backend/user_data/database/userData.db")

@pytest.fixture
def app():
    app = ikeaAPI.create_app()
    return app