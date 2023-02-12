import os
import sys
import sqlite3
sys.path.insert(0, "backend")
sys.path.insert(0, "backend/products")
sys.path.insert(0, "backend/products/database")
import curd
import search
import database_schemas

DATABASE_NAME = "test.db"
TABLE_NAME = "products"
PRIMARY_KEY = "product_id"
ATTRIBUTES = ["name", "price", "category", "description"]

def pre_setup():
    return sqlite3.connect(DATABASE_NAME)
    
def post_setup(conn):
    conn.close()
    os.remove(DATABASE_NAME)

# Sorts items by price
def test_sort_by_price():
    conn = pre_setup()
    conn.execute(database_schemas.create_products)
    # curd.read_data(TABLE_NAME, conn)
    curd.add_data(TABLE_NAME, PRIMARY_KEY, ATTRIBUTES, ["Vardar", 11.55, "Chair", "A lovely chair!"], conn)
    curd.add_data(TABLE_NAME, PRIMARY_KEY, ATTRIBUTES, ["Vardar", 9.55, "Chair", "A lovely chair!"], conn)
    curd.add_data(TABLE_NAME, PRIMARY_KEY, ATTRIBUTES, ["Vardar", 15.55, "Chair", "A lovely chair!"], conn)
    curd.add_data(TABLE_NAME, PRIMARY_KEY, ATTRIBUTES, ["Vardar", 3.55, "Chair", "A lovely chair!"], conn)
    price_df = search.sort_by_price(conn)
    assert(price_df.price.is_monotonic_increasing)
    post_setup(conn)

# Sorts/queries items by category
def test_sort_by_category():
    conn = pre_setup()
    conn.execute(database_schemas.create_products)
    post_setup(conn)

# Sorts items by popularity
def test_sort_by_popularity():
    conn = pre_setup()
    conn.execute(database_schemas.create_products)
    post_setup(conn)

# Custom queries/sorts
def test_custom_query():
    conn = pre_setup()
    conn.execute(database_schemas.create_products)
    post_setup(conn)