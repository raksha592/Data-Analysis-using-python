
# coding: utf-8

# ## Question 2 Part 1:
# ### Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.

# In[30]:

import pandas as pd


# In[31]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/employee_compensation.csv')


# In[32]:

#Find each department and their corresponding Organization Group
newOrganizationGroup=[]
newDepartment=[]
for index,rows in df.iterrows():
    if((rows['Department'] not in newDepartment)):
        newDepartment.append(rows['Department'])
        newOrganizationGroup.append(rows['Organization Group'])


# In[33]:

#Find the total Compensation of each Department
totalCompensation=[0]*56
j=[0]*56
for index,rows in df.iterrows():
    for i in range(1,(len(newDepartment)+1)):
        if rows['Department']==newDepartment[i-1]:
            totalCompensation[i-1]=rows['Total Compensation']+totalCompensation[i-1]
            j[i-1]+=1
    


# In[34]:

#Find mean of the total Compensation of each department
meanCompensation=[0]*56
for k in range(1,(len(j)+1)):
    meanCompensation[k-1]=totalCompensation[k-1]/j[k-1]


# In[35]:

df1=pd.DataFrame({'Organization Group':newOrganizationGroup,'Department':newDepartment,'Total Compensation':meanCompensation})
df1=df1.sort_values(by='Total Compensation',ascending=False) #Sorting values from highest to lowest
df1.head()


# In[36]:

df1.to_csv('TotalComensation.csv', sep=';', encoding='utf-8')


# In[ ]:



