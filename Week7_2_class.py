# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:29:37 2025

@author:Vincent Mutungi
"""

import pandas as pd
data = pd.read_csv('Class files\DQ-Example-Numeric.csv')
data.info()
data.taxrate.dtype
data.id.dtype
data['salary'].dtype

def lowValuesToNone(x):
    if x<18:
        return None
    else:
        return x
    
data['age_clean'] = data['age'].apply(lowValuesToNone)
# data['age_clean'] = data['age'].apply(lambda x: None if x < 18 else x)
data['age_clean'] = data['age_clean'].round()

def noNegativeChildren(x):
    if x<0:
        return None
    else:
        return x
    
data['children_num_clean'] = data['children_num'].apply(noNegativeChildren)

data['taxrate_outlier'] = \
    data['taxrate'].apply(lambda x: True if x >= 100 else False)
data[['taxrate', 'taxrate_outlier']]

data['taxrate_decimal'] = data['taxrate'] / 100
data[['taxrate', 'taxrate_decimal']]