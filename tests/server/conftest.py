import os
import sys
sys.path.insert(0, "backend")
import pytest
import sqlite3
import ikeaAPI
from user_data.user_data import engine
from products.database.curd import close_connection

PRODUCT_DB_PATH = "backend/products/database/productDatabase.db"
USER_DB_PATH = "backend/user_data/database/userData.db"

@pytest.fixture
def app():
    app = ikeaAPI.create_app()
    return app

def remove_all_database_records(connection_path):
    conn = sqlite3.connect(connection_path)
    for row in conn.execute("""SELECT name FROM sqlite_schema
                                WHERE type='table'
                                ORDER BY name;"""):
        with conn:
            conn.execute(f"DELETE FROM {row[0]}")
    conn.close()

def pytest_runtest_setup(item):
    if os.path.exists(PRODUCT_DB_PATH):
        remove_all_database_records(PRODUCT_DB_PATH)
    if os.path.exists(USER_DB_PATH):
        remove_all_database_records(USER_DB_PATH)

def pytest_sessionfinish(session, exitstatus):
    engine.dispose()
    close_connection()
    if os.path.exists(PRODUCT_DB_PATH):
        os.remove(PRODUCT_DB_PATH)
    if os.path.exists(USER_DB_PATH):
        os.remove(USER_DB_PATH)