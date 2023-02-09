# Importing the flask module.
# The Flask class creates the server for us
from flask import Flask, request, jsonify

# creates an instance of the Flask Class will be our server
app = Flask(__name__)

# This is an in-memory collection to hold objects
customers = []

# This is a boolean to determine if the user is logged in
logged_in = False

# The server instance can decorate a function
# When the url is passed to route() is called, Flask will execute the function 
# A Flask route must return a value, either text, HTML or JSON
@app.route("/")
def index():
    return "Welcome to the Ikea Store!!! :)"

@app.route("/login")
def login():
    global logged_in
    username = request.json["username"]
    password = request.json["password"]

    if username == "Hello" and password == "World":
        logged_in = True
    else:
        return "Incorrect Username or Password"

    # for x in userlist:
        # if username == userlist[user.name] and userlist[user.password]:
        #     logged_in = True
    # if not logged_in:
    #     return "Incorrect Username or Password"

# Flask methods should be organized by URL
# In this case, both adding customers and getting all customers is defined on /customers
@app.route("/customers", methods=["GET", "Post"])
def handle_create_read():

    # This statement will immediately end the function if the user is not logged in
    if not logged_in:
        return "please logini at /login"

    # The request object contains the information sent to the server from the client request
    # By switching behavior on the HTTP method, multiple request types can be handled.
    if request.method == "GET":
        # The get method wants to READ all customers, so we return a json object of the customers
        return jsonify(customers)

# Adding an <id> parameter of a URL will be called to this function
# This function will handle updating customers, deleting customers, and retrieving one customer by their id
@app.route("/customers/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete(id):

    # This statement will immediately end the function if the user is not logged in
    if not logged_in:
        return "please login at /login"
    
    # The GET method at this URL will return one customer if their id matches the value passed in the url
    if request.method == "GET":
        # I am using a List Comprehension to filter the customers list, then return that customer
        customer = [customer for customer in customers if customer["id"] == id]
        return jsonify(customer)

    # The PUT method will replace a customer in the list if their id matches what was passed
    elif request.method == "PUT":
        # PUT requests also have a method body, in this case it is the customer to be updated
        # Here, I am creating a loop to find the customer by the id from the URL.
        new_customer = request.json
        index = -1
        for i, customer in enumerate(customer):
            if customer["id"] == id:
                index = i
        if index != -1:
            customers[i] == new_customer[0]
        return jsonify(customers)
    
    # The DELETE method will remove a customer in the list if their id matches what was passed
    elif request.method == "DELETE":
        # I am using a List Comprehension to filter the employees list, then return all employees that do not Match!
        customer = [customer for customer in customers if not customer["id"] == id]
        return jsonify(customer)

# When this python file is run directly, the app will start
if __name__ == "__main__":
    # the debug argument will, among other things, automatically restart the reserver when changes are made to code
    app.run(port = 8080, debug = True)