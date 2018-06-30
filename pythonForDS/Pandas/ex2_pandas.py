
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[5]:


ecom = pd.read_csv("Ecommerce Purchases")


# **Check the head of the DataFrame.**

# In[46]:


ecom.head(10)


# ** How many rows and columns are there? **

# In[12]:


ecom.shape #10000 rows, 14 columns


# ** What is the average Purchase Price? **

# In[14]:


ecom["Purchase Price"].mean()
#50.347


# ** What were the highest and lowest purchase prices? **

# In[15]:


ecom["Purchase Price"].max()


# In[16]:


ecom["Purchase Price"].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[18]:


ecom[ecom["Language"] == "en"].count()
#1098


# ** How many people have the job title of "Lawyer" ? **
# 

# In[22]:


ecom[ecom["Job"] == "Lawyer"].count()
#30


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[27]:


ecom["AM or PM"].value_counts()
#PM - 5068
#AM - 4932
#value counts can differ between values and count per each value


# ** What are the 5 most common Job Titles? **

# In[28]:


ecom["Job"].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[36]:


ecom[ecom["Lot"] == "90 WT"]["Purchase Price"]
#75.1


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[43]:


ecom[ecom["Credit Card"] == 4926535242672853]["Email"]
#bondellen@williams-garza.com


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[51]:


ecom[(ecom["CC Provider"] == "American Express") & (ecom["Purchase Price"] > 95)].count()
# just make sure to use brackets on *each* condition


# ** Hard: How many people have a credit card that expires in 2025? **

# In[80]:


ecom[ecom["CC Exp Date"].str.contains("/25")].count()
#1033


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[124]:


f = lambda x: x["Email"].split("@")[1]
ecom["domainFromEmail"] = ecom.apply(f, axis=1)

ecom["domainFromEmail"].value_counts().head(5)
# hotmail.com     1638
# yahoo.com       1616
# gmail.com       1605
# smith.com         42
# williams.com      37


# # Great Job!
