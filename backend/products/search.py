import products.database.curd as dbc

# Sorts items by price
def sort_by_price():
    sql = """SELECT * FROM products ORDER BY price"""
    dbc.execute_and_read_statement(sql)

# Sorts/queries items by category
def sort_by_category():
    sql = """SELECT * FROM products ORDER BY category"""
    dbc.execute_and_read_statement(sql)

# Sorts items by popularity
def sort_by_popularity():
    sql = """SELECT * FROM reviews ORDER BY review DESC"""
    dbc.execute_and_read_statement(sql)

# Custom queries/sorts
def custom_query(attributes: list):
    while(True):
        custom_query = input(f"Type 1 to sort values by an attribute or 2 to search with a conditional statement: ")
        if custom_query not in ("1","2"):
            print("Please type 1 or 2.")
        elif custom_query == "1":
            while(True):
                attribute = input(f"What attribute do you want to sort by? Choose from this list: ({attributes})\n")
                if attribute not in attributes:
                    print("That attribute is not in the table!")
                else:
                    while(True):
                        asc = input("Type 1 to sort in ascending order or 2 to sort in descending order: ")
                        if asc not in ("1","2"):
                            print("Please type 1 or 2.")
                        elif asc == "1":
                            sql = f"SELECT * FROM products ORDER BY {attribute}"
                            dbc.execute_and_read_statement(sql)
                            break
                        elif asc == "2":
                            sql = f"SELECT * FROM products ORDER BY {attribute} DESC"
                            dbc.execute_and_read_statement(sql)
                            break
                    break
        elif custom_query == "2":
            while(True):
                attribute = input(f"What attribute do you want to set a condition for? Choose from this list: ({attributes})\n")
                if attribute not in attributes:
                    print("That attribute is not in the table!")
                else:
                    while True:
                        op = input("What operator (>, <, or =) do you want to use: ")
                        if op not in (">", "<", "="):
                            print("Please type either a '>', '<', or '=' character.")
                        elif op in (">", "<", "="):
                            value = input(f"Enter a value (Put strings in quotes). Only products where {attribute} is {op} the value will be shown: ")
                            try:
                                sql = f"SELECT * FROM products WHERE {attribute} {op} {value}"
                                print(f"SQL: {sql}")
                                dbc.execute_and_read_statement(sql)
                                break
                            except Exception as e:
                                print(f"Error: {e}")
                                break
                    break
        break