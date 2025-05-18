# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 20:28:22 2025

@author: Vinny
"""

# Importing package using SQLite3
import sqlite3 as db
import pandas as pd

sql2 = "SELECT * FROM tracks"
sql3 = "SELECT * FROM albums ORDER BY Title ASC"
sql4 = "SELECT EmployeeId, FirstName, LastName, Title FROM employees"
sql5 = "SELECT * FROM artists WHERE name like 'A%'"
sql6 = "SELECT * FROM artists ORDER BY name DESC"
sql7 = "SELECT * FROM tracks WHERE UnitPrice = 1.99"
sql8 = "SELECT * FROM tracks WHERE UnitPrice != 1.99"

# =============================================================================
# Task 1: Use the database chinook.db
# =============================================================================
# Connect to datababe
conn = db.connect('SQL Files/chinook.db')
# Create cursor
cur = conn.cursor()

# =============================================================================
# Question 2. Write a SQL statement to display all rows and columns from the tracks table.
# SELECT * FROM tracks;
# =============================================================================
# Now can run SQL code
# Cur.execute will run the code using the query
cur.execute(sql2)
# Getting the result from the cursor
# Using cur.fetchall() command
results = cur.fetchall()
# Create new dataframe to store results
df2 = pd.DataFrame(results)
# Get column names using the following;
fieldnames = []
for col in cur.description:
    fieldnames.append(col[0])
# Add column names/headers
df2.columns = fieldnames
df2.set_index('TrackId', inplace=True)
print(df2)

# =============================================================================
# Question 3. Write a SQL statement to display all rows and columns from the albums table, sorted alphabetically (A-Z) by title.
# SELECT * FROM albums ORDER BY Title ASC;
# =============================================================================
cur.execute(sql3)
# Getting the result from the cursor
# Using cur.fetchall() command
results = cur.fetchall()
# Create new dataframe to store results
df3 = pd.DataFrame(results)
# Get column names using the following;
fieldnames = []
for col in cur.description:
    fieldnames.append(col[0])
# Add column names/headers
df3.columns = fieldnames
df3.set_index('AlbumId', inplace=True)
print(df3)

# =============================================================================
# Question 4. Write a SQL statement to display EmployeeID, FirstName, LastName, and Title from the employees table.
# SELECT EmployeeId, FirstName, LastName, Title FROM employees;
# =============================================================================
cur.execute(sql4)
# Getting the result from the cursor
# Using cur.fetchall() command
results = cur.fetchall()
# Create new dataframe to store results
df4 = pd.DataFrame(results)
# Get column names using the following;
fieldnames = []
for col in cur.description:
    fieldnames.append(col[0])
# Add column names/headers
df4.columns = fieldnames
df4.set_index('EmployeeId', inplace=True)
print(df4)

# =============================================================================
# Question 5. Write a SQL statement to display all artists that begin with the letter “A”
# SELECT * FROM artists WHERE name like 'A%';
# =============================================================================
df5 = pd.read_sql_query(sql5, conn)
print(df5)

# =============================================================================
# Question 6. Write a SQL statement to display all artists sorted in descending order by name.
# SELECT * FROM artists ORDER BY name DESC;
# =============================================================================
df6 = pd.read_sql_query(sql6, conn)
print(df6)

# =============================================================================
# Question 7. Write a SQL statement to display all tracks (all columns) that have a UnitPrice of 1.99.
# SELECT * FROM tracks WHERE UnitPrice = 1.99;
# =============================================================================
df7 = pd.read_sql_query(sql7, conn)
print(df7)

# =============================================================================
# Question 8. Write a SQL statement to display all tracks (all columns) that have a UnitPrice other than 1.99.
# SELECT * FROM tracks WHERE UnitPrice != 1.99;
# =============================================================================
df8 = pd.read_sql_query(sql8, conn)
print(df8)

## close connection
conn.close()