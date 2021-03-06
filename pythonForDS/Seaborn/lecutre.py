# Distribution Plots
import seaborn as sns
import matplotlib.pyplot as plt # because not using jupyter notebook
import numpy as np
# if using jupyter notebook use %matplotlib inline for visualization inline
tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.head()) #people who had a meal and left tip in the end
# sns.distplot(tips['total_bill'],kde=False,bins=40) #removing the line above the distributor graph
# sns.jointplot(x='total_bill',y='tip',data=tips)
# kind = hex, hexagon plot shows distribution by "color"
# kind = reg, regression plot on that distribution
# kind = kde, density of where the points matches the most
# sns.pairplot(tips, hue='sex', palette='coolwarm') #quickly visualize data, hue for a specific column
# palette - some color to visualize
# sns.rugplot(tips['total_bill']) #dash mark on uni variable
# what is the KDE?
# Kernal Density Estimation plots - basically it's sum of few normal distributions around a rugplot
# sns.kdeplot(tips['total_bill'])

# Categorial Plots
# sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std) #estimator for aggregation function on the data
# sns.countplot(x='sex',data=tips) #count mechanism on the categorial data
# sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
# sns.violinplot(x='day',y='total_bill',data=tips, hue='sex',split=True) #advanced one, not the best to present to biz
# sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',split=True)
# sns.swarmplot(x='day',y='total_bill',data=tips) # not always scaling in large datasets
# two plots one in another
# sns.violinplot(x='day',y='total_bill',data=tips)
# sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
# sns.factorplot(x='day',y='total_bill',data=tips,kind='bar') - available for specific graphs usage
# matrix plots
# flights=sns.load_dataset('flights')
# print(flights.head())

# tc = tips.corr()
# print(tips.corr())
# sns.heatmap(tc, annot=True, cmap='coolwarm') #can use annot for annotation, cmap for colormap

#another matrix manipulation
# fp = flights.pivot_table(index='month',columns='year',values='passengers')
# sns.heatmap(fp,cmap='coolwarm',linecolor='black',linewidths=1) #and tons of options to customize
# sns.clustermap(fp,cmap='coolwarm',standard_scale=1) #clustering on the data
# iris = sns.load_dataset('iris')
# print(iris.head())
# print(iris['species'].unique())
#Grids
# g = sns.FacetGrid(data=tips,col='time',row='smoker') # facet grid for the tips dataset
# g = sns.PairGrid(iris) # makes all values and gives you control for subplots
# btw, pairplot is a simplified version of pairgrid
# g.map(plt.scatter)
# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)
# g.map(sns.distplot,'total_bill')
# g.map(plt.scatter,'total_bill','tip')

#Regression Plots - lmplot for linear regression plotting
#sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],
# scatter_kws={'s':100}) #x axis vs y axis
# sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex', aspect=0.6,size=8) #can add row as well
# style and color session
sns.set_style('whitegrid') #background style
# sns.countplot(x='sex',data=tips)
#remove spines by
# sns.despine() #can be used only on top, left, bottom, right as well
# plt.figure(figsize=(12,3))
# sns.set_context('poster',font_scale=5)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='seismic')
plt.show()
