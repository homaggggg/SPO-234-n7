#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Public\la_crime_200_recs.csv', sep=',')


# In[5]:


df.sample(5)


# In[7]:


df.columns


# In[17]:


for i in df.columns:
    print(i, ": ", len(df[i].unique()))


# In[27]:


import matplotlib.pyplot as plt
pvt = df.pivot_table(index=['dr_number'], columns=['victim_sex'], values='Name', aggfunc='count')


data.plot.bar()
plt.xlabel('пол жертвы')
plt.ylabel('количество жертв')

plt.show()


# In[28]:


df["victim_sex"].value_counts()


# In[35]:


df.hist('victim_age')


# In[55]:


a = []
for i in df['crime_code'].unique():
    a.append(len(df[df['crime_code']==i]))
Ndf = pd.DataFrame({'crime_code': df['crime_code'].unique(), 'count': a})
Ndf['count'].hist()
Ndf.sort_values(by=['count'])
Ndf.head(5)


# In[54]:


df['crime_code'].unique()


# In[58]:


pvt = df.pivot_table(index=['dr_number'], columns=['victim_descent'], values='Name', aggfunc='count')


# In[ ]:




