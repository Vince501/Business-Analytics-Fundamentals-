# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 12:42:52 2025

@author: Chief Principal
"""

# Asks for two variable, one file and read the lines and then print it out to the second file

f1 = open('a.txt', 'w')

print('Class Group Assignment', file=f1)
f1.close()

def fileCopy(a,b):
    f1 = open(a)
    contents = f1.read()
    f1.close
    
    f2 = open(b, 'w')
    print(contents, file = f2)
    f2.close()
    
fileCopy('a.txt', 'b.txt')

##
import pandas as pd
df = pd.read_csv('popgdp.csv')
df
    
df['gdppercap'] = round(df.gdp / df.population * 1000000)
df

gdppercap = df.pivot(index='year', columns='country', values='gdppercap')
gdppercap
g2 = gdppercap.transpose()

#
df1 = pd.read_csv('gdp.csv')
df1
df1.melt(id_vars='year', var_name='country')
