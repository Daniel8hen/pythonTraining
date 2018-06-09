import numpy as np
import pandas as pd
from numpy.random import randn
#series
# very similar to numpy array, but the difference - series can have axis lables

# labels = ['a','b','c'] #list
# my_data = [10,20,30] #np list
# arr = np.array(my_data) #np array
# d = {'a':10, 'b':20, 'c':30}

# print(pd.Series(data=my_data,index=labels)) #gets few params, data + index are the most important
# now I have a Series with labels
# the method can be also: pd.Series(my_data,labels)
# print(pd.Series(arr,labels)) # for arr

# print(pd.Series(d))
# print(pd.Series(labels))

# print(pd.Series(data=[sum,print,len])) - relevant for functions as well, holds references to those functions
# not working in the IDE

# ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','JAPAN'])
# print(ser1)

# ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','JAPAN'])
# print(ser2)

#get value of Series - index is usually a number or a string
# print(ser1['USA'])

# operations:
# when performing arithmetic on series, the int are becoming float.. ( keep in mind)
# print(ser1 + ser2)

# *** DataFrames ***
# np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# rand(5,4) for data, 'A' to 'E' for index, 'W' to 'Z' for columns
# print(df) - all df
# df - bunch of series that share the same index
# print(df['W']) #this is a series - get column by name
# another way (less recommended since it's not a method)
# print(df.W)
# multiple columns - df is returned by calling df with a list:
# print(df[['W','Z']])
# creating/adding new column - can be defined as already exists
df['new'] = df['W'] + df['Y']
# print(df)
# removing column by name using df.drop method - axis = 1 is a referer to the column (rather than indexes)
# the inplace = True is for deleting the actual dataframe (and not only on the drop)
df.drop('new', axis=1,inplace=True)
# print(df)
# print(df.drop('E')) #without inplace
# print(df.shape) # returnes 5,4 - index 0 = rows, index 1 = columns
# selecting rows
# print(df.loc['A']) # rows are series as well
# print(df.iloc[2]) #rows by index
# subset of rows, columns
# print(df.loc['B','Y'])
# print(df.loc[['A','B'],['W','Y']])
