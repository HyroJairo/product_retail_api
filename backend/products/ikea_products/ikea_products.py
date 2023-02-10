import copy
import pandas as pd
from pathlib import Path
import os

DASH_SEPARATOR = "\n" + ("-" * 50)

class IkeaProducts():
    alt_file_path = "C:/Users/payto/Desktop/Icons/JUMP Program/Python/project/product_retail_api/backend/products/ikea_products/ikea_products.csv"
    if os.path.exists(alt_file_path):
        ikea_products_file_path = alt_file_path
    else:
        ikea_products_file_path = Path("products/ikea_products/ikea_products.csv")
    
    def __init__(self):
        """Read csv and set item_id as the index column
        """
        self._ikea_products_df = pd.read_csv(self.ikea_products_file_path, index_col="item_id")
        self.clean_ikea_products_df()
        self._ikea_products_columns_list = list(self._ikea_products_df.columns)
    
    @property
    def ikea_products_df(self):
        return self._ikea_products_df
    
    @property
    def ikea_products_columns_list(self):
        return copy.deepcopy(self._ikea_products_columns_list)
    
    def clean_ikea_products_df(self):
        self.ikea_products_df.drop(columns=["id", "old_price", "sellable_online", "link", "other_colors", "designer", "depth", "height", "width"], inplace=True)    
    
    def print_head(self):
        print(self.ikea_products_df.head())
        self.ikea_products_df.info()