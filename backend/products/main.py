import products.ikea_products.ikea_products as ikp
import products.database.curd as dbc
import products.search as dbs

def get_user_input() -> int:
    RETRY_STRING = "That is not a valid choice! (Must be an integer from 0-4)"
    
    while(True):
        try:
            user_choice = int(input("""
                            What do you want to do? (type 0-4, followed by enter)\n
                            0) Proceed to server
                            
         Ikea Products Database 1) CREATE         2) UPDATE
                                3) READ           4) DELETE
                                5) SORT BY PRICE  6) SORT BY CATEGORY\n
                            """))
        except ValueError:
            print(RETRY_STRING)
        else:
            if user_choice >= 0 and user_choice < 7: 
                break
            else:
                print(RETRY_STRING)
    return user_choice

def main():
    dbc.open_connection()
    ikea_products = ikp.IkeaProducts()
    dbc.persist_dataset("products", ikea_products.ikea_products_df)
    
    while(True):
        user_choice = get_user_input()
        print(ikp.DASH_SEPARATOR)
        
        if user_choice == 0:
            break
        elif user_choice == 1:
            dbc.add_data("products", "item_id", ikea_products.ikea_products_columns_list)
        elif user_choice == 2:
            dbc.update_data("products", ikea_products.ikea_products_columns_list)
        elif user_choice == 3:
            dbc.read_data("products")
        elif user_choice == 4:
            dbc.delete_data("products", "item_id")
        elif user_choice == 5:
            dbs.sort_by_price()
        elif user_choice == 6:
            dbs.sort_by_category()

if __name__ == "__main__":
    main()