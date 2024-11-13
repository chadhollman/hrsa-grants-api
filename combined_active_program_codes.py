#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
pd.set_option("display.max_columns", 200)

pd.options.mode.copy_on_write = True


# In[2]:


# read in 1st csv file
codes_active_df = pd.read_csv('data/output/grant_program_codes.csv', encoding = "utf-8")

codes_active_df


# In[3]:


# read in 2nd csv file
codes_missed_active_df = pd.read_csv('data/output/missed_grant_program_codes.csv', encoding = "utf-8")

codes_missed_active_df


# In[4]:


# combine df using 'concat'
combined_active_codes = pd.concat([codes_active_df, codes_missed_active_df], ignore_index=True)

# widen columns in df to show the end of 'Grant Program Name'
pd.set_option('display.max_colwidth', None)

combined_active_codes


# In[8]:


# rename columns
combined_active_codes.rename(columns={'Grant Activity Code': 'Grant_Activity_Code ',
                                 'Grant Program Name': 'Grant_Program_Name',
                                 'HRSA Program Area Name': 'HRSA_Program_Area_Name'}, inplace=True)

combined_active_codes.head(2)


# In[5]:


# export df to a csv file
combined_active_codes.to_csv('data/output/combined_active_program_codes.csv', index=False)

