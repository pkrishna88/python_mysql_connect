import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import getpass

username = input("username: ")
password = getpass.getpass("password: ")
#print(password)
hostname = "localhost"
database_name = input("database_name: ")

l = 'mysql+pymysql://{username}:{password}@{hostname}'.format(username=username, password=password, hostname=hostname)

sql_engine       = create_engine(l, pool_recycle=3600)

db_connection    = sql_engine.connect()

df           = pd.read_sql("select * from bookshelf.aae_calls_data", db_connection);

#pd.set_option('display.expand_df_repr', False)

print(df)

db_connection.close()
