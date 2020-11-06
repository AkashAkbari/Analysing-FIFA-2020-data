#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[11]:


fifa=pd.read_csv('G:/GitHub_Projects/Analysing FIFA 2020 data/players_20.csv')


# In[7]:


fifa.head()


# In[12]:


for col in fifa.columns:
    print (col)


# In[13]:


fifa.shape


# In[14]:


fifa['nationality'].value_counts()


# In[15]:


fifa['nationality'].value_counts()[0:10]


# In[16]:


fifa['nationality'].value_counts()[0:5]


# In[17]:


plt.figure(figsize=(8, 5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()), list(fifa['nationality'].value_counts()[0:5]), color="g")
plt.show()


# In[18]:


player_salary=fifa[['short_name','wage_eur']]


# In[19]:


player_salary.head()


# In[20]:


plt.figure(figsize=(8, 5))
plt.bar(list(player_salary['short_name'])[0:5], list(player_salary['wage_eur'])[0:5], color="r")
plt.show()


# In[21]:


#Germany
Germany=fifa[fifa['nationality']=='Germany']
Germany.head()


# In[22]:


Germany.sort_values(by=['height_cm'], ascending=False).head()


# In[24]:


Germany.sort_values(by=['weight_kg'], ascending=False).head()


# In[25]:


Germany.sort_values(by=['wage_eur'], ascending=False).head()


# In[29]:


Germany[['short_name', 'wage_eur']].sort_values(by=['wage_eur'], ascending=False).head()


# In[31]:


#Shooting
player_shooting=fifa[['short_name', 'shooting']]


# In[32]:


player_shooting.sort_values(by=['shooting'], ascending=False).head()


# In[ ]:


#Defending


# In[34]:


player_defending=fifa[['short_name', 'defending']]


# In[37]:


player_defending.sort_values(by=['defending'],ascending=False).head()


# In[38]:


real_madrid=fifa[fifa['club']=='Real Madrid']


# In[39]:


real_madrid.sort_values(by=['wage_eur'], ascending=False).head()


# In[40]:


real_madrid.sort_values(by=['shooting'], ascending=False).head()


# In[41]:


real_madrid['nationality'].value_counts()

