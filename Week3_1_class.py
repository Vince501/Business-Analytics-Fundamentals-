# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:36:08 2025

@author: Vincent Mutungi
"""
#Accessing Unstructured Data
inFile = open('Duplicates.txt')
inFile.read()
inFile.close()

inFile = open('Duplicates.txt')
dups = inFile.read()

inFile = open('Duplicates.txt')
dups_1 = inFile.readline()
inFile.close()

inFile = open('Duplicates.txt')
dups_2 = inFile.readlines()
inFile.close()


#Accessing Structured Data
import pandas as pd
example1_csv = pd.read_csv('Example1.csv')
example2_csv = pd.read_csv('Example1.csv', sep='|')
