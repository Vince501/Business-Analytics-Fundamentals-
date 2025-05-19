#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 16, section 3
# 
# *** requires datafile: cars_pct.csv

# In[1]:


import pandas as pd
dfpct = pd.read_csv('cars_pct.csv', index_col='Country')


# In[2]:


dfpct.plot()


# In[3]:


dfpct = dfpct.transpose()


# In[4]:


dfpct.iloc[:5, :5]


# In[5]:


dfpct.index.name = 'Year'
dfpct.iloc[:5, :5]


# In[6]:


dfpct.plot()


# In[7]:


dfpct = dfpct.sort_index()
dfpct.iloc[:5, :5]


# In[8]:


dfpct.plot()


# In[9]:


dfpct[['Iceland', 'Sweden', 'Netherlands']].plot()


# In[10]:


dfpct[['China', 'Japan', 'Australia', 'New Zealand']].plot()


# In[11]:


dfpct[['China', 'Japan', 'Australia', 'New Zealand']].plot(kind='bar')


# In[12]:


dfpct.iloc[-1].plot(kind='barh')


# In[13]:


dfpct.iloc[-1].sort_values(ascending=True).plot(kind='barh')


# In[14]:


dfpct.iloc[-1].dropna().sort_values(ascending=True).plot(kind='barh')


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
