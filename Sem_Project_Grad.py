# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:01:27 2025

@author: Vincent Mutungi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

# Load the dataset from CSV file
df = pd.read_csv('CSV files/Flats_Resale_Prices.csv')

#Describe the dataset
print('\n No. of Columns/Variables \t', len(df.columns),  '\n')
print('No. of Rows \t', len(df), '\n')
print(df.dtypes, '\n')
print('No. of null values \n', df.isnull().sum(), '\n')

df.info()
df.describe()

# Define function to categorize flat types into ranked groups
def order_flat_types(flat_type):
    # Assign ranking based on flat type for ordered visualization
    if flat_type == '2 ROOM':
        return '1 - 2 Room'
    elif flat_type == '3 ROOM':
        return '2 - 3 Room'
    elif flat_type == '4 ROOM':
        return '3 - 4 Room'
    elif flat_type == '5 ROOM':
        return '4 - 5 Room'
    else:
        return '5 - Executive'

# Apply flat type ranking to create a new column
df['Flat_Type_Ranking'] = df['flat_type'].apply(order_flat_types)

# Create pivot table to count flats by flat type ranking
# Aggregates resale_price counts for each Flat_Type_Ranking
df_pivot = df.pivot_table(values='resale_price', index='Flat_Type_Ranking', aggfunc='count')
# Rename column to 'Count' for clarity
df_pivot.rename(columns={'resale_price': 'Count'}, inplace=True)

# Plot 1: Bar plot of flat type counts
# Plot bar chart using pivot table data
df_pivot['Count'].plot(kind='bar', color='blue')
# Set plot title and labels
plt.title('Number of Flats by Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Count')
# Rotate x-axis labels for readability
plt.xticks(rotation=45)
# Add grid lines on y-axis
plt.grid(True, axis='y')
# Adjust layout to prevent label cutoff
plt.tight_layout()
# Display the plot
plt.show()

# Plot 2: Pie chart of flat type distribution
# Plot pie chart with percentage labels
df_pivot['Count'].plot(kind='pie')
# Set plot title
plt.title('Distribution of Flats by Flat Type')
# Remove y-label for cleaner appearance
plt.ylabel('')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Plot 3: Count plot of flat types using seaborn
# Create count plot with sorted Flat_Type_Ranking order
sns.countplot(data=df, x='Flat_Type_Ranking', order=sorted(df['Flat_Type_Ranking'].unique()))
# Set plot title and labels
plt.title('Count of Flats by Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Count')
# Rotate x-axis labels
plt.xticks(rotation=45)
# Add y-axis grid
plt.grid(True, axis='y')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Plot 4: Average resale price by town
# Calculate mean resale_price by town and sort in ascending order
avg_price_by_town = df.groupby('town')['resale_price'].mean().sort_values(ascending=True)
# Plot horizontal bar chart
avg_price_by_town.plot(kind='barh', color='green')
# Set plot title and labels
plt.title('Average Resale Price by Town')
plt.xlabel('Average Resale Price (SGD)')
plt.ylabel('Town')
# Add x-axis grid
plt.grid(True, axis='x')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Plot 5: Scatter plot of resale price vs floor area
# Create scatter plot with transparency for overlapping points
sns.scatterplot(data=df, x='floor_area_sqm', y='resale_price')
# Set plot title and labels
plt.title('Resale Price vs Floor Area')
plt.xlabel('Floor Area (sqm)')
plt.ylabel('Resale Price (SGD)')
# Add grid
plt.grid(True)
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Plot 6: Histogram of resale prices
# Plot histogram with 30 bins
df['resale_price'].plot(kind='hist', bins=30, color='gray', edgecolor='black')
# Set plot title and labels
plt.title('Distribution of Resale Prices')
plt.xlabel('Resale Price (SGD)')
plt.ylabel('Frequency')
# Add grid
plt.grid(True)
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Plot 7: Box plot of resale prices by flat type
# Create box plot with sorted Flat_Type_Ranking order
sns.boxplot(data=df, x='Flat_Type_Ranking', y='resale_price')
# Set plot title and labels
plt.title('Resale Price Distribution by Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Resale Price (SGD)')
# Rotate x-axis labels
plt.xticks(rotation=45)
# Add y-axis grid
plt.grid(True, axis='y')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Convert 'month' to datetime and extract year for time-based analysis
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
# Create 'year' column from month
df['year'] = df['month'].dt.year
# Create pivot table for average resale_price by year and Flat_Type_Ranking
df_pivot_year = df.pivot_table(values='resale_price', index='year', columns='Flat_Type_Ranking', aggfunc='mean')

