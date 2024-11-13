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
ehb_award_path = Path("data/FS_EHB_AWARD_GRANT_FA_AGR_MVX.csv")
ehb_award_df = pd.read_csv(ehb_award_path, encoding="utf-8")

ehb_award_df.head(2)


# In[3]:


# isolate 2023 data
ehb_award_2023_df = ehb_award_df[(ehb_award_df['Award Year'] == 2023)]

ehb_award_2023_df.head(2)


# In[4]:


# Number of unique grant programs
len(ehb_award_df['Grant Program Name'].unique())


# In[5]:


# look at how the naming is formated
names = ehb_award_df[(ehb_award_df['HRSA Program Area Name'] == 'Maternal and Child Health')]
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


# create a key to narrow results so we can exclude data from 'Maternal and Child Health'
key = ehb_award_2023_df["HRSA Program Area Name"] == 'Maternal and Child Health'
nonmaternal_df = ehb_award_2023_df[~key] # exclude
maternal_df = ehb_award_2023_df[key] # include

# utilize key with 'keywords'
missed_stuff_df = nonmaternal_df[nonmaternal_df['Grant Program Name'].str.contains('Infant|Maternal|Fetus|Unborn|Pregnan|Breast', regex=True, case=False)]

missed_stuff_df


# In[9]:


# drop duplicate rows within 'Grant Program Name' to isolate unique 'Grant Activity Code' not contained within 'Maternal and Child Health'
missed_stuff_df = missed_stuff_df.drop_duplicates(subset = ('Grant Program Name'))

missed_stuff_df


# In[10]:


# create condensed df
missed_stuff_df = missed_stuff_df[['Grant Activity Code', 'Grant Program Name', 'HRSA Program Area Name']]

# widen columns in df to show the end of 'Grant Program Name'
pd.set_option('display.max_colwidth', None)

missed_stuff_df


# In[11]:


# combine df using 'concat'
combined_award_codes = pd.concat([code_for_program_df, missed_stuff_df], ignore_index=True)

# widen columns in df to show the end of 'Grant Program Name'
pd.set_option('display.max_colwidth', None)

# drop null values
combined_award_codes.dropna()

combined_award_codes


# In[12]:


# Slice off 'Grant Activity Code' form 'Grant Program Name'
###***** don't run this cell more than once, it will contiuouly slice 5 from the end of the string

combined_award_codes['Grant Program Name'] = combined_award_codes['Grant Program Name'].str.slice(0, -5)

combined_award_codes


# In[13]:


combined_award_codes = combined_award_codes.drop_duplicates(subset = ('Grant Program Name'))


# In[14]:


# Number of unique grant programs
len(combined_award_codes['Grant Program Name'].unique())


# In[15]:


combined_award_codes


# In[16]:


# rename columns
combined_award_codes.rename(columns={'Grant Activity Code': 'Grant_Activity_Code ',
                                 'Grant Program Name': 'Grant_Program_Name',
                                 'HRSA Program Area Name': 'HRSA_Program_Area_Name'}, inplace=True)

combined_award_codes.head(2)


# In[17]:


# export df to a csv file
combined_award_codes.to_csv('data/output/combined_award_program_codes.csv', index=False)


# In[ ]:




