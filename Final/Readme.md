
# Analysis on college majors Data set

The topic has always been debated on- "Which major is considered best for a student, how would it make one successful?" The college Majors Data set is the data from the American community survey in the years 2010-2011 which estimated median earnings for recent college graduates broken down by major. The survey also conducted gender based analysis and also the average IQ of candidates in each major.

The Dataset consists of the following the data files:
1. all-ages.csv: consists of data of students employed full-time, unemployement rates and median pay for all    age groups
2. grad-students.csv: consists of data of students above the age of 25 who went to college, graduated/not graduated, employed/unemployed and the median pay. It also consists of data of students who did not take up a major in college but are employed in that field.
3. iq-vs-salary-by-major.csv: This dataset consists of data of students by gender, average IQ, median pay.
4. Percentage-bachelors-degrees-women-usa.csv: consists of data of percentage of women in each major through the years 1970-2012
5. recent-grads.csv: consists of data of students below the age of 28 who went to college, graduated/not graduated, employed/unemployed and the median pay. It also consists of data of students who did not take up a major in college but are employed in that field.



**Analysis 1**:

This analysis uses the dataset recent-grads.csv. Here, we calculate the total men and the total women in each major category. We also find the gender ratio. We plot bar graphs for the same using matplotlib.

+ From this analysis, we see that, the number of women in Biology and life sciences,  Education, Health, Arts and Psychology are significantly higher. These major fields are dominated by the women.
![totalmenvstotalwomen](https://cloud.githubusercontent.com/assets/25044482/25308029/4ba02488-277a-11e7-975c-3a53919de9ea.png)
+ The gender ratio of the major fields like Engineering, Business, Law and public safety are much over 100. These major fields are mostly dominated by men
![genderratio](https://cloud.githubusercontent.com/assets/25044482/25308043/7b36e114-277a-11e7-876c-6e8f69d60a8d.png)

**Analysis 2**:

This analysis uses the dataset grad-students.csv. We find the number of students between the age group of 25-28. The findings are plotted on a bar graph.

+ We see that the number of students between the age group 25-28 are maximum in the education major. Jounalism has least number of students in this age group.
![gradsbetween25-28](https://cloud.githubusercontent.com/assets/25044482/25308051/9d00dae8-277a-11e7-9b0e-422a0fdebdd1.png)

**Analysis 3:**

This is a pattern analysis of the data from grad-students.csv. We analyse the dataset to observe the following:

+ The unemployment rates among non-grad students are always higher. Candodates who went to college had more chances of employment in every major.
![unemploymentratesgradsvsnongrads](https://cloud.githubusercontent.com/assets/25044482/25308077/25c43be0-277b-11e7-8a27-82f70213cb3a.png)
+ Among the candidates who were employed, The candidates in the business major were mostly non-grad candidates. 
![grademployedvsnongrademployed](https://cloud.githubusercontent.com/assets/25044482/25308060/e66f0b78-277a-11e7-937a-5075a461298e.png)
+ Most of the grad students and non grad students in every major were employed with full-time jobs (>35 hours a week) and very few were employed with half time jobs
![nongrademployedfulltimevsnongrademployedhalftime](https://cloud.githubusercontent.com/assets/25044482/25308068/fe9a8fc4-277a-11e7-8cc5-7e9578d1f69c.png)

**Analysis 4:**

In this analysis, we find the total number of men and women in each major. We also find the number of women compared to median pay. The female-dominated majors make less on average than male-dominated majors.

+ The majors which are mostly dominated by women have lower median pay. Education is a major which is mostly dominated by women. But the median pay in this field is one of the lowest
![comparisionnumberofmenwomen](https://cloud.githubusercontent.com/assets/25044482/25308087/595337cc-277b-11e7-886d-c20c555434a6.png)
+ The majors dominated by men are mostly business and Engineering. These fields are the highest paid. 
![percentage_femalevsmedian](https://cloud.githubusercontent.com/assets/25044482/25308092/6ea982b6-277b-11e7-8da4-d71ee8c8bd76.png)

**Analysis 5:**

In this Analysis, we find the percentage of women in each major through the years. We also compare the avaerage IQ of candidates in each major as compared to the percentage of women.

+ We notice that the number of women enrolled in each major has significantly increases. Especially in the Engineering and business major
![percentageofwomenvsyear](https://cloud.githubusercontent.com/assets/25044482/25308099/8c68129a-277b-11e7-8499-3577d52b466f.png)
+ From the scatter plot, we observe that the majors having highest percentage of female have low average IQs. A naive reader may look at this graph and conclude that men are smarter than women, but it is vital to note that, on average, men and women have about the same IQ.
![percentage_femalevsaverage_iq](https://cloud.githubusercontent.com/assets/25044482/25308103/9addec32-277b-11e7-872c-2743dc2af1fa.png)

**Analysis 6:**

In this Analysis, we find the majors which have maximum number of gradutes compared to the majors with maximum number of students employed. We find that education major has highest number of graduated students as well has highest employed students

**Analysis 7:**

In this analysis, we do a scatter plot of majors where in students have scored maximum in SAT.

![averagesat](https://cloud.githubusercontent.com/assets/25044482/25636415/5039b694-2f4f-11e7-853a-f8ccc8d8bec5.png)
![quantsat](https://cloud.githubusercontent.com/assets/25044482/25636420/53d67d96-2f4f-11e7-91b4-c18d9f09f75c.png)
![verbalsat](https://cloud.githubusercontent.com/assets/25044482/25636429/5686bbb4-2f4f-11e7-8706-3d4e0c76144b.png)

+ We notice that students in the business field have maximum Verbal SAT, Quant SAT and also Average SAT

```python

```
