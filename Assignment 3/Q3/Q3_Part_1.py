
# coding: utf-8

# ## Question 3 Part 1
# ### Calculate the average Score of each team that hosted and won the game

# In[28]:

import pandas as pd


# In[29]:

df=pd.read_csv('C:/Users/Raksha/Desktop/Spring 2017/DATA Analysis/Intro to python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/cricket_matches.csv')


# In[30]:

#Find all the home teams that hosted and Won the games
home=[]
for index,rows in df.iterrows():
    if(rows['home'] not in home and rows['home']==rows['winner']):
        home.append(rows['home'])


# In[31]:

len(home)


# In[32]:

#Find the total Score of each home team which hosted and won the game
score=[0]*275
total=[0]*275
for index,rows in df.iterrows():
    if(rows['home']==rows['winner']):
        i=home.index(rows['home'])
        if(rows['innings1_runs']>rows['innings2_runs']):
            score[i]=score[i]+rows['innings1_runs']
        else:
            score[i]=score[i]+rows['innings2_runs']
        total[i]+=1


# In[33]:

#Find the average score of each team
averageScore=[0]*275
for i in range(1,276):
    averageScore[i-1]=score[i-1]/total[i-1]


# In[34]:

df1=pd.DataFrame({'Home':home,'Average Score':averageScore})


# In[35]:

df1=df1.sort_values(by='Average Score',ascending=False)


# In[36]:

df1.head()


# In[37]:

df1.to_csv('Average_Score.csv', sep=';', encoding='utf-8')


# In[ ]:



