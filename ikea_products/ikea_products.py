import copy
import pandas as pd
from pathlib import Path

DASH_SEPARATOR = "\n" + ("-" * 50)

class IkeaProducts():
    ikea_products_file_path = Path("ikea_products/ikea_products.csv")
    
    def __init__(self):
        """Read csv and set item_id as the index column
        """
        self._ikea_products_df = pd.read_csv(self.ikea_products_file_path, index_col="item_id")
        self._ikea_products_columns_list = list(self._ikea_products_df.columns)
    
    @property
    def ikea_products_df(self):
        return self._ikea_products_df
    
    @property
    def ikea_products_columns_list(self):
        return copy.deepcopy(self._ikea_products_columns_list)