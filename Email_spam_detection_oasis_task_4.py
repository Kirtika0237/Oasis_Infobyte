# -*- coding: utf-8 -*-
"""Oasis_task_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D2t3rvnRM24GDMBWMeEMPC82KEgoOZ7b

Task- 4 EMAIL SPAM DETECTION WITH MACHINE LEARNING

We’ve all been the recipient of spam emails before. Spam mail, or junk mail, is a type of email
that is sent to a massive number of users at one time, frequently containing cryptic
messages, scams, or most dangerously, phishing content.



In this Project, use Python to build an email spam detector. Then, use machine learning to
train the spam detector to recognize and classify emails into spam and non-spam.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/spam.csv', encoding='latin-1')
data

data.describe()

data.shape

#data cleaning
data.info()

data.head(5)

data.isnull().sum()

print(data.columns)

data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],axis=1,inplace=True)
data

data.rename(columns={'v1':'target','v2':'text'},inplace=True)
data

data.duplicated().sum()

data.drop_duplicates(keep='first',inplace=True)
data.shape

data

print(data.columns)

sns.countplot(x='target', data=data, palette=['blue', 'red'])
plt.title('Count of spams and hams')
plt.xlabel('Spam or Ham')
plt.ylabel('count')
plt.show()

plt.pie(data['target'].value_counts(),labels=['ham','spam'],autopct="%0.2f")
plt.show()

data['text_length'] = data['text'].apply(len)

# Plotting histogram
plt.figure(figsize=(10, 5))
sns.histplot(data=data, x='text_length', hue='target', kde=True, bins=20)
plt.title('Histogram of Text Length for Spam and Ham')
plt.xlabel('Text Length')
plt.ylabel('Frequency')
plt.legend(title='Target')
plt.show()

sns.pairplot(data,hue='target')
plt.show()

data['target_encoded'] = data['target'].map({'ham': 0, 'spam': 1})

# Drop non-numeric columns
numeric_data = data.drop(columns=['target', 'text'])

# Create a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='crest')
plt.title('Correlation Heatmap')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X = data['text']
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Define and train  model
model = LogisticRegression()
model.fit(X_train_counts, y_train)

# Predict on the test set
y_pred = model.predict(X_test_counts)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

# Print the evaluation metric
print("Accuracy:", accuracy)
