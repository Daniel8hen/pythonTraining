
# coding: utf-8

# In[96]:


import requests
from bs4 import BeautifulSoup

# requests.get (URL) + requests.content - keep HTML of page.
r = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

# beautify HTML
soup = BeautifulSoup(c, "html.parser")

# logic - grab HTML, go through HTML's and find relevant tags for data we want to get.
# we should find the elements which identifies 
all = soup.find_all("div",{"class":"propertyRow"})
# each element of the "all" have same methods of soup.find_all ...
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","")
# get page number dynamically
num_of_pages = soup.find_all("a", {"class":"Page"})[-1].text
print(num_of_pages)


# In[98]:


#now we'd like to extract the data by iterating
l = []
#base_url="https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(num_of_pages)*10,10):
    r = requests.get(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d = {}
        d["Address"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"] = None
        d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","")
        try:
            d["Beds"] = item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            d["Area"] = item.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Full baths"] = None

        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),
                                                  column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)


# In[99]:


import pandas
df = pandas.DataFrame(l)


# In[85]:


df


# In[100]:


df.to_csv("WebScrapperOutput.csv")

