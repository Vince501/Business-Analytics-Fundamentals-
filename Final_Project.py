# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 21:17:17 2025

@author: Vincent Mutungi
"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from CSV file
df = pd.read_csv('CSV files/Flats_Resale_Prices.csv')

# Describe the dataset
print('\n No. of Columns/Variables \t', len(df.columns),  '\n')  # Prints the number of columns
print('No. of Rows \t', len(df), '\n')  # Prints the number of rows
print(df.dtypes, '\n')  # Prints the data types of each column
print('No. of null values \n', df.isnull().sum(), '\n')  # Checks for null values in the dataset
df.info()  # Provides a summary of the dataset's columns, non-null counts, and data types
summary_stats = df.describe()  # Summarizes the numeric columns of the dataset
Q1 = summary_stats.iloc[4]
Q3 = summary_stats.iloc[6]

Q3 +1.5
Q1 - 1.5


# 1. Resale Price Trends Over Time
# Group by month and calculate average resale price for each month
monthly_price = df.groupby('month')['resale_price'].mean().reset_index()
# Plot the trend of average resale price over time
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_price, x='month', y='resale_price')
plt.title('Average Resale Price Over Time')
plt.xlabel('Month')
plt.ylabel('Average Resale Price (SGD)')
plt.show()
plt.savefig('Resale_Price_Trends_Over_Time.png')  # Save the plot as an image

# 2. Average Resale Price by Town
# Group by town and calculate average resale price for each town
town_price = df.groupby('town')['resale_price'].mean().sort_values(ascending=False)
# Plot the average resale price by town in a horizontal bar chart
plt.figure(figsize=(10,12))
town_price.sort_values(ascending=True).plot(kind='barh')  # Makes long town names easier to read
plt.title('Average Resale Price by Town')
plt.xlabel('Average Price (SGD)')
plt.ylabel('Town')
plt.show()
plt.savefig('Average_Resale_Price_by_Town.png')  # Save the plot as an image

# 3. Floor Area vs. Resale Price
# Create a scatter plot to visualize the relationship between floor area and resale price
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='floor_area_sqm', y='resale_price', alpha=0.5)
plt.title('Floor Area vs Resale Price')
plt.xlabel('Floor Area (sqm)')
plt.ylabel('Resale Price (SGD)')
plt.grid(True)
plt.show()
plt.savefig('Floor_Area_vs_Resale_Price.png')  # Save the plot as an image

# 4. Average Resale Price by Flat Model
# Group by flat model and calculate average resale price for each flat model
model_price = df.groupby('flat_model')['resale_price'].mean().sort_values(ascending=False)
# Plot the average resale price by flat model in a horizontal bar chart
plt.figure(figsize=(12,8))
model_price.sort_values(ascending=True).plot(kind='barh')
plt.title('Average Resale Price by Flat Model')
plt.xlabel('Average Resale Price (SGD)')
plt.ylabel('Flat Model')
plt.show()
plt.savefig('Average_Resale_Price_by_Flat_Model.png')  # Save the plot as an image

