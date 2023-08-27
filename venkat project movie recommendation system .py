#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt


# In[2]:


movie = pd.read_csv('movies_metadata.csv')


# In[3]:


movie.head()


# In[4]:


for i in movie.columns:
    print(i)


# In[5]:


movie.shape


# In[7]:


movie.describe()


# movie['original_language'].value_counts()

# In[8]:


movie['original_language'].value_counts()


# In[9]:


movie['original_language'].value_counts()[0:5]


# In[10]:


plt.figure(figsize=(5,5))
plt.bar(list(movie['original_language'].value_counts()[0:5].keys()),list(movie['original_language'].value_counts()[0:5]),color="r")
plt.show() 


# In[11]:


plt.figure(figsize=(5,5))
plt.hist(movie['vote_average'])
plt.show()


# In[12]:


high_rated_movies=movie[movie['vote_average']>8]


# In[13]:


high_rated_movies.head()


# In[14]:


high_rated_movies.shape


# In[17]:


top5_high=high_rated_movies.sort_values(by="vote_average",ascending=False).head()


# In[18]:


top5_high


# In[19]:


top5_revenue=movie.sort_values(by="revenue",ascending=False).head()


# In[20]:


top5_revenue


# In[21]:


movie['status'].value_counts()


# In[ ]:




