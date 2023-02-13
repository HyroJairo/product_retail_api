import os
from flask import request, Flask
from user_data.user_data import Users, engine
import sqlalchemy
from sqlalchemy import select
import pandas as pd
import settings
import products.main as prd
from productAPI import simple_page

def create_app():
    settings.init()
    
    app = Flask(__name__)
    app.register_blueprint(simple_page)

    sqlite_path = "backend/user_data/database/userData.db"
    if os.path.exists(sqlite_path):
        sqlite_connect = f"sqlite+pysqlite:///{sqlite_path}"
    else:
        sqlite_connect = "sqlite+pysqlite:///user_data/database/userData.db"

    @app.route('/register/', methods=['GET', 'POST', 'PUT', 'DELETE']) #for creating, updating, deleting an account
    def register():   
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
                    conn.close()
                    engine.dispose()
                    return "email already exists"
                conn.commit()
                conn.close() 
                engine.dispose() 
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
                dlt = pd.read_sql(sqlalchemy.select(Users.email==current_email), conn).values.tolist()
                dlt = [True for i in dlt if [True] == i]
                try:
                    if dlt == []:
                        raise Exception
                    stmt = sqlalchemy.update(Users).where(Users.email==current_email).values(user_name=un, password=pw, email=em, address=ad, payment_methods=pm)
                    conn.execute(stmt)
                    conn.commit()
                    conn.close()
                    engine.dispose() 
                except Exception as e:
                    conn.close()
                    engine.dispose() 
                    return 'invalid email'
            return 'account updated'
        elif request.method=='DELETE':  ### TODO: Log out users who are deleted while logged in
            current_email = request.json["email"]
            #email=input("What is your email: ") #an old method of adding from command line instead of postman
            
            with engine.connect() as conn:
                dlt = pd.read_sql(sqlalchemy.select(Users.email==current_email), conn).values.tolist()
                dlt = [True for i in dlt if [True] == i]
                try:
                    if dlt == []:
                        raise Exception
                    stmt = sqlalchemy.delete(Users).where(Users.email==current_email)
                    conn.execute(stmt)
                    conn.commit()
                    conn.close()
                    engine.dispose()  
                except Exception as e:
                    conn.close()
                    engine.dispose() 
                    return 'invalid email'
            return 'account deleted'
        engine.dispose()
        return 'nothing here'

    @app.route('/login/', methods=['POST']) #for logging in with an existing email
    def login():
        if settings.logged_in:
            return 'Already Logged In'
        
        engine = sqlalchemy.create_engine(sqlite_connect)
        
        email = request.json["email"]
        password = request.json["password"]

        # username= input("Enter your name and password ")  #an old method of adding from command line instead of postman
        # password = input("Enter your password ")
        with engine.connect() as conn:
            new_data = pd.read_sql(select(Users).where(Users.email==email), conn).values.tolist()
            if new_data:
                if (new_data[0][2]==password and new_data[0][3]==email):
                    settings.logged_in = True
                    conn.close()
                    engine.dispose()
                    return f'Welcome {new_data[0][1]}'
                # for i, j in zip(newdb, newdp): #an old method of searching throught he data base to see if two columns match at the same row
                #     if i == [True] and j == [True]:
                #         print(newdb)
                #         print(newdp)
                #         logged_in = True
                #         return 'logged in'
            else:
                conn.close()
                engine.dispose()
                return 'invalid'
        engine.dispose()        
        # if session.query(Users).filter(Users.user_name==username) & session.query(Users).filter(Users.password==password): 
        #     logged_in = True 
        #     return 'Logged In'            ###### an older moethod of using users.filters to find the username ########
        # else:
        #     return 'invalid name or password'
            
    @app.route('/logout/', methods=['POST']) # logout returns nothing if you are not logged in (remember that debug mode resets to false whenever you save while running)
    def logout():
        if settings.logged_in:
            settings.logged_in = False
            return 'Logged Out'
        else:
            return 'Not Logged In'
     
    return app

if __name__ =='__main__':
    ikea_products = prd.main()
    #prd.cli_testing(ikea_products)
    app = create_app()
    app.run(port = 8080)#, debug=True) #local host 8080
    prd.dbc.close_connection()
    engine.dispose()