#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data_all = pd.read_csv("https://osf.io/download/4ay9x/")

data_all.columns

data_all[data_all['occ2012']==205].count()


# 

# 

# In[ ]:


top_occ = data_all['occ2012'].value_counts().head(2)
print(top_occ)


