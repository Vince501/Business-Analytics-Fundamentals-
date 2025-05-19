#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 1
# 
# *** requires datafile: attendance.csv

# In[1]:


midterms = [99, 85, 98, 72, 89]


# In[2]:


sum(midterms) / len(midterms)


# In[3]:


finals = [88, None, 99, 81, 91]
sum(finals) / len(finals)


# In[4]:


import numpy as np
finals = [88, np.nan, 99, 81, 91]


# In[5]:


sum(finals) / len(finals)


# In[6]:


np.nanmean(finals)


# In[7]:


# create a DataFrame of test scores
import pandas as pd
scores = pd.DataFrame({'midterm': [99, 85, 98, 72, 89],
                       'final':[88, None, 99, 81, 91]},
                        index=['Stefanie', 'Adam', 'Becca', 'John', 'Jane']
)
scores


# In[8]:


scores.midterm.mean()


# In[9]:


scores.midterm.median()


# In[10]:


scores.final.mean()


# In[11]:


scores.final.median()


# In[12]:


scores.mean()


# In[13]:


scores.median()


# In[14]:


scores.mean(axis='columns')


# In[15]:


scores.final.var(ddof=0)


# In[16]:


scores.std(axis='rows', ddof=0)


# In[17]:


attendance = pd.read_csv('Class files/attendance.csv', index_col='student')
attendance


# In[18]:


attendance.week1.map({'y':1,'n':0})


# In[19]:


for i in range(1, 5):
   week = 'week' + str(i)
   attendance[week] = attendance[week].map({'y':1,'n':0})
attendance


# In[20]:


attendance.sum(axis='columns') / len(attendance.columns) * 100

attendance.sum(axis='rows') / len(attendance.columns) * 100

# In[21]:


attendance.sum(axis='rows') / len(attendance) * 100


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
