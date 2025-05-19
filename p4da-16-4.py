#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 16, section 4
# 
# *** requires datafile: cars_sales.csv

# In[1]:


import pandas as pd
dfsales = pd.read_csv('cars_sales.csv', index_col='Country')
dfsales


# In[2]:


dfsales /= 1000
dfsales


# In[3]:


pd.options.display.float_format = '{:,.0f}'.format
dfsales


# In[4]:


dfsales = dfsales.transpose()
dfsales.rename_axis(index='Year')
dfsales = dfsales.sort_index()
dfsales.iloc[:5, :5]


# In[5]:


dfsales.plot(kind='bar', stacked=True)


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


dfsales.plot(kind='bar', stacked=True)
plt.legend(loc='upper left', fontsize='x-small')
plt.show()


# In[8]:


dfsales.plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()


# In[9]:


dfsales.loc['2020'].plot(kind='pie')


# In[10]:


dfsales.loc['2017'].plot(kind='pie')


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