# Plot 8: Stacked bar plot of average resale price by year and flat type
# Plot stacked bar chart
df_pivot_year.plot(kind='bar', stacked=True)
# Set plot title and labels
plt.title('Average Resale Price by Year and Flat Type')
plt.xlabel('Year')
plt.ylabel('Average Resale Price (SGD)')
# Adjust legend size and position
plt.legend(loc='upper left', fontsize='x-small')
# Add y-axis grid
plt.grid(True, axis='y')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Statistical Summary
# Calculate mean of resale_price
mean_price = df['resale_price'].mean()
# Calculate median of resale_price
median_price = df['resale_price'].median()
# Calculate population variance of resale_price
var_price = df['resale_price'].var(ddof=0)
# Calculate population standard deviation of resale_price
std_price = df['resale_price'].std(ddof=0)
# Print statistical summaries
print("Mean Resale Price: " + str(round(mean_price, 2)) + " SGD")
print("Median Resale Price: " + str(round(median_price, 2)) + " SGD")
print("Variance of Resale Price: " + str(round(var_price, 2)) + " SGD^2")
print("Standard Deviation of Resale Price: " + str(round(std_price, 2)) + " SGD")

# Distribution Analysis
# Calculate skewness to measure asymmetry of resale_price distribution
skewness = df['resale_price'].skew()
# Calculate kurtosis to measure tailedness of resale_price distribution
kurtosis = df['resale_price'].kurt()
# Print distribution metrics
print("Skewness of Resale Price: " + str(round(skewness, 2)))
print("Kurtosis of Resale Price: " + str(round(kurtosis, 2)))

# Time Series Analysis
# Create pivot table for average resale_price by year
yearly_avg = df.pivot_table(values='resale_price', index='year', aggfunc='mean')
# Plot line chart of yearly average resale price
yearly_avg.plot(kind='line', title='Yearly Average Resale Price')
# Set plot labels
plt.xlabel('Year')
plt.ylabel('Average Resale Price (SGD)')
# Add grid
plt.grid(True)
# Display the plot
plt.show()

# Rolling mean for smoothing
# Calculate 12-month rolling average of resale_price
df['resale_price_rolling'] = df['resale_price'].rolling(window=12).mean()
# Plot resale_price and rolling mean over time
df[['month', 'resale_price', 'resale_price_rolling']].plot(x='month', title='Resale Price with 12-Month Rolling Mean')
# Set plot labels
plt.xlabel('Month')
plt.ylabel('Resale Price (SGD)')
# Add grid
plt.grid(True)
# Display the plot
plt.show()

# Hypothesis Testing
# Select two towns for comparison
town1, town2 = 'ANG MO KIO', 'BEDOK'
# Extract resale_price for each town, dropping NaN values
prices_town1 = df[df['town'] == town1]['resale_price'].dropna()
prices_town2 = df[df['town'] == town2]['resale_price'].dropna()
# Perform independent t-test to compare means
t_stat, p_value = stats.ttest_ind(prices_town1, prices_town2)
# Print t-test results
print("T-test between {} and {}: t-stat={:.2f}, p-value={:.4f}".format(town1, town2, t_stat, p_value))

# Variance ratio test
# Calculate variance of resale_price for each town
var_town1 = prices_town1.var()
var_town2 = prices_town2.var()
# Compute F-statistic for variance comparison
F = var_town1 / var_town2
# Calculate p-value for F-test
p_value_var = 1 - stats.f.cdf(F, len(prices_town1)-1, len(prices_town2)-1)
# Print F-test results
print("F-test for variance between {} and {}: F={:.2f}, p-value={:.4f}".format(town1, town2, F, p_value_var))

# Confidence Intervals
# Define function to compute confidence interval
def confinterval(x, conf=0.95):
    # Calculate mean of the input data
    mean = np.mean(x)
    # Calculate standard error of the mean
    sem = stats.sem(x)
    # Compute confidence interval using t-distribution
    interval = stats.t.interval(conf, len(x)-1, loc=mean, scale=sem)
    return interval

