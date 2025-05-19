#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 2
#
# *** requires datafile: sales.csv

# In[1]:


import pandas as pd
sales = pd.read_csv('Class files/sales.csv', parse_dates=['time'])


# In[2]:


sales.head()


# In[3]:


sales.pivot_table(values='count', index='product', aggfunc='sum')


# In[4]:


pd.set_option('display.precision', 1)
pivot = sales.pivot_table(values='count', index='product', aggfunc='mean')
pivot.columns = ['Avg # per Transaction']
pivot


# In[5]:


sales['quarter'] = sales['time'].dt.to_period('Q')
sales.head()


# In[6]:


sales.pivot_table(values='count', columns='quarter', aggfunc='sum')


# In[7]:


sales.pivot_table(values='count', index='product', columns='quarter',
                  aggfunc='sum')


# In[8]:

import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
pivot = sales.pivot_table(values='count', index='product', columns='quarter',
                          aggfunc='sum')
pivot.plot(kind='bar')
plt.show()

# In[9]:


sales.pivot_table(values='count', index=['region','product'],
                  columns='quarter', aggfunc='sum', margins=True)


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
