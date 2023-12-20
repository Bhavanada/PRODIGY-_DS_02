#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 02
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset

titanic_data = pd.read_csv("C:\\Users\\compaq\\Desktop\\gender_submission.csv")

# Display the first few rows of the dataset to understand its structure
print(titanic_data.head())

# Check for missing values
print(titanic_data.isnull().sum())





# Correlation heatmap for numeric variables
numeric_cols = titanic_data[['Survived','PassengerId']]
correlation_matrix = numeric_cols.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




