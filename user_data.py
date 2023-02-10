import sqlalchemy
import os
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

sqlite_path = "groupProject4/product_retail_api/userData.db"
if os.path.exists(sqlite_path):
    sqlite_connect = "sqlite+pysqlite:///groupProject4/product_retail_api/userData.db"
else:
    sqlite_connect = "sqlite+pysqlite:///user_data/database/userData.db"
engine = sqlalchemy.create_engine(sqlite_connect)

Base = declarative_base()

class Users(Base):
    __tablename__= "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=False, nullable=False)
    password = Column(String(25), unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String, unique=False, nullable=False)
    payment_methods = Column(String, unique=False, nullable=False)


class Products(Base):#for testing purposes
    __tablename__="products"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    product_price = Column(Float)
    product_category = Column(String)
    product_description = Column(String)



Base.metadata.create_all(bind=engine) #creates the database