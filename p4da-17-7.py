#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 17, section 7
# 
# *** requires datafiles: ORNG.csv, USIX.csv

# In[1]:


import pandas as pd
stockSymbol = 'ORNG'
stock = pd.read_csv(stockSymbol+'.csv', index_col='Date', parse_dates=True,
                    usecols=['Date', 'AdjustedClose'])
stock.columns = ['Stock_Adj_Close']
stock.head()


# In[2]:


marketSymbol = 'USIX'
market = pd.read_csv(marketSymbol+'.csv', index_col='Date', parse_dates=True,
                     usecols=['Date', 'AdjustedClose'])
market.columns = ['Market_Adj_Close']
market.head()


# In[3]:


df = pd.concat([stock, market], axis=1, join='inner')
df.head()


# In[4]:


df['Stock_Return'] = df['Stock_Adj_Close'].pct_change()
df['Market_Return'] = df['Market_Adj_Close'].pct_change()
df = df[1:] # drop the first row (return is NaN)
df.head()


# In[5]:


df.plot.scatter('Market_Return', 'Stock_Return', marker='.')


# In[6]:


from scipy.stats import linregress
beta, alpha, rvalue, pvalue, stderr =    linregress(df.Market_Return, df.Stock_Return)


# In[7]:


print('Beta:     ', round(beta,2))
print('Alpha:    ', round(alpha,2))
print('R-squared:', round(rvalue**2 * 100), '%')
print('pvalue:   ', round(pvalue, 4))
print('stderr:   ', round(stderr, 4))


# In[8]:


import matplotlib.pyplot as plt
plt.scatter(df.Market_Return, df.Stock_Return, marker='.')
plt.plot(df.Market_Return, alpha + beta*df.Market_Return, color='black')
plt.xlabel(marketSymbol)
plt.ylabel(stockSymbol)
plt.title('Daily Returns')
plt.show()


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
