import os
from flask import request, Flask
from user_data import Users #for testing
#from users_data.users_data import Users #for main branch
import sqlalchemy
from sqlalchemy import select
import pandas as pd
#import products.main as prd
app = Flask(__name__)

logged_in = False


@app.route('/register', methods=['GET', 'POST', 'PUT', 'DELETE']) #for creating, updating, deleting an account
def register():
    sqlite_path = "groupProject4/product_retail_api/userData.db"
    if os.path.exists(sqlite_path):
        sqlite_connect = "sqlite+pysqlite:///groupProject4/product_retail_api/userData.db"
    else:
        sqlite_connect = "sqlite+pysqlite:///user_data/database/userData.db"
        
    engine = sqlalchemy.create_engine(sqlite_connect)
    if request.method=='POST':
        un = request.json["name"]
        pw = request.json["password"]
        em = request.json["email"]
        ad = request.json["address"]
        pm = request.json["payment_method"]
        # un = input("please enter your name: ") #an old method of adding from command line instead of postman
        # pw = input("please enter a password: ")
        # em = input("please enter an email: ")
        # ad = input("please enter an address: ")
        # pm = input("please enter your prefered payment methods: ")
        #confirm_password=input("")
        with engine.connect() as conn:
            try:
                stmt = sqlalchemy.insert(Users).values(user_name=un, password=pw, email=em, address=ad, payment_methods=pm)
                conn.execute(stmt)
            except Exception as e:
                return "email already exists"
            conn.commit()
        return 'account added'
    elif request.method=='PUT':
        current_email = request.json["current_email"]
        un = request.json["name"]
        pw = request.json["password"]
        em = request.json["email"]
        ad = request.json["address"]
        pm = request.json["payment_method"]
        with engine.connect() as conn:
            # current_email=input("What is your email: ")  #an old method of adding from command line instead of postman
            # un = input("please enter your name: ")
            # pw = input("please enter a password: ")
            # em = input("please enter an email: ")
            # ad = input("please enter an address: ")
            # pm = input("please enter your prefered payment methods: ")
            try:
                stmt = sqlalchemy.update(Users).where(Users.email==current_email).values(user_name=un, password=pw, email=em, address=ad, payment_methods=pm)
                conn.execute(stmt)
                conn.commit()
            except Exception as e:
                return "invalid email"
        return 'account updated'
    elif request.method=='DELETE':
        email = request.json["email"]
        #email=input("What is your email: ")
        
        with engine.connect() as conn:
            try:
                stmt = sqlalchemy.delete(Users).where(Users.email==email)
                conn.execute(stmt)
                conn.commit()
            except:
                return 'invalid email'
        return 'account deleted'
    return 'nothing here'

@app.route('/login', methods=['POST']) #for logging in with an existing email
def login():
    global logged_in
    sqlite_path = "groupProject4/product_retail_api/userData.db"
    if os.path.exists(sqlite_path):
        sqlite_connect = "sqlite+pysqlite:///groupProject4/product_retail_api/userData.db"
    else:
        sqlite_connect = "sqlite+pysqlite:///user_data/database/userData.db"
    engine = sqlalchemy.create_engine(sqlite_connect)
    
    email = request.json["email"]
    password = request.json["password"]

    print(email)
    print(password)
    # username= input("Enter your name and password ")  #an old method of adding from command line instead of postman
    # password = input("Enter your password ")
    with engine.connect() as conn:
        db = pd.read_sql(select(Users.email==email), conn)
        dp = pd.read_sql(select(Users.password==password), conn)
        newdp = dp.values.tolist()
        newdb = db.values.tolist()[::-1] #for some reason this is printing in reverse order
        for i, j in zip(newdb, newdp):
            if i == [True] and j == [True]:
                print(newdb)
                print(newdp)
                logged_in = True
                return 'logged in'
        return 'invalid'
            
    # if session.query(Users).filter(Users.user_name==username) & session.query(Users).filter(Users.password==password): 
    #     logged_in = True 
    #     return 'Logged In'            ###### an older moethod of using users.filters to find the username ########
    # else:
    #     return 'invalid name or password'
        
@app.route('/logout', methods=['POST']) # logout returns nothing if you are not logged in (remember that debug mode resets to false whenever you save while running)
def logout():
    global logged_in
    if logged_in == True:
        logged_in = False
        return 'Logged Out'
    else:
        return 'Not Logged In'


if __name__ =='__main__':
    #prd.main() #just turned off for testing my own part
    app.run(debug=True) #local host 5000