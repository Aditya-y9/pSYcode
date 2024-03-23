#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data = pd.read_excel("Instagramdata.xlsx")
data = data.dropna()
print(data.head())


# In[6]:


figure = px.scatter(data_frame = data, 
                    x="Impressions",
                    y="Likes", 
                    size="Likes", 
                    trendline="ols", 
                    title = "Relationship Between Likes and Impressions")
figure.show()


# In[7]:


plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()


# In[ ]:




