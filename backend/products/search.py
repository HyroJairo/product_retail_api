import products.database.curd as dbc

# Sorts items by price
def sort_by_price():
    sql = """SELECT * FROM products ORDER BY price"""
    dbc.execute_and_read_statement(sql)
    
# Sorts items by popularity
def sort_by_popularity():
    return

# Sorts/queries items by category
def sort_by_category():
    sql = """SELECT * FROM products ORDER BY category"""
    dbc.execute_and_read_statement(sql)

# Custom queries/sorts
"""def custom_query(attributes: list):
    while(True):
        custom_query = input(f"Type 1 to sort values by an attribute or 2 to set a condition: ")
        if custom_query not in (1,2):
            print("Please type 1 or 2.")
        elif custom_query == 1:
            attribute = input(f"What attribute do you want to sort by? Choose from this list: ({attributes})\n")
            if attribute not in attributes:
                print("That attribute is not in the table!")
        elif custom_query == 2:
            conditional = input("Type in the conditional statement after the WHERE clause: ")
            sql = f"SELECT * FROM products WHERE ? "
        else: break
    sql = f"SELECT * FROM products WHERE {conditional}"
    dbc.execute_and_read_statement(sql)
"""