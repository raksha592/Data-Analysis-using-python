
# coding: utf-8

# ## Question 4 part 1
# 
# ### You are supposed to extract data from the awards column in this dataset and split it into several columns

# In[114]:

import pandas as pd


# In[115]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/movies_awards.csv')


# In[116]:

#Creating seperate columns for all award nominations and wins
df['Awards_Won'] = df['Awards'].str.extract('(\d+) win', expand=True)
df['Awards_Nominated'] = df['Awards'].str.extract('(\d+) nomination', expand=True)
df['PrimeAwards_Won']= df['Awards'].str.extract('Won (\d+) Primetime', expand=True)
df['PrimeAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
df['BaftaAwards_Won']= df['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
df['BaftaAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
df['OscarAwards_Won']= df['Awards'].str.extract('Won (\d+) Oscar', expand=True)
df['OscarAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
df['GoldenGlobeAwards_Won']= df['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
df['GoldenGlobeAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)


# In[117]:

awardsList=df[[15,21,22,23,24,25,26,27,28,29,30]]


# In[118]:

df1 = awardsList.fillna(0)


# In[119]:

#Convert all string values to int for every row of every column
df1['Awards_Won'] = df1['Awards_Won'].astype(str).astype(int)
df1['PrimeAwards_Won'] = df1['PrimeAwards_Won'].astype(str).astype(int)
df1['BaftaAwards_Won']=df1['BaftaAwards_Won'].astype(str).astype(int) 
df1['OscarAwards_Won']=df1['OscarAwards_Won'].astype(str).astype(int) 
df1['GoldenGlobeAwards_Won']=df1['GoldenGlobeAwards_Won'].astype(str).astype(int)
df1['Awards_Nominated'] =df1['Awards_Nominated'].astype(str).astype(int) 
df1['PrimeAwards_Nominations']=df1['PrimeAwards_Nominations'].astype(str).astype(int)
df1['BaftaAwards_Nominations']=df1['BaftaAwards_Nominations'].astype(str).astype(int)
df1['OscarAwards_Nominations']=df1['OscarAwards_Nominations'].astype(str).astype(int)  
df1['GoldenGlobeAwards_Nominations']=df1['GoldenGlobeAwards_Nominations'].astype(str).astype(int)


# In[120]:

#Total wins for the movie
df1['Awards_Won'] = df1['Awards_Won']+df1['PrimeAwards_Won']+df1['BaftaAwards_Won']+df1['OscarAwards_Won']+df1['GoldenGlobeAwards_Won']


# In[121]:

#total nominations
df1['Awards_Nominated']=df1['Awards_Nominated']+df1['PrimeAwards_Nominations']+df1['BaftaAwards_Nominations']+df1['OscarAwards_Nominations']+df1['GoldenGlobeAwards_Nominations']


# In[122]:

df1.head()


# In[123]:

df1.to_csv('awards.csv')


# In[ ]:



