# -*- coding: utf-8 -*-
"""
Data Visualization Example
Visualizing multiple variables to explore
potential relationships between variables.
@author: chad.birger
"""
# Objective
# Teach students how to identify, visualize, and interpret relationships between:
# •	Two quantitative variables
# •	Two categorical variables
# •	One quantitative and one categorical variable
# The lesson includes explanations, code examples, common mistakes, and mini practice tasks.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
tips = sns.load_dataset("tips")
penguins = sns.load_dataset("penguins")

# Explore how two continuous/numeric variables move together. Is there correlation? Linear trend? 
# Best Visualizations:
# •	Scatter Plot
# •	Regression Plot
# •	Hexbin (for dense data)
# •	Correlation Heatmap (for multiple quantitative vars)
# Example 1: tips Dataset
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title("Tip vs Total Bill")
plt.show()
sns.lmplot(data=tips, x='total_bill', y='tip', line_kws={'color': 'red'})

# Mini Practice: Use the penguins dataset. 
#Plot body_mass_g vs flipper_length_mm. Is there a linear trend?
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm')
plt.title("body_mass_g vs flipper_length_mm")
plt.show()
sns.lmplot(data=penguins, x='body_mass_g', y='flipper_length_mm', line_kws={'color': 'red'})

# Step 2: Categorical vs Categorical
# Goal:
# See how categories relate. Are they independent? Is one more frequent with another?
# Best Visualizations:
# •	Grouped Bar Plot
# •	Count Plot (stacked/grouped)
# •	Heatmap of Crosstab
# Example 1: tips Dataset – Sex vs Smoking Status
# Using the seaborn package on unsummarized data
sns.countplot(data=tips, x='sex', hue='smoker')
plt.title("Smoking Status by Gender")
plt.show()
# Now using the .plot() method on summarized pandas dataframe
tips_sub = tips[["sex", "smoker"]]
tips_sub = tips_sub.reset_index()
SmokingPivot = tips_sub.pivot_table(values = 'index', index = 'sex', columns='smoker', aggfunc = 'count')
SmokingPivot.plot(kind='bar')
SmokingPivot.plot(kind='bar', stacked=True)

# Mini Practice: Use penguins — visualize the relationship between island and species.
sns.countplot(data=penguins, x='island', hue='species')
plt.title("Species by Island")
plt.show()

penguins_sub = penguins[["island", "species"]]
penguins_sub = penguins_sub.reset_index()
Pivot = penguins_sub.pivot_table(values = 'index', index = 'island', columns='species', aggfunc = 'count')
Pivot.plot(kind='bar')
Pivot.plot(kind='bar', stacked=True)


# Step 3: Categorical vs Quantitative
# Goal:
# Compare distributions of a numeric variable across groups. Are the means different? Is the spread wider in one group?
# Best Visualizations:
# •	Box Plot
# •	Bar Plot (for means with CI)
# Example 1: tips Dataset – Tip by Day
# Using Seaborn library on raw data set
sns.boxplot(data=tips, x='day', y='tip')
plt.title("Tip Distribution by Day")
plt.show()
sns.barplot(data=tips, x='day', y='tip', ci=95)


# Mini Practice: Compare body_mass_g across penguin species. Which species is heavier?
sns.boxplot(data=penguins, x='species', y='body_mass_g')
plt.title("Compare body_mass_g across penguin species")
plt.show()
sns.barplot(data=penguins, x='species', y='body_mass_g', ci=95)