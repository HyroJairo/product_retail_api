import copy
import pandas as pd
from pathlib import Path
import os
import random

DASH_SEPARATOR = "\n" + ("-" * 50)

class ProductReviews():
    if os.path.exists("C:/Users/payto/Desktop/Icons/JUMP Program/Python/project/product_retail_api/product_reviews/product_reviews.csv"):
        product_reviews_file_path = "C:/Users/payto/Desktop/Icons/JUMP Program/Python/project/product_retail_api/product_reviews/product_reviews.csv"
    else:
        product_reviews_file_path = Path("product_reviews/product_reviews.csv")
    
    def __init__(self):
        """Generate product reviews table 
        """
        self.gen_product_reviews_df()
        self.product_reviews_df.to_csv("product_reviews.csv", index="review_id")
        self._product_reviews_columns_list = list(self._product_reviews_df.columns)
    
    @property
    def product_reviews_df(self):
        return self._product_reviews_df
    
    @property
    def product_reviews_columns_list(self):
        return copy.deepcopy(self._product_reviews_columns_list)
    
    def gen_product_reviews_df(self):
        data = {
            'review_id': range(1, 101),
            'user_id': [random.randint(1, 3) for i in range(100)],
            'order_id': [random.randint(1, 3693) for i in range(100)]
               }
        self.product_reviews_df = pd.DataFrame(data)
    
    def print_head(self):
        print(self.product_reviews_df.head())
        self.product_reviews_df.info()