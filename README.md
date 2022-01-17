# Student-Monitoring-System
## A simple student monitoring system for a module leader/lecturer

This student monitoring system allows the user to check whether students have engaged with their 
formative and summative tests.

There are four main components to the system:
1) Test Results
2) Student Performance
3) Underperforming Students
4) Hardworking Students

- Test Results requires the user to enter the student ID number of the student they wish to review. The user can
then either click 'Results' to view a dataframe of the student's results, or 'Plot Results' to view a linechart
of the student's results.

- Student Performance requires two inputs. The first is the name of the test written with underscores instead of 
spaces (e.g. Formative_Test_1, Formative_Test_2, SumTest, etc), and the second is the student's ID number. The user 
can then click 'Absolute Grade' to view the student's grade for that test, or 'Relative Grade' to view the student's relative grade
for that test. Relative grade is calculated by subtracting the student's absolute grade from the average grade earned 
by all students for that test. 

- Underperforming Students will display a dataframe of the students who have underperformed in the module as a whole.
Underpforming students are defined as those who receive grades well below the average in every test. That is, students 
whose relative performance is less than -10 (0 being average). A threshold of -10 will exclude students who were very 
close to the average. Since the average grade may be high, some students could receive high grades and still be below 
the average. It is, however, possible that a student receives high grades for one or two tests and low grades for the rest. 
The user will be able to view all of the test scores of each 'underperforming' student to determine for themselves. 
To exclude disengaged students, students who failed to take two or more formative tests are not considered. The lowest
score achieved for the Formative Tests will be highlighted with '*'.

- Hardworking Students will display a dataframe of the hardest working students. Hardworking 
students are defined as those who self-describe as 'beginner' or 'below beginner' but who nonetheless received a grade of 
above 60 for their Summative Test.
