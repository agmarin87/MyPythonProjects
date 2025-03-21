# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:46:12 2025

@author: Antonio
"""

## setup the working directory
import os
os.chdir(r"C:\Users\Antonio\my_projects\my_database_dbt\my_database_dbt")

# setup the connection and creates the database, if it does not exist 
import duckdb
conn = duckdb.connect(database='./dev.duckdb', read_only=False)

#To see the tables I have
query = "SELECT table_name FROM information_schema.tables WHERE table_schema='main';"
tables = conn.execute(query).fetchall()
print(tables)

## query the table
df = conn.sql("select * from fact_orders").df()
print(df)