#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


data = pd.read_csv('movie_metadata.csv')


# In[16]:


data.columns


# In[ ]:


# keeping the columns that are useful in recommndation system
data = data.loc[:,['actor_1_name','actor_2_name','actor_3_name','director_name','genres','movie_title']]


# In[18]:


data.head()


# In[19]:


# dealing with null values
data.isnull().sum(axis=0)


# In[ ]:


# replacing null values in the all columns with string 'unknown'
data['actor_1_name'] = data['actor_1_name'].replace(np.nan, 'unknown')
data['actor_2_name'] = data['actor_2_name'].replace(np.nan, 'unknown')
data['actor_3_name'] = data['actor_3_name'].replace(np.nan, 'unknown')
data['director_name'] = data['director_name'].replace(np.nan, 'unknown')


# In[ ]:


# In the ‘genres’ column, replacing the ‘|’ with whitespace,
# so the genres would be considered different strings.
data['genres'] = data['genres'].replace('|', ' ')


# In[ ]:


# Now converting the ‘movie_title’ columns values to lowercase for searching simplicity.
data['movie_title'] = data['movie_title'].str.lower()


# In[24]:


# all the movie_title values have a special character added to the end
# which needs to be removed
data['movie_title'][0]


# In[ ]:


data['movie_title'] = data['movie_title'].str[:-1]


# In[ ]:


data.to_csv('data.csv',index=False)


# In[ ]:




