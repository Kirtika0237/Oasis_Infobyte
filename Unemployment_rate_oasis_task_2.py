# -*- coding: utf-8 -*-
"""Oasis_task_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yGmiDq03lQxPhm6mApDPzF7OxWPyvvhk

## Oasis Infobyte

Task 2: Unemployment is measured by the unemployment rate which is the number of people
who are unemployed as a percentage of the total labour force. We have seen a sharp
increase in the unemployment rate during Covid-19, so analyzing the unemployment rate
can be a good data science project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/Unemployment in India.csv')
data=pd.read_csv('/content/Unemployment_Rate_upto_11_2020.csv')
data

data.head()

data.info()

data.describe()

data.isnull().sum()

plt.figure(figsize=(12, 6))
plt.bar(data['Region'], data[' Estimated Unemployment Rate (%)'], color='skyblue')

# Label the axes and title
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Estimated Unemployment Rate By Region')

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Filter out non-numeric columns
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdBu')

sns.pairplot(data,hue='Region.1',palette='brg')

"""# Distribution of Estimated Employed by Region"""

plt.figure(figsize=(12, 8))
sns.histplot(x=' Estimated Employed', hue='Region', data=data, multiple="stack", palette="inferno")
plt.title('Distribution of Estimated Employed by Region')
plt.xlabel('Estimated Employed')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
sns.histplot(x=' Estimated Employed', hue='Region', data=data)

# Add title
plt.title('Indian Unemployment')

# Show plot
plt.show()

sns.set_theme(style="whitegrid")

# Create the box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Region', y=' Estimated Unemployment Rate (%)', data=data, palette='bright')

# Add labels and title
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Box Plot of Estimated Unemployment Rate by Region')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.show()

unemployment = data[["Region", " Estimated Employed"]]
figure = px.sunburst(unemployment, path=["Region"],
                     values=" Estimated Employed", # Use the correct column name with the leading space
                     width=700, height=700, color_continuous_scale="Viridis",
                     title="Unemployment Rate in India")
figure.show()

plt.figure(figsize=(10, 6))

# Scatter plot with a color palette
sns.scatterplot(data=data, x=' Estimated Unemployment Rate (%)', y=' Estimated Employed', hue=' Estimated Unemployment Rate (%)', palette='Dark2', alpha=0.7, legend=None)

# Adding labels and title
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Estimated Employed')
plt.title('Scatter Plot of Estimated Unemployment Rate vs. Estimated Employed')
plt.grid(True)

# Show plot
plt.show()
