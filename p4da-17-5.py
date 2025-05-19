#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 5
# 
# *** requires datafile: measures2.csv

# In[1]:


import numpy as np
# the first 5 weight measures
data = [10.11, 9.85, 10.09, 10.03, 10.51]
mean = np.mean(data)
round(mean,3)


# In[2]:


import scipy.stats as stats
confint = stats.t.interval(alpha=0.95, df=len(data)-1,loc=mean, scale=stats.sem(data))
confint


# In[3]:


def confinterval(x, conf=.95, decimals=None):
   result = stats.t.interval(alpha=conf, df=len(x)-1,
                             loc=np.mean(x), scale=stats.sem(x))
   if decimals != None:
      result = (round(result[0], decimals), round(result[1], decimals))
   return result


# In[4]:


import pandas as pd
measures = pd.read_csv('measures2.csv', index_col='#')
measures.head()


# In[5]:


early = measures.measure[0:35].tolist()
later = measures.measure[40:].tolist()


# In[6]:


confinterval(early, decimals=3)


# In[7]:


for conf in (.9, .95, .99):
   print(conf, confinterval(later, conf=conf, decimals=3))


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
