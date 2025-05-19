#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 16, sections 7 and 8
#
# *** requires datafile: members.csv

# In[1]:


import pandas as pd
dfmembers = pd.read_csv('Class files/members.csv', parse_dates=['visitDate', 'endDate'])


# In[2]:


dfmembers.head()


# In[3]:


dfmembers.info()
stats = dfmembers.describe()

# In[4]:


len(dfmembers[dfmembers.status=='active'])


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

# In[6]:


sns.countplot(data=dfmembers, x='married')
plt.show()

# In[7]:


sns.countplot(data=dfmembers, y='gender')
plt.show()

# In[8]:


sns.countplot(data=dfmembers, x='age')
plt.show()

# In[9]:


import matplotlib.pyplot as plt
g = sns.countplot(data=dfmembers, x='age')
for label in g.get_xticklabels():
   visible = int(label.get_text()) % 10 == 0
   label.set_visible(visible)
g


# In[10]:


sns.displot(dfmembers.age, bins=15)
plt.show()

# In[11]:


g = sns.FacetGrid(dfmembers, col='pool', height=5)
g = g.map(sns.histplot, 'age')
plt.show()

# In[12]:


len(dfmembers[(dfmembers.gym == 'y') & (dfmembers.pool == 'y')])


# In[13]:


sns.scatterplot(x=dfmembers.visitDate, y=dfmembers.age)
plt.show()

# In[14]:


dfmembers['year'] = dfmembers.visitDate.dt.year
dfmembers.head()


# In[15]:


dfmembers.pivot_table(values='guestID', index='year', aggfunc='count')


# In[16]:


dfByGender = dfmembers.pivot_table(values='guestID', index='year',
                                   columns='gender', aggfunc='count')
dfByGender


# In[17]:


dfByGender['pctFemale'] = round(dfByGender.F /(dfByGender.F + dfByGender.M) * 100)
dfByGender


# In[18]:


sns.barplot(data=dfByGender, x=dfByGender.index, y='pctFemale')
plt.show()

# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
