
# coding: utf-8

# ## Question 1 Part 2:
# ### For each borough, find out distribution of each collision scale

# In[33]:

import pandas as pd


# In[41]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv')
df


# In[35]:

#Find all the unique Boroughs
newBorough=[]
for index,rows in df.iterrows():
    if((rows['BOROUGH'] not in newBorough)and not(pd.isnull(rows['BOROUGH']))):
        newBorough.append(rows['BOROUGH'])


# In[36]:

newBorough


# In[37]:

#Find the collisions involving one,two three or more vehicles in each borough
oneVehicleInvolved=[0,0,0,0,0]
twoVehicleInvolved=[0,0,0,0,0]
threeVehicleInvolved=[0,0,0,0,0]
moreVehicleInvolved=[0,0,0,0,0]
for index,rows in df.iterrows():
    if(pd.isnull(rows['VEHICLE 2 TYPE'])):
        for i in range(1,(len(newBorough)+1)):
            if(rows['BOROUGH']==newBorough[i-1]):
                oneVehicleInvolved[i-1]+=1
    elif(pd.isnull(rows['VEHICLE 3 TYPE'])):
        for i in range(1,(len(newBorough)+1)):
            if(rows['BOROUGH']==newBorough[i-1]):
                twoVehicleInvolved[i-1]+=1
    elif(pd.isnull(rows['VEHICLE 4 TYPE'])):
        for i in range(1,(len(newBorough)+1)):
            if(rows['BOROUGH']==newBorough[i-1]):
                threeVehicleInvolved[i-1]+=1
    else:
        for i in range(1,(len(newBorough)+1)):
            if(rows['BOROUGH']==newBorough[i-1]):
                moreVehicleInvolved[i-1]+=1


# In[38]:

df1=pd.DataFrame({'BOROUGH':newBorough,'One_Vehicle_Involved':oneVehicleInvolved,'Two_Vehicle_Involved':twoVehicleInvolved,'Three_Vehicle_Involved':threeVehicleInvolved,'More_Vehicle_Involved':moreVehicleInvolved})


# In[39]:

df1


# In[40]:

df1.to_csv('VehiclesInvolved.csv', sep=';', encoding='utf-8')


# In[ ]:



