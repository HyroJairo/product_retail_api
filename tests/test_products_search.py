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
    
def pre_setup(schema, add_products):
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute(schema)
    add_products(conn)
    return conn
    
def post_setup(conn):
    conn.close()
    os.remove(DATABASE_NAME)

class TestProduct():
    TABLE_NAME = "products"
    PRIMARY_KEY = "product_id"
    ATTRIBUTES = ["name", "price", "category", "description"]
    
    def add_products_to_table(self, conn):
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, ["Vardar", 11.55, "Chair", "A lovely chair!"], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, ["Magdal", 9.55, "Table", "A lovely table!"], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, ["Gormand", 15.55, "Art", "Pretty art!"], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, ["NICETUN", 3.55, "Wall Cover", "A lovely cover!"], conn)
    
    def test_sort_by_price_monotonicity(self):
        conn = pre_setup(database_schemas.create_products, self.add_products_to_table)
        price_df = curd.return_df_of_table(self.TABLE_NAME, conn)
        assert(not price_df.price.is_monotonic_increasing)
        post_setup(conn)

    # Sorts items by price
    def test_sort_by_price(self):
        conn = pre_setup(database_schemas.create_products, self.add_products_to_table)
        price_df = search.sort_by_price(conn)
        assert(price_df.price.is_monotonic_increasing)
        post_setup(conn)

    def test_sort_by_category_monotonicity(self):
        conn = pre_setup(database_schemas.create_products, self.add_products_to_table)
        price_df = curd.return_df_of_table(self.TABLE_NAME, conn)
        assert(not price_df.category.is_monotonic_increasing)
        post_setup(conn)

    # Sorts/queries items by category
    def test_sort_by_category(self):
        conn = pre_setup(database_schemas.create_products, self.add_products_to_table)
        price_df = search.sort_by_category(conn)
        assert(price_df.category.is_monotonic_increasing)
        post_setup(conn)
        

class TestReview():
    TABLE_NAME = "reviews"
    PRIMARY_KEY = "review_id"
    ATTRIBUTES = ["user_id", "product_id", "review"]
    
    def add_products_to_table(self, conn):
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, [1, 1, 5], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, [1, 2, 3], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, [1, 3, 5], conn)
        curd.add_data(self.TABLE_NAME, self.PRIMARY_KEY, self.ATTRIBUTES, [1, 4, 1], conn)
    
    def test_sort_by_popularity(self):
        conn = pre_setup(database_schemas.create_reviews, self.add_products_to_table)
        reviews_df = curd.return_df_of_table(self.TABLE_NAME, conn)
        assert(not reviews_df.review.is_monotonic_decreasing)
        post_setup(conn)
    
    # Sorts items by popularity (highest to lowest)
    def test_sort_by_popularity(self):
        conn = pre_setup(database_schemas.create_reviews, self.add_products_to_table)
        reviews_df = search.sort_by_popularity(conn)
        assert(reviews_df.review.is_monotonic_decreasing)
        post_setup(conn)