import pandas as pd
import sqlite3

df = pd.read_csv('heart.csv', sep=";")

"""Establish a connection to a salite3 database and create a table in that database"""
conn = sqlite3.connect('itdaadb.db')
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE heart_patient(
                age INT , 
                sex BOOLEAN,
                cp INT, 
                trestbps INT, 
                chol INT, 
                fbs BOOLEAN, 
                restecg INT,
                thalach INT,
                exang BOOLEAN,
                oldpeak REAL,
                slope INT,
                ca INT,
                thal INT, 
                target BOOLEAN
                )''')
    print("Table now created")
except: 
  print("Table already exists")    

df.to_sql('heart_patient',conn,if_exists='append',index=False)