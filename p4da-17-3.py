#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 3
# 
# *** requires datafiles: measures2.csv, USIX.csv

# In[1]:


import pandas as pd
measures = pd.read_csv('measures2.csv', index_col='#')
measures.head()


# In[2]:


measures.plot()


# In[3]:


measures['measure'].rolling(10).mean().head(12)


# In[4]:


measures['ten'] = 10
measures['ten'].plot()
measures['measure'].rolling(10).mean().plot()


# In[5]:


usix = pd.read_csv('USIX.csv', index_col='Date', parse_dates=True)
usix.head()


# In[6]:


usix = usix[['AdjustedClose']]
usix['Return'] = usix['AdjustedClose'].pct_change()
usix.head()


# In[7]:


usix['Return'].rolling(20).std().plot()


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
