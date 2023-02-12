import sqlite3

# Sql statement to create users table
create_users = (
    """ CREATE TABLE IF NOT EXISTS users(
    	 user_id INT PRIMARY KEY NOT NULL,
	 username VARCHAR(25) NOT NULL,
	 password VARCHAR(25) NOT NULL,
	 email VARCHAR(25),
	 address VARCHAR(50),
	 payment_method VARCHAR(25)); """
)

# Sql statement to create products table
create_products = (
    """CREATE TABLE IF NOT EXISTS products(
    	product_id INT PRIMARY KEY NOT NULL,
	name VARCHAR(25) NOT NULL,
	price DECIMAL NOT NULL,
	category VARCHAR(25),
	description VARCHAR(25));"""
)

# Sql statement to create reviews table
create_reviews = (
    """CREATE TABLE IF NOT EXISTS reviews(
    	review_id INT PRIMARY KEY NOT NULL,
   	user_id INT NOT NULL,
	product_id INT NOT NULL,
	review INT,
	FOREIGN KEY(product_id) REFERENCES products(product_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id));"""
)

# Sql statement to create orders table
create_orders = (
    """CREATE TABLE IF NOT EXISTS orders(
	order_id INT PRIMARY KEY NOT NULL,
   	user_id INT NOT NULL,
	order_time DATETIME,
	FOREIGN KEY(user_id) REFERENCES users(user_id));"""
)

# Sql statement to create product orders table
create_product_orders = (
    """CREATE TABLE IF NOT EXISTS product_orders(
	product_order_id INT PRIMARY KEY NOT NULL,
    	product_id INT NOT NULL,
   	order_id INT NOT NULL,
	FOREIGN KEY(product_id) REFERENCES products(product_id),
	FOREIGN KEY(order_id) REFERENCES orders(order_id));"""
)

# Opens/closes connection and executes sql statements
if __name__ == "__main__":
	conn = sqlite3.connect("ikea.db")
	cur = conn.cursor()
	cur.execute(create_users)
	cur.execute(create_products)
	cur.execute(create_reviews)
	cur.execute(create_orders)
	cur.execute(create_product_orders)
	cur.close()
	conn.close()
	print("Tables created.")
