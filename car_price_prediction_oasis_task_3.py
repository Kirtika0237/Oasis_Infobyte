# -*- coding: utf-8 -*-
"""Oasis_task_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UUHf9U2hCL6Z1blpk34hkOUr1rgz4Ib-

Task 3 :CAR PRICE PREDICTION WITH MACHINE LEARNING

The price of a car depends on a lot of factors like the goodwill of the brand of the car,
features of the car, horsepower and the mileage it gives and many more. Car price
prediction is one of the major research areas in machine learning. So if you want to learn
how to train a car price prediction model then this project is for you
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/car data.csv')
data

data.head(5)

data.describe()

data.shape

data.info()

data.isnull().sum()

"""Visualize the distribution of the target variable"""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(data['Selling_Price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Selling Price', fontsize=16)
plt.xlabel('Selling Price', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

sns.set_palette("deep")
sns.pairplot(data, vars=['Year', 'Present_Price', 'Driven_kms', 'Selling_Price'])
plt.show()

sns.pairplot(data,hue='Year',palette='twilight')

numeric_data = data.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='twilight_shifted', fmt='.2f', linewidths=0.5)
plt.title('Correlation matrix')
plt.show()

palette = "twilight"
plt.figure(figsize=(10, 5))
sns.boxplot(x='Fuel_Type', y='Selling_Price', data=data, palette=palette)
plt.title('Selling price vs Fuel Type')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x='Selling_type',data=data,palette='twilight')
plt.title('Seller Type')
plt.show()

sns.pairplot(data,hue='Fuel_Type',palette='cubehelix')

plt.figure(figsize=(10,5))
sns.violinplot(x='Selling_type',y='Selling_Price',hue='Transmission',data=data,palette='twilight')
plt.title('Selling Price vs Seller Type and Transmission')
plt.show()

# Perform one-hot encoding on the categorical columns
x = pd.get_dummies(data.drop(['Car_Name', 'Selling_Price'], axis=1))

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Define and train your model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict on the test set
y_pred = model.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

plt.scatter(y_test,y_pred)
plt.plot(y_test,y_test,color='red')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()
