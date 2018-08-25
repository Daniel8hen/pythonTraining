# ## Imports
import pandas as pd
import numpy as np
#visualization libs
import matplotlib.pyplot as plt
import seaborn as sns
#for having the ability to see the visualizations in the notebook
get_ipython().magic(u'matplotlib inline')


# ## Get the Data
customers = pd.read_csv("Ecommerce Customers")
# recommended actions on data
customers.head()
customers.describe()
customers.info()


# ## Exploratory Data Analysis
sns.jointplot(data=customers, x="Time on Website", y="Yearly Amount Spent")
sns.jointplot(x=customers["Time on App"], y=customers["Yearly Amount Spent"],kind='scatter', height=6)
sns.jointplot(x=customers["Time on Website"], y=customers["Length of Membership"],kind='hex', height=6)
sns.pairplot(customers)

sns.lmplot(x="Yearly Amount Spent",y="Length of Membership",data=customers)


# ## Training and Testing Data

X = customers[["Avg. Session Length", "Time on App",
       "Time on Website", "Length of Membership"]]
y = customers["Yearly Amount Spent"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# ## Training the Model
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)
# printing coefficients
print(lm.coef_)


# ## Predicting Test Data
predictions = lm.predict(X_test)
sns.scatterplot(predictions, y_test)


# ## Evaluating the Model
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('Explained Variance Score', metrics.explained_variance_score(y_test, predictions))
# np.sqrt since it's root on the MSE

# ## Residuals
sns.distplot(y_test - predictions,bins=50)


# ## Conclusion
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficients'])
print(coeff_df)

# **Do you think the company should focus more on their mobile app or on their website?**
# app if it's only about "what is working better"
# website if it's to enhance if it's only in enhancing existing products
