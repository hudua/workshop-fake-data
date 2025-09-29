#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset_social_programs = ml_client.data.get("social_programs", version="1")
data_asset_applications = ml_client.data.get("applications", version="1")


df_social_programs = pd.read_parquet(data_asset_social_programs.path)
df_applications = pd.read_parquet(data_asset_applications.path)


# In[2]:


df_applications.head(5)


# In[3]:


merged_df = pd.merge(df_social_programs, df_applications, on='ProgramID')

# Aggregate by ProgramID and sum the applicationcost column
aggregated_df = merged_df.groupby('ProgramID')['ApplicationCost'].sum().reset_index()


# In[4]:


aggregated_df.head(5)


# In[5]:


aggregated_df.to_csv('program_costs.csv', index = False)

from azureml.fsspec import AzureMachineLearningFileSystem
# instantiate file system using following URI
fs = AzureMachineLearningFileSystem('azureml://subscriptions/<sub-id>/resourcegroups/<customer>-workshop/workspaces/amlhuduaworkshop/datastores/experimentation/paths/')

# you can specify recursive as False to upload a file
fs.upload(lpath='program_costs.csv', rpath='data/fsspec', recursive=False, **{'overwrite': 'MERGE_WITH_OVERWRITE'})


# In[6]:


aggregated_df


# In[7]:


import xport
import xport.v56
 
#....
 
ds = xport.Dataset(aggregated_df, name='DATA', label='Wonderful data')
 
ds = ds.rename(columns={k: k.upper()[:8] for k in ds})
 
for k, v in ds.items():
    v.label = k.title()
    if v.dtype == 'object':
        v.format = '$CHAR20.'
    else:
        v.format = '10.2'
 
library = xport.Library({'DATA': ds})
 
with open('output.xpt', 'wb') as f:
    xport.v56.dump(library, f)


# In[8]:


import xport.v56
 
with open('output.xpt', 'rb') as f:
    library = xport.v56.load(f)


# In[11]:


library['DATA']


# In[ ]:




