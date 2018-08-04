#pandas allows you to visualize data directly from a dataframe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
#time series
df1 = pd.read_csv('df1',index_col=0)
# print(df1.head())
# non time series
df2 = pd.read_csv('df2',index_col=0)
# print(df2.head())
# print(df1['A'].hist(bins=30))
# df1['A'].plot.hist() - histograms are used the most
# df2.plot.area(alpha=0.4) #alpha is for transparent
# df2.plot.bar(stacked=True)
#line plot
# df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)
#scatter plot
# df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm') #c = color - 3D graph
# df1.plot.scatter(x='A',y='B',s=df1['C']*100)
# box plot (seaborn is likely to use more than pandas, but still)
# df2.plot.box()
df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
# print(df.head())
# df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')
# df['a'].plot.kde()
# df['a'].plot.density()
plt.show()
