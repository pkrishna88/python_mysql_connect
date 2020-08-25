import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import getpass

database_name = input("database_name: ")
table_name = input("table_name: ") #'aae_calls_data"
host_name = "localhost"
username = input("username: ")
password = getpass.getpass("password: ")
pool_recycle = 3600

l = 'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'.format(username=username,password=password, host_name=host_name, database_name=database_name)

sql_engine = create_engine(l, pool_recycle=pool_recycle)

db_connect = sql_engine.connect()

file_name = input("file_name: ")

try:
  df = pd.read_csv(file_name)
except:
  df = pd.read_excel(file_name)
else:
  print("df cannot be created!!")
finally:
  print("df has been created!!")

try:
  frame = df.to_sql(table_name, db_connect, if_exists='fail')
except ValueError as vx:
  print(vx)
except Exception as ex:
  print(ex)
else:
  print("the table %s has been created successfully!"%table_name)
finally:
  db_connect.close()



