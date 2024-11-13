#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
pd.set_option("display.max_columns", 200)


# In[2]:


ehb_active_path = Path("data/EHB_ACTIVE_GRANT_FA_AGR.csv")
# https://data.hrsa.gov//DataDownload/DD_Files/EHB_ACTIVE_GRANT_FA_AGR.csv

# Read the Grant csv and store into Pandas DataFrame
ehb_active_df = pd.read_csv(ehb_active_path, encoding="utf-8")
# ehb_active_df.head()


# In[3]:


ehb_active_2023_df = ehb_active_df[(ehb_active_df['Award Year'] == 2023)].copy()
# ehb_active_df.dtypes


# In[4]:


ehb_active_2023_df.drop('Unnamed: 29', axis= 1, inplace = True)
ehb_active_2023_df.drop('Grant Program Description', axis= 1, inplace = True)
ehb_active_2023_df.drop('Abstract', axis= 1, inplace = True)
ehb_active_2023_df.drop('Unique Entity Identifier', axis= 1, inplace = True)
ehb_active_2023_df.drop('Uniform Data System Grant Program Description', axis= 1, inplace = True)
ehb_active_2023_df.drop('U.S. - Mexico Border 100 Kilometer Indicator', axis= 1, inplace = True)
ehb_active_2023_df.drop('U.S. - Mexico Border County Indicator', axis= 1, inplace = True)


# In[5]:


ehb_active_2023_df.dropna(inplace = True)
ehb_active_clean = ehb_active_2023_df.copy()


# In[6]:


ehb_active_clean.head(1)
# Number of unique grant programs
len(ehb_active_clean['Grant Program Name'].unique())


# In[7]:


# ehb_active_clean["HRSA Program Area Name"].unique()
temp = ehb_active_clean[(ehb_active_clean["HRSA Program Area Name"] == 'Rural Health')]
temp['Grant Program Name'].unique()



# In[8]:


ehb_active_maternal = ehb_active_clean[(ehb_active_clean["HRSA Program Area Name"] == 'Maternal and Child Health')]
ehb_active_clean = ehb_active_maternal.rename(columns=lambda x: x.replace(" ", "_").replace(".", ""))
ehb_active_clean.insert(0, 'ID', range(880, 880 + len(ehb_active_clean)))
ehb_active_clean.to_csv("data/output/maternal_ehb_active.csv", index=False)


# In[9]:


# for finding missing relevant data
key = ehb_active_clean["HRSA_Program_Area_Name"]=='Maternal and Child Health'
nonmaternal_df = ehb_active_clean[~key]
maternal_df=ehb_active_clean[key]
missedstuff_df = nonmaternal_df[nonmaternal_df['Grant_Program_Name'].str.contains('Infant|Maternal|Pregnan', regex=True, case=False)]
missedstuff_df = missedstuff_df.drop_duplicates(subset=('Grant_Program_Name'))
missedstuff_df


# Cleaning code for Awarded Grants data

# In[10]:


ehb_awarded_path = Path("data/FS_EHB_AWARD_GRANT_FA_AGR_MVX.csv")
# https://data.hrsa.gov//DataDownload/DD_Files/EHB_ACTIVE_GRANT_FA_AGR.csv

# Read the Grant csv and store into Pandas DataFrame
ehb_awarded_df = pd.read_csv(ehb_awarded_path, encoding="utf-8")
ehb_awarded_df.head()


# In[11]:


ehb_awarded_2013_df = ehb_awarded_df[(ehb_awarded_df['Award Year'] == 2023)].copy()
#ehb_awarded_df.dtypes


# In[12]:


ehb_awarded_2013_df.drop('Unnamed: 43', axis= 1, inplace = True)
ehb_awarded_2013_df.drop('Abstract', axis= 1, inplace = True)
ehb_awarded_2013_df.drop('U.S. - Mexico Border 100 Kilometer Indicator', axis= 1, inplace = True)
ehb_awarded_2013_df.drop('U.S. - Mexico Border County Indicator', axis= 1, inplace = True)
ehb_awarded_2013_df.drop('Uniform Data System Grant Program Description', axis= 1, inplace = True)
# ehb_awarded_2013_df.drop('Unique Entity Identifier', axis= 1, inplace = True)
# considered removing, but it matches data in other datasets


# In[13]:


ehb_awarded_2013_df.dropna(inplace = True)
ehb_awarded_clean = ehb_awarded_2013_df.copy()


# In[14]:


ehb_awarded_clean.head(1)
# Number of unique grant programs
len(ehb_awarded_clean['Grant Program Name'].unique())


