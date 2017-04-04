
# coding: utf-8

# ## Question 1 Part 1:
# ### For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City

# In[47]:

import pandas as pd
import datetime


# In[48]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv')


# In[49]:

#Since date is of type object, it has been converted to the type datetime
df['DATE']=pd.to_datetime(df['DATE'], format='%m/%d/%y')


# In[50]:

df_date=df['DATE']


# In[51]:

#Extracting month and year from each date
df['Month'] = df['DATE'].map(lambda x: x.month)
df['Year'] = df['DATE'].map(lambda y: y.year)


# In[52]:

#total collisions per month in NYC in 2016
totalCollisionsPerMonthInNYC=[0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(1,13):
    for y in df[df.Year==2016].Month:
        if x==y:
            totalCollisionsPerMonthInNYC[y-1]+=1
totalCollisionsPerMonthInNYC
        


# In[53]:

#total collisions per month in manhattan in 2016
totalCollisionsPerMonthInManhattan=[0,0,0,0,0,0,0,0,0,0,0,0]
for index, rows in df.iterrows():
    if((rows['BOROUGH']=='MANHATTAN')and(rows['Year']==2016)):
        for i in range(1,13):
            if i==rows['Month']:
                totalCollisionsPerMonthInManhattan[i-1]+=1
totalCollisionsPerMonthInManhattan


# In[54]:

#percentage of collisions each month in manhattan in 2016
percentageOfCollisionsPerMonth=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,13):
    percentageOfCollisionsPerMonth[i-1]=(totalCollisionsPerMonthInManhattan[i-1]/totalCollisionsPerMonthInNYC[i-1])
percentageOfCollisionsPerMonth
    


# In[55]:

df1=pd.DataFrame({'Month':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],'Manhattan':totalCollisionsPerMonthInManhattan,'NYC':totalCollisionsPerMonthInNYC,'Percentage':percentageOfCollisionsPerMonth})
df1.head()


# In[56]:

df1.to_csv('PercentageOfCollisions.csv', sep=';', encoding='utf-8')


# In[ ]:



