#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
pd.set_option("display.max_columns", 200)

pd.options.mode.copy_on_write = True


# In[2]:


# Read in the Active Grant csv and store into Pandas DataFrame
# https://data.hrsa.gov//DataDownload/DD_Files/EHB_ACTIVE_GRANT_FA_AGR.csv (source file)
ehb_active_path = Path("data/EHB_ACTIVE_GRANT_FA_AGR.csv")
ehb_active_df = pd.read_csv(ehb_active_path, encoding="utf-8")

ehb_active_df.head(2)


# In[3]:


# isolate 2023 data
ehb_active_2023_df = ehb_active_df[(ehb_active_df['Award Year'] == 2023)]

ehb_active_2023_df.head(2)


# In[4]:


# Number of unique grant programs
len(ehb_active_df['Grant Program Name'].unique())


# In[5]:


# look at how the naming is formated
names = ehb_active_df[(ehb_active_df['HRSA Program Area Name'] == 'Maternal and Child Health')]
names['Grant Program Name'].unique()


# In[6]:


# create condensed df
code_for_program_df =names[['Grant Activity Code', 'Grant Program Name', 'HRSA Program Area Name']]

code_for_program_df


# In[7]:


# Remove duplicates from column 'Grant Activity Code'
code_for_program_df = code_for_program_df.drop_duplicates(subset = 'Grant Activity Code')

code_for_program_df


# In[8]:


# drop null values
code_for_program_df.dropna().copy()

# widen columns in df to show the end of 'Grant Program Name'
pd.set_option('display.max_colwidth', None)

code_for_program_df


# In[9]:


# Slice off 'Grant Activity Code' form 'Grant Program Name'
###***** don't run this cell more than once, it will contiuouly slice 5 from the end of the string

code_for_program_df['Grant Program Name'] = code_for_program_df['Grant Program Name'].str.slice(0, -5)

code_for_program_df


# In[10]:


# Number of unique grant programs
len(code_for_program_df['Grant Program Name'].unique())


# In[ ]:


# export df to a .csv file
code_for_program_df.to_csv('data/output/grant_program_codes.csv', index=False)

