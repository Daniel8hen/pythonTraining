# Plotly - *interactive* visualization library
# Cufflinks - connect plotly with Pandas
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
import cufflinks as cf
from plotly import __version__
%matplotlib inline

init_notebook_mode(connected=True)
cf.go_offline()

#DATA
# DataFrame
df = pd.DataFrame(np.random.randn(100,4),columns = 'A B C D'.split())
# print(df.head())
# another DataFrame
df2 = pd.DataFrame({'Category':['A','B','C'], 'Values':[32,43,50]})
# print(df2)
# for specific kinds of visualizations, we can use -
# df.iplot(kind='scatter', x='A',y='B',mode='markers',size=20)
# df.sum().iplot(kind='bar') // kind = 'box' // df.count()
# 3D surface
# df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
# df3.iplot(kind='surface',colorscale='rdylbu') #rd red, yl yellow, bu blue
# histogram
# df['A'].iplot(kind='hist',bins=25)
# spread - relevant for time series data (like stocks...)
# df[['A','B']].iplot(kind='spread')
# bubble plot - like GDP, population etc.
# df.iplot(kind='bubble',x='A',y='B',size='C')
# make sure columns are numerical
# df.scatter_matrix()
# more info in cufflinks github
