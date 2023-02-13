import copy
import random
import pandas as pd

DASH_SEPARATOR = "\n" + ("-" * 50)

class ProductReviews():
    @property
    def product_reviews_columns_list(self):
        return copy.deepcopy(self._product_reviews_columns_list)
    
    # Returns a dataframe with random review scores 1-5 for first n products
    def gen_product_reviews_df(self, n):
        data = {
            'review_id': range(1, n),
            'product_id': [random.randint(1, 3693) for i in range(1, n)],
            'review': [random.randint(1, 5) for i in range(1, n)]
               }
        self.product_reviews_df = pd.DataFrame(data)
        self._product_reviews_columns_list = list(self.product_reviews_df.columns)
        return self.product_reviews_df
    
    def print_head(self):
        print(self.product_reviews_df.head())
        self.product_reviews_df.info()

if __name__ == "__main__":
    pr = ProductReviews
    pr.gen_product_reviews_df(pr, 10).to_csv("product_reviews.csv", index="review_id")