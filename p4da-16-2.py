#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 16, section 2
# 
# *** requires datafile: cars_pct.csv

# In[1]:


import pandas as pd
dfpct = pd.read_csv('cars_pct.csv', index_col='Country')


# In[2]:


dfpct.head()


# In[3]:


dfsales = pd.read_csv('cars_sales.csv', index_col='Country')


# In[4]:


dfsales


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
