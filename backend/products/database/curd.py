import sqlite3

TABLE_NAME = "products"
PRIMARY_KEY = "item_id"

def open_connection():
    global conn
    conn = sqlite3.connect(f"products/database/productDatabase.db")

def persist_dataset(df):
    try:
        df.to_sql(TABLE_NAME, conn, if_exists='fail')
    except ValueError:
        print("Database already exists!")

def get_primary_key():
    query = f"SELECT MAX({PRIMARY_KEY}) FROM {TABLE_NAME}"
    return conn.execute(query).fetchone()[0]

def add_data(attributes: list):
    user_data = [input(f"Enter input for {attribute}: ") for attribute in attributes]
    user_data.append(int(get_primary_key() + 1))
    attributes.append(PRIMARY_KEY)
    
    query, data = prep_insert_qry(user_data, attributes)
    with conn: conn.execute(query, data)

def update_data(attributes: list):
    while(True):
        attribute = input(f"What attribute do you want to change? Choose from this list: ({attributes})\n")
        if attribute not in attributes:
            print("That attribute is not in the table!")
        else: break
    value = input("What value do you want to set the attribute to? ")
    conditional = input("Type in the conditional statement after the WHERE clause: ")
    
    query = f"UPDATE {TABLE_NAME} SET {attribute} = ? WHERE {conditional}"
    try:
        with conn: conn.execute(query, (value,))
    except Exception as e:
        print(e)

def read_data():
    for row in conn.execute(f"SELECT * FROM {TABLE_NAME}"): print(row)
    
def delete_data():
    while(True):
        try:
            product_id = int(input(f"Type in the {PRIMARY_KEY} of the IKEA product that you want to delete:\n"))
        except ValueError:
            print("That is not an integer!")
        else: break
    query = f"DELETE FROM {TABLE_NAME} WHERE {PRIMARY_KEY} = ?"
    with conn: conn.execute(query, (product_id,))

def prep_insert_qry(args, colnames):
    """ source: https://stackoverflow.com/a/70745278
    this query is secure as long as `colnames` contains trusted data
    standard parametrized query mechanism secures `args`
    """

    binds,use = [],[]

    for colname, value in zip(colnames,args):
        if value is not None:
            use.extend([colname,","])
            binds.extend(["?",","])


    parts = [f"insert into {TABLE_NAME} ("]
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