
# coding: utf-8

# ## Question 2 Part 2:
# 
# ### Find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# 
# ### For each job family these people are associated with (job family refers to ’Job Family' column), calculate what is the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column (Percent_total_benefit) which has the percentage value.
# 

# In[42]:

import pandas as pd


# In[43]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/employee_compensation.csv')


# In[44]:

#Find all the Unique Job Families
UniqueJobFamilies=[]
for index, rows in df.iterrows():
    if(rows['Job Family'] not in UniqueJobFamilies):
        UniqueJobFamilies.append(rows['Job Family'])
    


# In[45]:

len(UniqueJobFamilies)


# In[46]:

#Find the total Benefit and the Total Compensation of each Job Family
TotalBenefit=[0]*58
TotalCompensation=[0]*58
total=[0]*58
for index, rows in df.iterrows():
    for i in range(1,59):
        if((UniqueJobFamilies[i-1]==rows['Job Family']) and ((rows['Salaries']*(5/100))<rows['Overtime'])):
            TotalBenefit[i-1]=TotalBenefit[i-1]+rows['Total Benefits']
            TotalCompensation[i-1]=TotalCompensation[i-1]+rows['Total Compensation']
            total[i-1]+=1


# In[47]:

#Find the average Value of the Total Benefit and the Total Compensation of all the Job Families
averageTotalBenefit=[0]*58
averageTotalCompensation=[0]*58
for i in range(1,(len(total)+1)):
    if(total[i-1]!=0):
        averageTotalBenefit[i-1]=TotalBenefit[i-1]/total[i-1]
        averageTotalCompensation[i-1]=TotalCompensation[i-1]/total[i-1]
    else:
        averageTotalBenefit[i-1]=0
        averageTotalCompensation[i-1]=0


# In[48]:

#Percent of Total Benefit with respect to Total Compensation
percentTotalBenefit=[0]*58
for i in range(1,59):
    if(averageTotalCompensation[i-1]!=0):
        percentTotalBenefit[i-1]=(averageTotalBenefit[i-1]/averageTotalCompensation[i-1])*100
    else:
        percentTotalBenefit[i-1]=0


# In[49]:

df1=pd.DataFrame({'Job Family':UniqueJobFamilies,'Total Benefit':averageTotalBenefit,'Total Compensation':averageTotalCompensation,'Percent_Total_Benefit':percentTotalBenefit})


# In[50]:

df1=df1.sort_values(by='Percent_Total_Benefit',ascending=False)


# In[51]:

df1.head()


# In[52]:

df1.to_csv('Percent_Total_Benefit.csv', sep=';', encoding='utf-8')

