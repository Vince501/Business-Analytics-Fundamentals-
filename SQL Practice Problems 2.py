# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:58:34 2025

@author: Vinny
"""

# Importing package using SQLite3
import sqlite3 as db
import pandas as pd

sql1 = "SELECT * FROM tracks"
sql2 = "SELECT * FROM albums"
sql3 = "SELECT * FROM artists"
sql4 = '''SELECT al.title AS AlbumName, tr.name AS SongName 
            FROM tracks AS tr LEFT JOIN albums AS al ON tr.AlbumId = al.AlbumId
            ORDER BY AlbumName'''
sql5 = '''SELECT ar.Name AS ArtistName, al.Title AS AlbumName
FROM albums AS al LEFT JOIN artists AS ar ON al.ArtistId = ar.ArtistId
ORDER BY ar.Name'''
sql6 = '''SELECT ar.Name AS Artist, al.Title AS Album,  COUNT(tr.TrackId) AS TracksCount 
            FROM albums AS al
            LEFT JOIN tracks AS tr ON al.AlbumId = tr.AlbumId
            LEFT JOIN artists AS ar ON al.ArtistId = ar.ArtistId
            GROUP BY ar.Name, al.Title
            ORDER BY ar.Name'''

# Connect to datababe
conn = db.connect('SQL Files/chinook.db')

# call the read_sql_query() function, and get the resulting DataFrame
df1 = pd.read_sql_query(sql1, conn, index_col='TrackId')
print(df1)
df2 = pd.read_sql_query(sql2, conn, index_col='AlbumId')
print(df2)
df3 = pd.read_sql_query(sql3, conn, index_col='ArtistId')
print(df3)
df4 = pd.read_sql_query(sql4, conn)
print(df4)
df5 = pd.read_sql_query(sql5, conn)
print(df5)
FinalResults = pd.read_sql_query(sql6, conn)
print(FinalResults)
