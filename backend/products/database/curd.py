import os
import sqlite3

def open_connection():
    global conn

    connection_path = "backend/products/database"
    if os.path.exists(connection_path):
        conn = sqlite3.connect(f"{connection_path}/productDatabase.db")
    else:
        conn = sqlite3.connect(f"products/database/productDatabase.db")

def persist_dataset(table_name, df):
    try:
        df.to_sql(table_name, conn, if_exists='fail')
    except ValueError: pass

def get_primary_key(table_name, primary_key):
    query = f"SELECT MAX({primary_key}) FROM {table_name}"
    return conn.execute(query).fetchone()[0]

def add_data(table_name, primary_key, attributes: list):
    user_data = [input(f"Enter input for {attribute}: ") for attribute in attributes]
    user_data.append(int(get_primary_key(table_name, primary_key) + 1))
    attributes.append(primary_key)
    
    query, data = prep_insert_qry(table_name, user_data, attributes)
    with conn: conn.execute(query, data)

def update_data(table_name, attributes: list):
    while(True):
        attribute = input(f"What attribute do you want to change? Choose from this list: ({attributes})\n")
        if attribute not in attributes:
            print("That attribute is not in the table!")
        else: break
    value = input("What value do you want to set the attribute to? ")
    conditional = input("Type in the conditional statement after the WHERE clause: ")
    
    query = f"UPDATE {table_name} SET {attribute} = ? WHERE {conditional}"
    try:
        with conn: conn.execute(query, (value,))
    except Exception as e:
        print(e)

def read_data(table_name):
    for row in conn.execute(f"SELECT * FROM {table_name}"): print(row)
    
def delete_data(table_name, primary_key):
    while(True):
        try:
            product_id = int(input(f"Type in the {primary_key} of the IKEA product that you want to delete:\n"))
        except ValueError:
            print("That is not an integer!")
        else: break
    query = f"DELETE FROM {table_name} WHERE {primary_key} = ?"
    with conn: conn.execute(query, (product_id,))

def prep_insert_qry(table_name, args, colnames):
    """ source: https://stackoverflow.com/a/70745278
    this query is secure as long as `colnames` contains trusted data
    standard parametrized query mechanism secures `args`
    """

    binds,use = [],[]

    for colname, value in zip(colnames,args):
        if value is not None:
            use.extend([colname,","])
            binds.extend(["?",","])


    parts = [f"insert into {table_name} ("]
    use = use[:-1]
    binds = binds[:-1]
    
    parts.extend(use)
    parts.append(") values(")
    parts.extend(binds)
    parts.append(")")

    qry = " ".join(parts)

    return qry, tuple([v for v in args if not v is None])

def close_connection():
    conn.close()