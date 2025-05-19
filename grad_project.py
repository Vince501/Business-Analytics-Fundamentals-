# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 18:37:15 2025

@author: Vinny
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("CSV files/Flats_Resale_Prices.csv")

# Data Exploration
print(df.info())

# describe(include='all') including categorical
print(df.describe(include='all')) 

# Checking Null Values
print(df.isnull().sum())

# Convert 'month' to datetime and calculate flat age
df["month"] = pd.to_datetime(df["month"])
df["flat_age"] = 2025 - df["lease_commence_date"]

# Set seaborn style
sns.set(style="whitegrid")

# 1. Average Resale Price Over Time
plt.figure(figsize=(12, 6))
df.groupby("month")["resale_price"].mean().plot()
plt.title("Average Resale Price Over Time")
plt.ylabel("Average Resale Price ($)")
plt.xlabel("Month")
plt.tight_layout()
plt.show()

# 2. Resale Price Distribution by Flat Type
plt.figure(figsize=(10, 6))
sns.boxplot(x="flat_type", y="resale_price", data=df)
plt.title("Resale Price Distribution by Flat Type")
plt.ylabel("Resale Price ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Average Floor Area by Flat Model
plt.figure(figsize=(12, 6))
model_avg = df.groupby("flat_model")["floor_area_sqm"].mean().sort_values()
sns.barplot(x=model_avg.values, y=model_avg.index)
plt.title("Average Floor Area by Flat Model")
plt.xlabel("Floor Area (sqm)")
plt.tight_layout()
plt.show()

# 4. Number of Resale Transactions by Town
plt.figure(figsize=(10, 12))
town_counts = df["town"].value_counts().sort_values()
sns.barplot(x=town_counts.values, y=town_counts.index)
plt.title("Number of Resale Transactions by Town")
plt.xlabel("Number of Transactions")
plt.tight_layout()
plt.show()

# 5. Resale Price vs Floor Area
plt.figure(figsize=(10, 6))
sns.scatterplot(x="floor_area_sqm", y="resale_price", data=df, alpha=0.3)
plt.title("Resale Price vs Floor Area")
plt.xlabel("Floor Area (sqm)")
plt.ylabel("Resale Price ($)")
plt.tight_layout()
plt.show()

# 6. Flat Age vs Resale Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x="flat_age", y="resale_price", data=df, alpha=0.3)
plt.title("Flat Age vs Resale Price")
plt.xlabel("Flat Age (years)")
plt.ylabel("Resale Price ($)")
plt.tight_layout()
plt.show()
