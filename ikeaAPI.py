import os
from flask import request, Flask
from user_data.user_data import Users
import sqlalchemy
from sqlalchemy import select
import pandas as pd
import products.main as prd
app = Flask(__name__)

logged_in = False


@app.route('/register', methods=['GET', 'POST', 'PUT', 'DELETE'])
def register():
    sqlite_path = "groupProject4/product_retail_api/userData.db"
    if os.path.exists(sqlite_path):
        sqlite_connect = "sqlite+pysqlite:///groupProject4/product_retail_api/userData.db"
    else:
        sqlite_connect = "sqlite+pysqlite:///userData.db"
        
    engine = sqlalchemy.create_engine(sqlite_connect)
    if request.method=='POST':
        un = request.json["name"]
        pw = request.json["password"]
        em = request.json["email"]
        ad = request.json["address"]
        pm = request.json["payment_method"]
        # un = input("please enter your name: ")
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
        with engine.connect() as conn:
            current_email=input("What is your email: ")
            un = input("please enter your name: ")
            pw = input("please enter a password: ")
            em = input("please enter an email: ")
            ad = input("please enter an address: ")
            pm = input("please enter your prefered payment methods: ")
            stmt = sqlalchemy.update(Users).where(Users.email==current_email).values(user_name=un, password=pw, email=em, address=ad, payment_methods=pm)
            conn.execute(stmt)
            conn.commit()
        return 'account updated'
    elif request.method=='DELETE':
        email=input("What is your email: ")
        stmt = sqlalchemy.delete(Users).where(Users.email==email)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return 'account deleted'
    return 'nothing here'

@app.route('/login', methods=['POST'])
def login():
    print("reached login")
    
    global logged_in
    sqlite_path = "groupProject4/product_retail_api/userData.db"
    if os.path.exists(sqlite_path):
        sqlite_connect = "sqlite+pysqlite:///groupProject4/product_retail_api/userData.db"
    else:
        sqlite_connect = "sqlite+pysqlite:///userData.db"
    engine = sqlalchemy.create_engine(sqlite_connect)
    
    username = request.json["username"]
    password = request.json["password"]

    
    # username= input("Enter your name and password ")
    # password = input("Enter your password ")
    with engine.connect() as conn:
        db = pd.read_sql(select(Users.user_name==username), conn)
        dp = pd.read_sql(select(Users.password==password), conn)
        newdb = db.values.tolist() 
        newdp = dp.values.tolist()
        for i, j in zip(newdb, newdp):
            if i == [True] and j == [True]:
                print(newdb)
                print(newdp)
                logged_in = True
                return 'logged in'
        return 'invalid'
                
    # if session.query(Users).filter(Users.user_name==username) & session.query(Users).filter(Users.password==password):
    #     logged_in = True
    #     return 'Logged In'
    # else:
    #     return 'invalid name or password'
        


if __name__ =='__main__':
    prd.main()
    app.run(debug=True) #local host 5000