#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 6
#
# *** requires datafile: USIX.csv

# In[1]:


import pandas as pd
ticker = 'Class files/USIX'
filename = ticker + '.csv'
df = pd.read_csv(filename, index_col='Date', parse_dates=True)


# In[2]:


df = df[['AdjustedClose']]
df['Return'] = df['AdjustedClose'].pct_change()
df.head()


# In[3]:


df = df[1:]


# In[4]:


df['Return'].plot(kind='hist', bins=50)


# In[5]:


print('Skewness=', round(df.Return.skew(),2))
print('Kurtosis=', round(df.Return.kurt(),2))


# In[6]:


import scipy.stats as stats
print('Skewness test p-value:',
round(stats.skewtest(df.Return).pvalue, 4))
print('Kurtosis test p-value:',
round(stats.kurtosistest(df.Return).pvalue, 4))
summary_stats = df.describe()  # Summarizes the numeric columns of the dataset
Q1 = summary_stats.iloc[4]
Q3 = summary_stats.iloc[6]

IQR = Q3 - Q1
upper_bound = Q3 + 1.5*IQR
lower_bound = Q1 - 1.5*IQR
print('\n IQR: ', IQR)
print('\n upper_bound: ', upper_bound)
print('\n lower_bound: ', lower_bound)

outliers = df[(df.Return < lower_bound) | (df.Return > upper_bound)]

# In[7]:


sd = df.Return.std()
round(sd, 3)


# In[8]:


df[df.Return > (sd*3)]


# In[9]:


df[df.Return < (-sd*3)]


# In[10]:


outliers = df[(df.Return < (-3*sd)) | (df.Return > (3*sd))]


# In[11]:


import matplotlib.pyplot as plt
plt.scatter(x=outliers.index, y=outliers.Return)
plt.xticks(rotation = 45)
plt.show()


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
