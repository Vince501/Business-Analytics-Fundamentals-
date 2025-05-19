# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 19:33:06 2025

@author: Vinny
"""

import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Load dataset
df = pd.read_csv("DataImports_2025/backup_data.csv")  # Read CSV into DataFrame

# Data Exploration
print(df.info())  # Display data types and non-null counts
print(df.describe(include='all'))  # Summary statistics for all columns
print(df.isnull().sum())  # Display count of missing values for each column

# Data Cleaning and Feature Engineering
df["month"] = pd.to_datetime(df["month"])  # Convert 'month' column to datetime format
df["flat_age"] = 2025 - df["lease_commence_date"]  # Calculate flat age by subtracting lease start year from 2025
df["lease_commence_year"] = df["lease_commence_date"].astype(str)  # Convert lease year to string for categorical plotting

# Average Resale Price Over Time
plt.figure(figsize=(12, 6))  # Set plot size to 12x6 inches
df.groupby("month")["resale_price"].mean().plot(kind='line')  # Plot average resale price per month as a line
plt.title("Average Resale Price Over Time")  # Set plot title
plt.ylabel("Average Resale Price ($)")  # Set y-axis label
plt.xlabel("Month")  # Set x-axis label
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()  # Display the plot

# Average Resale Price Over Time by Flat Type
plt.figure(figsize=(14, 6))  # Set figure size
# Group data by month and flat_type, compute mean resale price
grouped_ftype = df.groupby(["month", "flat_type"])["resale_price"].mean().unstack()
# Plot each flat_type as a separate line
grouped_ftype.plot(kind='line', figsize=(14, 6))  # Multi-line plot
plt.title("Average Resale Price Over Time by Flat Type")  # Set title
plt.ylabel("Average Resale Price ($)")  # Set y-axis label
plt.xlabel("Month")  # Set x-axis label
plt.legend(title="Flat Type", bbox_to_anchor=(1.05, 1), loc='upper left')  # Position legend outside the plot
plt.tight_layout()  # Adjust layout
plt.show()  # Display plot

# Resale Price Distribution by Flat Type
plt.figure(figsize=(10, 6))  # Set plot size to 10x6 inches
flat_types = df["flat_type"].unique()  # Extract unique flat types
# Create a list of resale prices grouped by flat type
data = [df[df["flat_type"] == ft]["resale_price"] for ft in flat_types]
plt.boxplot(data, labels=flat_types)  # Create a boxplot for each flat type
plt.title("Resale Price Distribution by Flat Type")  # Set plot title
plt.ylabel("Resale Price ($)")  # Set y-axis label
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot

# Average Floor Area by Flat Model
plt.figure(figsize=(12, 6))  # Set plot size
model_avg = df.groupby("flat_model")["floor_area_sqm"].mean().sort_values()  # Compute mean floor area per flat model
model_avg.plot(kind='barh')  # Create a horizontal bar plot
plt.title("Average Floor Area by Flat Model")  # Set plot title
plt.xlabel("Floor Area (sqm)")  # Set x-axis label
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot

# Number of Resale Transactions by Town
plt.figure(figsize=(10, 12))  # Set plot size
town_counts = df["town"].value_counts().sort_values()  # Count transactions per town and sort
town_counts.plot(kind='barh')  # Create horizontal bar plot
plt.title("Number of Resale Transactions by Town")  # Set plot title
plt.xlabel("Number of Transactions")  # Set x-axis label
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot

# Resale Price vs Floor Area
plt.figure(figsize=(10, 6))  # Set plot size
df.plot(kind='scatter', x="floor_area_sqm", y="resale_price", alpha=0.3)  # Scatter plot with transparency
plt.title("Resale Price vs Floor Area")  # Set plot title
plt.xlabel("Floor Area (sqm)")  # Set x-axis label
plt.ylabel("Resale Price ($)")  # Set y-axis label
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot

# Flat Age vs Resale Price
plt.figure(figsize=(10, 6))  # Set plot size
df.plot(kind='scatter', x="flat_age", y="resale_price", alpha=0.3)  # Scatter plot of flat age vs price
plt.title("Flat Age vs Resale Price")  # Set plot title
plt.xlabel("Flat Age (years)")  # Set x-axis label
plt.ylabel("Resale Price ($)")  # Set y-axis label
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot

# Resale Price by Lease Commencement Year (All Years) ---
plt.figure(figsize=(16, 6))  # Set plot size
years = sorted(df["lease_commence_year"].unique())  # Get all unique lease years and sort them
# Create a list of resale prices for each lease year
data = [df[df["lease_commence_year"] == year]["resale_price"] for year in years]
plt.boxplot(data, labels=years)  # Create boxplot for each lease year
plt.title("Resale Price by Lease Commencement Year (All Years)")  # Set plot title
plt.ylabel("Resale Price ($)")  # Set y-axis label
plt.xlabel("Lease Commencement Year")  # Set x-axis label
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot