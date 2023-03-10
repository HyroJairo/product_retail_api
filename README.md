This is a team project about a backend api for a retail site. It lets users to register and signin and to buy products.
This is what this application can do:
* Help with user login/signup
* Manage the product data
* Purchasing products
* Storing Customer Product Reviews
* Sort by price
* Sort by popularity
* Sort and query by category
* Custom Queries and sorts




### Tasks
- [x] Python code of how user interacts with the store (buying, making transactions, giving reviews) - Jairo
- [x] Coding the queries (sorting different table attributes) needed, and databases besides user database - Payton
- [X] User database - Andrew
- [x] unit testing with Pytest - Mustafa




Example of how program can be interacted with:

1. Start the program from backend/ikeaAPI.py (https://github.com/HyroJairo/product_retail_api/blob/main/backend/ikeaAPI.py)
2. Download the program Postman Desktop from https://www.postman.com/downloads/
3. Run the following commands in the Postman Desktop application, in order:
        
        1. GET: localhost:8080/
        
        2. POST: localhost:8080/register/
        Body - raw: {
                "name": "TestingMan",
                "password": "aabccc",
                "email": "testing3@gmail.com",
                "address": "2222 NW testing ST",
                "payment_method": "card"
        }

        3. POST: localhost:8080/login/
        Body - raw: {
            "email": "testing3@gmail.com",
            "password": "aabccc"
        }

        4. GET: localhost:8080/products/
        Response should be of type "Preview" at the bottom

        5. GET: localhost:8080/products/79291360/
        Response should be of type "Preview" at the bottom

        6. POST: localhost:8080/logout/
        No data needed to send

        7. DELETE: localhost:8080/register/
        Body - raw: {
                "name": "TestingMan",
                "password": "aabccc",
                "email": "testing3@gmail.com",
                "address": "2222 NW testing ST",
                "payment_method": "card"
        }

Alternatively, backend/products/main.py (https://github.com/HyroJairo/product_retail_api/blob/main/backend/products/main.py) can be run directly in order to interact with the products and reviews database from the CLI (command line interface).
