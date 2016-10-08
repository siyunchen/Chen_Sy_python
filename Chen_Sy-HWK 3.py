# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:18:45 2016

@author: SiyunChen
"""
# Group E Homework 3

'''
Q1 Search for the IRIS dataset on the internet. You should quickly find the 
   UCI Machine Learning repository. Download the data and the data 
   description to your Python working directory. Use a text editor to add 
   the names of the columns to the data.
'''

'''
Q2 Search for help on the Python Pandas package. This is a very handy 
   package to manipulate and explore data in Python. It creates the 
   equivalent of an R dataframe (which you will learn about soon).
'''
import pandas as pd #import pandas to use functions from pandas using pd ro represent pandas in the following functions
pd.read_table('/Users/SiyunChen/Desktop/Chen_Sy_python/iris.data.txt',
              header = 0, sep = ',') 
              #read the data from local file, the header is the text that the names we add to the columns, and each column is seperated 
              #by ',', so we use header = 0 and sep = ','. then each column has a name that we have added. there are total 
              #150 rows and 5 columns.

'''
Q3 Using a Pandas method, read the file into a data structure, including the 
   column names. (If you have completed step one correctly, this should be 
   automatic).
'''
data = pd.read_table('/Users/SiyunChen/Desktop/Chen_Sy_python/iris.data.txt',
       header = 0, sep = ',')
       #using a Pandas method read the local data file into a data structure 
       #the header is the text that the names we add to the columns. 
       #and each column is seperated by ','.

'''
Q4 Using Pandas, display the first ten and the last ten rows of the data.
'''
data.head(10) #using data.head(10) to display the first ten rows of data

data.tail(10) #using data.tail(10) to display the last ten rows of data

'''
Q5 Using Pandas, print simple location statistics (Count, Mean, STD, Min, 
   25%, 50%, 75%, MAX).
   There is a single method call that will accomplish this.
'''
data.describe().transpose()
#this single function can give the simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX) of numeric variables

'''
Q6 Using Pandas, plot a histogram for each of the numeric columns and a 
   bar chart for the nominal column.
'''
data.hist() #using data.hist() to plot a a histogram for each of the numeric columns: sepal length in cm, sepal width in cm,
            #petal length in cm, petal width in cm

data.class0.value_counts().plot(kind='bar')
#plot a bar chart for the nomial column: class
#there are three kinds in class: Iris-setosa, Iris-versicolor and Iris-virginica 


