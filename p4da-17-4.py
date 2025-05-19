#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 4
# 
# *** requires datafile: measures2.csv

# In[1]:


import pandas as pd
measures = pd.read_csv('measures2.csv', index_col='#')
measures.head()


# In[2]:


early = measures.measure[0:35]
later = measures.measure[40:]


# In[3]:


type(early)


# In[4]:


import scipy.stats as stats
result = stats.ttest_ind(early, later)
round(result.pvalue,4)


# In[5]:


earlyVar = early.var()
round(earlyVar,4)


# In[6]:


laterVar = later.var()
round(laterVar,4)


# In[7]:


F = earlyVar/laterVar
round(F,4)


# In[8]:


pvalue = 1 -stats.f.cdf(F, len(early)-1,len(later)-1)
round(pvalue, 4)


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
