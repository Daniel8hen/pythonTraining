import pandas as pd

#read CSV file // print not really needed, just to see output
# pandas can read from JSON, xml, html, and many more - user help for reference.
df = pd.read_csv('example.csv')
# write to csv
# df.to_csv('MY_Output', index=False) #index = False to remove irrelevant index
# print(pd.read_csv('MY_Output'))
# print(pd.read_excel('Excel_sample.xlsx', sheet_name='Sheet1'))
# pass file name, pass sheet name - that's all about reading from excel file
# writing to excel
# df.to_excel('Excel_sample2.xlsx',sheet_name='NewSheet')
# HTML
# read HTML
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
#print(df[0].head())

# SQL
# pandas is not the best approach to read data from
from sqlalchemy import create_engine #import relevant method
engine = create_engine('sqlite:///:memory:') #create in-memory engine
df.to_sql('my_table',engine) #create a table called "my_table" using the sql engine we've created
sqldf = pd.read_sql('my_table', con=engine) #read data from that "my_table" table
print(sqldf) #print data. Note: "index" is a new column
