#!/usr/bin/env python
# coding: utf-8

# ## Sparkanalysis
# 
# 
# 

# In[1]:


1+1


# In[3]:


get_ipython().run_cell_magic('pyspark', '', "df_appplications = spark.read.load('abfss://raw@esdcdatalakehudua.dfs.core.windows.net/applications.parquet', format='parquet')\ndf_programs = spark.read.load('abfss://raw@esdcdatalakehudua.dfs.core.windows.net/social_programs.parquet', format='parquet')\n")


# In[4]:


df_joined = df_appplications.join(df_programs, on="ProgramID", how="inner")


# In[7]:


df_joined.write.partitionBy("ProgramName").format("delta").save("abfss://experimentation@esdcdatalakehudua.dfs.core.windows.net/delta/application_social_programs")


# In[8]:


spark.sql("CREATE TABLE application_social_programs USING DELTA LOCATION 'abfss://experimentation@esdcdatalakehudua.dfs.core.windows.net/delta/application_social_programs'")


# In[9]:


get_ipython().run_cell_magic('sql', '', '\nselect * from application_social_programs\n')


# In[14]:


get_ipython().run_cell_magic('sql', '', '\ndescribe history application_social_programs\n')


# In[11]:


get_ipython().run_cell_magic('sql', '', '\nDELETE from application_social_programs where programid = 4\n')


# In[18]:


get_ipython().run_cell_magic('sql', '', '\nselect count(*) from application_social_programs version as of 1\n')


# In[ ]:




