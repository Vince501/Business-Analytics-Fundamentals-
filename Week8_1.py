# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:34:23 2025

@author: Vincent Mutungi
"""

import pandas as pd

# Dates
df = pd.read_csv('Class files\DQ-Example-Dates.csv', index_col='id')
df.info()

df['date_clean'] = df['date'].str.replace(r'[^0-9/-]','', regex=True)
df[['date', 'date_clean']]

df['date_clean2'] = pd.to_datetime(df['date_clean'], errors='coerce')
df

dfnona = df.dropna(subset=['date_clean2'])
dfnona

# Categories
df2 = pd.read_csv('Class files\DQ-Example-Category.csv', index_col='id')
df2

df2.children.unique()
df2['children_clean'] = df2.children.str.lower()
df2[['children', 'children_clean']]
df2['children_clean2'] = df2.children_clean.map({'y':1, 'n':0})
df2[['children', 'children_clean2']]
df2.children_clean2.astype('category')

df2['gender_clean'] = df2.gender.str.lower()
df2['gender_clean2'] = df2.gender_clean.str[0]
df2.gender_clean2.astype('category')
df2[['gender', 'gender_clean2']]
df2.info()

df2['age_range'] = pd.cut(df2.age, [0,18,21,30,100],labels=['<19', '19-21', '22-30', '31+'])
df2[['age','age_range']]











