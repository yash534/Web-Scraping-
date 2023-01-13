#!/usr/bin/env python
# coding: utf-8

# # Saving Data to CSV and Excel

# In[16]:


import bs4
import urllib.request
from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup


# In[18]:



html = urlopen('https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets')
bsobj = soup(html.read())
tbody = bsobj('table',{'class':'wikitable plainrowheaders sortable'})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
    cols = tuple(element.text.strip().replace('%','') for element in cols)
    xl.append(cols)
xl = xl[1:-1]
xl
 


# ### Connecting to MySQL Database

# In[ ]:





# In[19]:


import pymysql

# Open database connection
import configparser
config = configparser.RawConfigParser()
config.read(filenames = 'my.properties')
print(config.sections())


# In[20]:


h = config.get('mysql','host')
u = config.get('mysql','user')
p = config.get('mysql','password')
db = config.get('mysql','db')


# In[24]:


# Open database connection

scrap_db = pymysql.connect(h,u,p,db)


# In[25]:




# prepare a cursor object using cursor() method
cursor = scrap_db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS WIKI2 ")

# Create table as per requirement
sql = """CREATE TABLE WIKI2 (
   RANKING  INT,
   MARKET  CHAR(50),
   RETAIL_VALUE  CHAR(20),  
   PHYSICAL  INT,
   DIGITAL  INT,
   PERFORMANCE_RIGHTS  INT,
   SYNCHRONIZATION  INT
   )"""

cursor.execute(sql)

# disconnect from server
scrap_db.close()


# In[26]:


scrap_db = pymysql.connect(h,u,p,db)
mySql_insert_query = """INSERT INTO WIKI2 (RANKING, MARKET, RETAIL_VALUE, PHYSICAL,DIGITAL,PERFORMANCE_RIGHTS,SYNCHRONIZATION) 
                                VALUES (%s, %s, %s, %s ,%s, %s, %s) """

records_to_insert = xl

cursor = scrap_db.cursor()
cursor.executemany(mySql_insert_query, records_to_insert)
scrap_db.commit()
print(cursor.rowcount, "Record inserted successfully into WIKI2 table")
scrap_db.close()