# In[15]:


# ehb_active_clean["HRSA Program Area Name"].unique()
temp = ehb_awarded_clean[(ehb_awarded_clean["HRSA Program Area Name"] == 'Rural Health')]
temp['Grant Program Name'].unique()


# In[16]:


ehb_awarded_maternal = ehb_awarded_clean[(ehb_awarded_clean["HRSA Program Area Name"] == 'Maternal and Child Health')]
ehb_awarded_clean = ehb_awarded_maternal.rename(columns=lambda x: x.replace(" ", "_").replace(".", ""))
ehb_awarded_clean.to_csv("data/output/maternal_ehb_awarded.csv", index=False)


# Cleaning code for Awarded Grants data

# In[17]:


ehb_2023_path = Path("data/Data_Explorer_Dataset.csv")
# https://data.hrsa.gov//DataDownload/DD_Files/EHB_ACTIVE_GRANT_FA_AGR.csv

# Read the Grant csv and store into Pandas DataFrame
ehb_2023_df = pd.read_excel(ehb_2023_path)
ehb_2023_df.head()


# In[18]:


ehb_2023_grants = ehb_2023_df[(ehb_2023_df["HRSA Program Area"] == 'Maternal and Child Health')]
ehb_2023_clean = ehb_2023_grants.rename(columns=lambda x: x.replace(" ", "_").replace(".", "").replace("#", "Number"))
ehb_2023_clean.to_csv("data/output/maternal_ehb_2023.csv", index=False)


# In[ ]:





# WIC program dat

# In[19]:


# there are additional worksheets that can be looked. The one we loaded is the total of those sheets
wic_xls = pd.read_excel("data/wicagencies2023ytd-10.xlsx", sheet_name=['Total Women'], skiprows = 4)
wic_xls_df = wic_xls['Total Women']
wic_xls_df


# In[20]:


wic_xls_clean = wic_xls_df.dropna().copy()
# wic_xls_clean.columns = [str(col).replace(" 00:00:00", "") for col in wic_xls_clean.columns]
wic_xls_clean.columns = [str(col).replace(" 00:00:00", "").replace(" ", "_") for col in wic_xls_clean.columns]
wic_xls_clean


# In[21]:


wic_xls_clean.rename(columns={'2022-10-01': 'October_2022', '2022-11-01': 'November_2022', '2022-12-01': 'December_2022',
                              '2023-01-01': 'January_2023', '2023-02-01': 'February_2023', '2023-03-01': 'March_2023',
                              '2023-04-01': 'April_2023', '2023-05-01': 'May_2023', '2023-06-01': 'June_2023',
                              '2023-07-01': 'July_2023', '2023-08-01': 'August_2023', '2023-09-01': 'September_2023'}, inplace=True)
wic_xls_clean
                            


# In[22]:


wic_xls_clean.insert(0, 'ID', range(880, 880 + len(wic_xls_clean)))
wic_xls_clean.to_csv("data/output/wic_totals.csv", index=False)


# In[23]:


wic_state_xls = pd.read_excel("data/26wifypart-10.xlsx", skiprows = 2)
wic_state_xls_df = wic_state_xls.rename(columns=lambda x: x.replace(" ", "").replace("/", "-").replace("\n", ""))
wic_state_xls_df


# In[24]:


wic_state_xls_df.rename(columns={'State-IndianTribe': 'State_Indian_Tribe'}, inplace=True)	
wic_state_xls_df


# In[25]:


# wic_state_rename_df = wic_state_xls_df.rename(columns={'FY 2023\n': 'FY 2023'})
wic_state_xls_clean = wic_state_xls_df.dropna().copy()
wic_state_xls_clean.insert(0, 'ID', range(880, 880 + len(wic_state_xls_clean)))
wic_state_xls_clean.to_csv("data/output/wic_states.csv", index=False)


# In[26]:


ehb_grantee_path = Path("data/MCHB_Data_GranteeDetails.csv")
# https://data.hrsa.gov//DataDownload/DD_Files/EHB_ACTIVE_GRANT_FA_AGR.csv

# Read the csv and store into Pandas DataFrame
ehb_grantee_df = pd.read_excel(ehb_grantee_path)
ehb_grantee_clean = ehb_grantee_df.rename(columns=lambda x: x.replace(" ", "_"))
ehb_grantee_clean.insert(0, 'ID', range(880, 880 + len(ehb_grantee_clean)))
ehb_grantee_clean.to_csv("data/output/maternal_ehb_grantees.csv", index=False)

