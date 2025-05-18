# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 13:03:39 2025

@author: Vinny
"""
# Importing package using SQLite3
import sqlite3 as db
import pandas as pd

# Connect to datababe
conn = db.connect('SQL Files/dj.db')
## Create cursor
cur = conn.cursor()
### Now can run SQL code
### Cur.execute will run the code using the query
cur.execute("SELECT * FROM company WHERE ticker LIKE '%A%'")
#### Getting the result from the cursor
#### Using cur.fetchall() command
results = cur.fetchall()
##### Create new dataframe to store results
df1 = pd.DataFrame(results)
#### Get column names using the following;
fieldnames = []
for col in cur.description:
    fieldnames.append(col[0])
### Add column names/headers
df1.columns = fieldnames
df1.set_index('id', inplace=True)
## close connection
conn.close()

# Importing package using SQLite3
import sqlite3 as db
import pandas as pd
sql8 = ''' SELECT ticker_id, date, opening, high, low FROM daily_measures ORDER BY ticker_id, high DESC; '''
# Connect to datababe
conn = db.connect('SQL Files/dj.db')
df8 = pd.read_sql_query(sql8, conn)
### Close connection
conn.close()


















