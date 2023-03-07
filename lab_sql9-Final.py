#!/usr/bin/env python
# coding: utf-8

# ## Create a Python connection with SQL database and retrieve the results of the last two queries (also mentioned below) as dataframes:
# 
# Check the number of rentals for each customer for May
# 
# Check the number of rentals for each customer for June
# 
# Hint: You can store the results from the two queries in two separate dataframes.

# In[1]:


import pandas as pd
import sqlalchemy as alch


# In[2]:


from getpass import getpass
password = getpass("Introduce your sql password: ")


# In[3]:


dbName = "sakila"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)


# In[12]:


rentals_may = pd.read_sql_query(
"""
SELECT * FROM rentals_may;
""", engine
)
rentals_may.head()


# In[54]:


len(rentals_may)


# In[34]:


customers_rentals_may = pd.read_sql_query(
"""
SELECT customer_id, COUNT(rental_id) AS num_rental_may FROM rentals_may GROUP BY customer_id;
""", engine
)
customers_rentals_may.head()


# In[35]:


rentals_june = pd.read_sql_query(
"""
SELECT * FROM rentals_june;
""", engine
)
rentals_june.head()


# In[55]:


len(rentals_june)


# In[36]:


customers_rentals_june = pd.read_sql_query(
"""
SELECT customer_id, COUNT(rental_id) AS num_rental_june FROM rentals_june GROUP BY customer_id;
""", engine
)
customers_rentals_june.head()


# ## Write a function that checks if customer borrowed more or less films in the month of June as compared to May.

# In[37]:


merge_rental = customers_rentals_may.merge(customers_rentals_june, on="customer_id", how="inner")
merge_rental.head()


# In[39]:


#comparing rentals in May with rentals in June

merge_rental['more_in_june'] = merge_rental['num_rental_may']<merge_rental['num_rental_june']
merge_rental.head()


# In[41]:


#Adding a column to show the difference of rentals in June and May

merge_rental['difference'] = merge_rental['num_rental_june']- merge_rental['num_rental_may']
merge_rental.head()


# In[52]:


#Adding a column to show if the number of rentals for each customer increased or decreased.

def more_in_june(x):
    if x is True:
        return 'Increase'
    else:
        return 'Decrease'

        
merge_rental['rental_increase_in_june'] = list(map(more_in_june, merge_rental['more_in_june']))


# In[56]:


merge_rental.sample(10)

