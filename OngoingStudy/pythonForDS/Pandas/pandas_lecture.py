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
# df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# rand(5,4) for data, 'A' to 'E' for index, 'W' to 'Z' for columns
# print(df) - all df
# df - bunch of series that share the same index
# print(df['W']) #this is a series - get column by name
# another way (less recommended since it's not a method)
# print(df.W)
# multiple columns - df is returned by calling df with a list:
# print(df[['W','Z']])
# creating/adding new column - can be defined as already exists
# df['new'] = df['W'] + df['Y']
# print(df)
# removing column by name using df.drop method - axis = 1 is a referer to the column (rather than indexes)
# the inplace = True is for deleting the actual dataframe (and not only on the drop)
# df.drop('new', axis=1,inplace=True)
# print(df)
# print(df.drop('E')) #without inplace
# print(df.shape) # returnes 5,4 - index 0 = rows, index 1 = columns
# selecting rows
# print(df.loc['A']) # rows are series as well
# print(df.iloc[2]) #rows by index
# subset of rows, columns
# print(df.loc['B','Y'])
# print(df.loc[['A','B'],['W','Y']])

# conditional selection
# print(df > 0)
# booldf = df > 0
# print(df[booldf])
# print(df)
# print(df['W'] > 0)
# print(df[df['W'] > 0])
# print(df[df['W'] > 0]['X'])
# multiple conditions
# df[(df['W'] > 0) and (df['Y'] > 1)] # returns error - can't handle seris of bool and another series of bools
# and can only deal with single bool values
# print(df[(df['W'] > 0) & (df['Y'] > 1)]) - works well! for "or" - use | (1 pipe)
# convention - (condition) & or | (condition)

# print(df.reset_index()) #reset the index to another column, not inplace by default
# print(df.set_index('X')) #set a specific column to be the index!
# print(df)

#index levels
# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside,inside)) #list of tuples G1,1, G1,2, ...
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# now we see that we have multi level "hierarchy" index
# df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
# print(df)

# print(df.loc['G1'].loc[1])
# give high index names
# df.index.names = ['Groups', 'Num']
# print(df)
# print(df.loc['G2'].loc[2]['B'])
# another option of multi level index - for specific data - cross section of rows and columns
# print(df.xs(1,level='Num')) # where level = Num is 1

# *** Missing data ***
# d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
# df = pd.DataFrame(d)
# print(df)
# Drop missing values
# print(df.dropna()) # use axis = 1 for columns with no values
# another argument is thresh
# print(df.dropna(thresh=2))
# fill missing values
# print(df.fillna(value='FILL VALUE'))
# fill values with mean - though there's a great philosophy of how to fill empty values
# print(df['A'].fillna(value=df['A'].mean()))

# **** GroupBy ****
#
# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#         'Person':['Sam', 'Charlie','Amy','Vanessa', 'Carl', 'Sarah'],
#         'Sales':[200,120,340,124,243,350]}
#
# df = pd.DataFrame(data)
# byComp = df.groupby('Company')
# print(byComp.mean().loc['FB']) #ignore non numeric values - std(), mean(), sum() works as well
# # one line - df.groupby('Company').count()
# print(df.groupby('Company').describe().transpose())


# *** Merging, joining and concatenating DFs ***
# once we have separate DF's, we can use -
# pd.concat([df1,df2,df3]) - pd.concat gets a list of DFs - we can use axis = 1 as a flag in the concat as well
# and then we'll have NaNs since not all rows, columns had values (columnar concat)

# merge - like merging in SQL (join) - merging two dataframes on specific key
#pd.merge(left, right, how='inner', on='key') - like SQL inner join
# we can use "on" on list of keys (not only 1 key), outer/right/left joins on "how"


# joining - same as merge except the "keys" is the actual indexes

# df1.join(df2) / df1.join(df2, how ='outer')

# *** operations ***
# find unique values - df['someCol'].unique() // nunique() - number of unique values
# counts of unique values in a column - df['col'].value_counts()
# apply method
# def times(x):
#     return x*2
# apply is a powerful method for df['someCol'], and for lambda expressions
# df['col'].apply(lambda x: x*2) - applies a custom expression on columns

# df.drop('someCol', axis = 1, inplace=True) // for column
# df.sort_values(by='col2') // df.sort_values('col2') - same same - will present df sorted by relevant col.
# df.isnull() - returns DF for if the value is null or not
# df.pivot_table(values='someCol', index=['A','B'], columns = ['C'])
