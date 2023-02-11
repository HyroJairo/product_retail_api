# Importing the flask module.
# The Flask class creates the server for us
from flask import request, jsonify, Blueprint, render_template
import products.main as prd
import settings

simple_page = Blueprint('simple_page', __name__, template_folder='templates')

# This is an in-memory collection to hold objects
users = []
orders = []
products = []

# The server instance can decorate a function
# When the url is passed to route() is called, Flask will execute the function 
# A Flask route must return a value, either text, HTML or JSON
@simple_page.route("/", methods=["GET"])
def index():
    return "Welcome to the Ikea Store!!! :)"

# Flask methods should be organized by URL
# In this case, both adding users and getting all users is defined on /users
@simple_page.route("/users", methods=["GET", "POST"])
def handle_create_read():

    # This statement will immediately end the function if the user is not logged in
    if not settings.logged_in:
        return "please login at /login"

    # The request object contains the information sent to the server from the client request
    # By switching behavior on the HTTP method, multiple request types can be handled.
    if request.method == "GET":
        # The get method wants to READ all users, so we return a json object of the users
        return jsonify(users)

# Adding an <id> parameter of a URL will be called to this function
# This function will handle updating users, deleting users, and retrieving one user by their id
@simple_page.route("/users/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete(id):

    # This statement will immediately end the function if the user is not logged in
    if not settings.logged_in:
        return "please login at /login"
    
    # The GET method at this URL will return one user if their id matches the value passed in the url
    if request.method == "GET":
        # I am using a List Comprehension to filter the users list, then return that user
        user = [user for user in users if user["id"] == id]
        return jsonify(user)

    # The PUT method will replace a user in the list if their id matches what was passed
    elif request.method == "PUT":
        # PUT requests also have a method body, in this case it is the user to be updated
        # Here, I am creating a loop to find the user by the id from the URL.
        new_user = request.json
        index = -1
        for i, user in enumerate(user):
            if user["id"] == id:
                index = i
        if index != -1:
            users[i] == new_user[0]
        return jsonify(users)
    
    # The DELETE method will remove a user in the list if their id matches what was passed
    elif request.method == "DELETE":
        # I am using a List Comprehension to filter the employees list, then return all employees that do not Match!
        user = [user for user in users if not user["id"] == id]
        return jsonify(user)

#-------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------

# Flask methods should be organized by URL
# In this case, both adding orders and getting all orders is defined on /orders
@simple_page.route("/orders", methods=["GET", "POST"])
def view_orders():

    # This statement will immediately end the function if the order is not logged in
    if not settings.logged_in:
        return "please login at /login"

    # The request object contains the information sent to the server from the client request
    # By switching behavior on the HTTP method, multiple request types can be handled.
    if request.method == "GET":
        # The get method wants to READ all orders, so we return a json object of the orders
        return jsonify(orders)

# Adding an <id> parameter of a URL will be called to this function
# This function will handle updating orders, deleting orders, and retrieving one order by their id
@simple_page.route("/orders/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete_order(id):

    # This statement will immediately end the function if the order is not logged in
    if not settings.logged_in:
        return "please login at /login"
    
    # The GET method at this URL will return one order if their id matches the value passed in the url
    if request.method == "GET":
        # I am using a List Comprehension to filter the orders list, then return that order
        order = [order for order in orders if order["id"] == id]
        return jsonify(order)

    # The PUT method will replace a order in the list if their id matches what was passed
    elif request.method == "PUT":
        # PUT requests also have a method body, in this case it is the order to be updated
        # Here, I am creating a loop to find the order by the id from the URL.
        new_order = request.json
        index = -1
        for i, order in enumerate(order):
            if order["id"] == id:
                index = i
        if index != -1:
            orders[i] == new_order[0]
        return jsonify(orders)
    
    # The DELETE method will remove a order in the list if their id matches what was passed
    elif request.method == "DELETE":
        # I am using a List Comprehension to filter the employees list, then return all employees that do not Match!
        order = [order for order in orders if not order["id"] == id]
        return jsonify(order)

#-------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------
# Flask methods should be organized by URL
# In this case, both adding products and getting all products is defined on /products
@simple_page.route("/products", methods=["GET", "POST"])
def view_products():

    # This statement will immediately end the function if the product is not logged in
    if not settings.logged_in:
        return "please login at /login"

    # The request object contains the information sent to the server from the client request
    # By switching behavior on the HTTP method, multiple request types can be handled.
    if request.method == "GET":
        products_df = prd.dbc.read_data_to_json("products")
        return render_template('simple.html', tables=[products_df.to_html(classes='date')], titles=products_df.columns.values)
        #return jsonify(prd.dbc.read_data_to_json("products"))
        # The get method wants to READ all products, so we return a json object of the products
        #return jsonify(products)

# Adding an <id> parameter of a URL will be called to this function
# This function will handle updating products, deleting products, and retrieving one product by their id
@simple_page.route("/products/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete_product(id):

    # This statement will immediately end the function if the product is not logged in
    if not settings.logged_in:
        return "please login at /login"
    
    # The GET method at this URL will return one product if their id matches the value passed in the url
    if request.method == "GET":
        # I am using a List Comprehension to filter the products list, then return that product
        product = [product for product in products if product["id"] == id]
        return jsonify(product)

    # The PUT method will replace a product in the list if their id matches what was passed
    elif request.method == "PUT":
        # PUT requests also have a method body, in this case it is the product to be updated
        # Here, I am creating a loop to find the product by the id from the URL.
        new_product = request.json
        index = -1
        for i, product in enumerate(product):
            if product["id"] == id:
                index = i
        if index != -1:
            products[i] == new_product[0]
        return jsonify(products)
    
    # The DELETE method will remove a product in the list if their id matches what was passed
    elif request.method == "DELETE":
        # I am using a List Comprehension to filter the employees list, then return all employees that do not Match!
        product = [product for product in products if not product["id"] == id]
        return jsonify(product)