# Compute 95% confidence interval for mean resale_price
ci = confinterval(df['resale_price'].dropna())
# Print confidence interval
print("95% CI for Mean Resale Price: {:.2f} to {:.2f} SGD".format(ci[0], ci[1]))

# Outlier Detection
# Calculate standard deviation of resale_price
sd = df['resale_price'].std()
# Identify outliers using 3 standard deviation threshold
outliers = df[(df['resale_price'] < (mean_price - 3*sd)) | (df['resale_price'] > (mean_price + 3*sd))]
# Print number of outliers
print("Number of outliers: {}".format(len(outliers)))
# Plot outliers in red and normal data points with transparency
plt.scatter(outliers['month'], outliers['resale_price'], color='red', label='Outliers')
plt.scatter(df['month'], df['resale_price'], alpha=0.1, label='Normal')
# Set plot title and labels
plt.title('Resale Price Outliers')
plt.xlabel('Month')
plt.ylabel('Resale Price (SGD)')
# Add legend
plt.legend()
# Add grid
plt.grid(True)
# Display the plot
plt.show()

# Regression Analysis
# Drop rows with NaN in resale_price or floor_area_sqm for clean dataset
df_clean = df.dropna(subset=['resale_price', 'floor_area_sqm'])
# Define predictor (floor_area_sqm) and response (resale_price) variables
X = df_clean[['floor_area_sqm']]
y = df_clean['resale_price']
# Fit linear regression model
model = LinearRegression().fit(X, y)
# Print regression parameters
print("Intercept: {:.2f}, Slope: {:.2f}".format(model.intercept_, model.coef_[0]))
# Calculate R-squared as percentage
r_squared = model.score(X, y) * 100
# Print R-squared
print("R-squared: {:.2f}%".format(r_squared))
# Initialize figure for regression plot
plt.scatter(X, y, alpha=0.5)
# Plot regression line
plt.plot(X, model.predict(X), color='red')
# Set plot title and labels
plt.title('Resale Price vs Floor Area with Regression Line')
plt.xlabel('Floor Area (sqm)')
plt.ylabel('Resale Price (SGD)')
# Add grid
plt.grid(True)
# Display the plot
plt.show()

# Regression plot with Seaborn
# Create scatter plot with regression line
sns.lmplot(data=df, x='floor_area_sqm', y='resale_price', line_kws={'color': 'red'})
# Set plot title and labels
plt.title('Resale Price vs Floor Area with Regression Line')
plt.xlabel('Floor Area (sqm)')
plt.ylabel('Resale Price (SGD)')
# Add grid
plt.grid(True)
# Display the plot
plt.show()

# Box plot by flat type
# Create box plot of resale_price by flat_type
sns.boxplot(data=df, x='flat_type', y='resale_price')
# Set plot title and labels
plt.title('Resale Price Distribution by Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Resale Price (SGD)')
# Rotate x-axis labels
plt.xticks(rotation=45)
# Add y-axis grid
plt.grid(True)
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Heatmap of average prices
# Create pivot table for average resale_price by town and flat_type
pivot_table = df.pivot_table(values='resale_price', index='town', columns='flat_type', aggfunc='mean')
# Plot heatmap with annotations for mean values
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f')
# Set plot title and labels
plt.title('Average Resale Price by Town and Flat Type')
plt.xlabel('Flat Type')
plt.ylabel('Town')
# Adjust layout
plt.tight_layout()
# Display the plot
plt.show()

# Regression with log-transformed resale_price
df_clean = df.dropna(subset=['resale_price', 'floor_area_sqm'])
df_clean['log_resale_price'] = np.log1p(df_clean['resale_price'])
X = df_clean[['floor_area_sqm']]
y = df_clean['log_resale_price']
model = LinearRegression().fit(X, y)
print("Log Regression Intercept: " + str(round(model.intercept_, 2)) + ", Slope: " + str(round(model.coef_[0], 2)))
r_squared = model.score(X, y) * 100
print("Log Regression R-squared: " + str(round(r_squared, 2)) + "%")
plt.scatter(X, y, alpha=0.5)
plt.plot(X, model.predict(X), color='red')
plt.title('Log Resale Price vs Floor Area with Regression Line')
plt.xlabel('Floor Area (sqm)')
plt.ylabel('Log Resale Price (SGD)')
plt.grid(True)
# Display the plot
plt.show()
plt.close()