# 5. Price Distribution by Flat Type
# Create a boxplot to show the distribution of resale prices by flat type
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='flat_type', y='resale_price')
plt.title('Resale Price Distribution by Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Resale Price (SGD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
plt.savefig('Price_Distribution_by_Flat_Type.png')  # Save the plot as an image

# 6. Resale Price vs Flat Size Category
# Step 1: Categorize floor area into size categories
def map_flat_size(area):
    if area < 70:
        return '1 - Small'
    elif area <= 100:
        return '2 - Medium'
    else:
        return '3 - Large'
df['Flat_Size_Category'] = df['floor_area_sqm'].apply(map_flat_size)  # Apply the categorization function
# Step 2: Create a pivot table for counting the number of flats in each Town and Flat Size Category
df_pivot = df.pivot_table(values='resale_price', index='town', columns='Flat_Size_Category', aggfunc='count', fill_value=0)
# Step 3: Plot the number of flats by town and flat size category
df_pivot.plot(kind='bar', figsize=(20,8))
plt.title('Number of Flats by Town and Flat Size Category')
plt.xlabel('Town')
plt.ylabel('Number of Flats')
plt.xticks(rotation=90)
plt.legend(title='Flat Size', loc='upper right')
plt.grid(True, axis='y', alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig('Resale_Price_vs_Flat_Size_Category.png')  # Save the plot as an image

# 7. Distribution of Flat Types
# Count the occurrences of each flat size category
flat_type_counts = df['Flat_Size_Category'].value_counts()
# Plot the distribution of flat types using a pie chart
plt.figure(figsize=(8, 8))
flat_type_counts.plot(kind='pie')
plt.title('Distribution of Flats by Size Category')
plt.ylabel('')  # Hide y-label to keep it clean
plt.tight_layout()
plt.show()
plt.savefig('Distribution_of_Flat_Types.png')  # Save the plot as an image

# 8. Number of Flats by Lease Commence Date
# Step 1: Extract Year from Lease Commence Date
df['lease_commence_year'] = df['lease_commence_date'].astype(str).astype(int)  # Convert to integer
# Step 2: Plot the count of flats by lease commence year
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='lease_commence_year', order=sorted(df['lease_commence_year'].unique()))
plt.title('Number of Flats by Lease Commence Year')
plt.xlabel('Lease Commence Year')
plt.ylabel('Number of Flats')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('Number_of_Flats_by_Lease_Commence_Date.png')  # Save the plot as an image

# 9. Distribution of Resale Prices
# Create a histogram to visualize the distribution of resale prices
plt.figure(figsize=(10, 6))
plt.hist(df['resale_price'], bins=50, color='blue', alpha=0.7)
plt.title('Distribution of Resale Prices')
plt.xlabel('Resale Price (SGD)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('Distribution_of_Resale_Prices.png')  # Save the plot as an image

# Testing Skewness and Kurtosis
print('Skewness=', round(df.resale_price.skew(),2))
print('Kurtosis=', round(df.resale_price.kurt(),2))
import scipy.stats as stats
print('Skewness test p-value:',
round(stats.skewtest(df.resale_price).pvalue, 4))
print('Kurtosis test p-value:',
round(stats.kurtosistest(df.resale_price).pvalue, 4))

# 10. Proportion of Flat Sizes by Town
# Step 1: Create a pivot table for flat size proportions
df_pivot_size = df.pivot_table(values='resale_price', index='town', columns='Flat_Size_Category', aggfunc='count')
# Step 2: Sort the pivot table by the total count of flats for each town in descending order
df_pivot_size['Total_Flats'] = df_pivot_size.sum(axis=1)  # Calculate total flats for each town
df_pivot_size_sorted = df_pivot_size.sort_values(by='Total_Flats', ascending=False)  # Sort the towns
# Step 3: Plot the stacked bar chart of flat size proportions
df_pivot_size_sorted.drop(columns='Total_Flats').plot(kind='bar', stacked=True, figsize=(20, 8)) # Set title and labels
plt.title('Proportion of Flat Sizes by Town')
plt.xlabel('Town')
plt.ylabel('Number of Flats')
plt.tight_layout()
plt.show() # Show the plot
plt.savefig('Proportion_of_Flat_Sizes_by_Town.png')  # Save the plot as an image

# 11. Lease Commence Year vs. Resale Price
plt.figure(figsize=(16, 8))
sns.boxplot(data=df, x='lease_commence_year', y='resale_price')
plt.title('Resale Price by Lease Commence Year')
plt.xlabel('Lease Commence Year')
plt.ylabel('Resale Price (SGD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, axis='y', alpha=0.5)
plt.show()
plt.savefig('Resale_Price_by_Lease_Commence_Year.png')

# 12. Remaining Lease vs Resale Price
# Step 1: Calculate remaining lease from lease_commence_year
df['remaining_lease_years'] = 99 - (2025 - df['lease_commence_date'])
lease_vs_price = df.groupby('remaining_lease_years')['resale_price'].mean().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=lease_vs_price, x='remaining_lease_years', y='resale_price', marker='o')
plt.title('Average Resale Price vs. Remaining Lease Duration')
plt.xlabel('Remaining Lease (Years)')
plt.ylabel('Average Resale Price (SGD)')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('Avg_Resale_Price_vs_Remaining_Lease_Years.png')
