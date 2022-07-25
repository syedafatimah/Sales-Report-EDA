# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Syeda Fatima Zahid
#Graduate Rotational Internship Program Sparks Foundation-Data Science And Business Analytics

#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataset
data = pd.read_csv("SampleSuperstore.csv")
print(data)

data.info() #It shows that our dataset has no null value

print(data.shape)
print(data.describe()) #It shows statistical relation between data values

#Checking Missing Values
print(data.isnull().sum())

# Chaecking the dupilication in data
print(data.duplicated().sum())
data.drop_duplicates()

#Deleting the Variable.
col=['Postal Code']
sample1=data.drop(columns=col,axis=1) #We don't need postal code for our profit and loss determination

#View all the states
print(data['State'].unique())

#Correlation Between Variables.
print(sample1.corr())

#Covariance Between Variables.
print(sample1.cov())

#View all segments
print(data['Segment'].value_counts())

####### Data Visualization #########

plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=sample1)
plt.title('Category vs Sub Category')
plt.xlabel('Sub-Catgory')
plt.ylabel('Category')
plt.xticks(rotation=45)
plt.show()

#create a histogram
sample1.hist(bins=50 ,figsize=(20,15))
plt.show();
#histogram shows our data has outliers

#Find loss sales
loss_df=data[data['Profit'] < 0]
loss_df

print(loss_df.groupby(by='Segment').sum())
#It shows more discount leads to more loss

print(loss_df.groupby(by='Sub-Category').sum())
#It shows that binders sales has more loss