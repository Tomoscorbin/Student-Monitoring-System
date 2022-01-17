import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import functools


def return_results(id):
    """
    Given a student ID, returns the grades from every test
    the student has taken. Returns 0 for tests the student
    did not take.

        Parameters:
            id(int): The student's ID.

        Returns:
            grades_df(dataframe): A dataframe containing a
                                  single row of the students
                                  results.
    """
    
    # converting strings to ints if needed
    if isinstance(id, str) == True:
        id = int(id)

    # return nothing if ID number incorrect
    if id not in range(1, 157):
        return None
    
    # connect to database
    conn = sqlite3.connect("ResultDatabase.db")
    c = conn.cursor()

    grades = []

    # get Formative Test 1 result
    c.execute("SELECT Grade FROM Formative_Test_1 WHERE research_id = %d" %(id))
    grade = c.fetchall()
    if len(grade) == 0:
        grade = 0
    else:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    grades.append(grade)

    # get Formative Test 2 result
    c.execute("SELECT Grade FROM Formative_Test_2 WHERE research_id = %d" %(id))
    grade = c.fetchall()
    if len(grade) == 0:
        grade = 0
    else:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    grades.append(grade)

    # get Formative Test 3 result
    c.execute("SELECT Grade FROM Formative_Test_3 WHERE research_id = %d" %(id))
    grade = c.fetchall()
    if len(grade) == 0:
        grade = 0
    else:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    grades.append(grade)

    # get Formative Test 4 result
    c.execute("SELECT Grade FROM Formative_Test_4 WHERE research_id = %d" %(id))
    grade = c.fetchall()
    if len(grade) == 0:
        grade = 0
    else:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    grades.append(grade)

    # get Summative Test result
    c.execute("SELECT Grade FROM SumTest WHERE research_id = %d" %(id))
    grade = c.fetchall()
    if len(grade) == 0:
        grade = 0
    else:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    grades.append(grade)

    conn.close()

    # creating dataframe
    grades_df = pd.DataFrame(["Formative Test 1", "Formative Test", "Formative Test 3","Formative Test 4","Summative Test"],
                             columns=['Test'])
    grades = np.array(grades)
    grades_df['Grade'] = grades
                                                               

    return grades_df

        
        
def plot_results(id):
    """
    Given a student's ID, returns a line chart of the student's
    grades for every test taken. Plots a 0 for tests not taken.

        Parameters:
            id(int): The student's ID.

        Returns:
            Returns a line chart with the test names on
            the x-axis and grades on the y-axis.
    """
    
    # converting strings to ints if needed
    if isinstance(id, str) == True:
        id = int(id)

    # return nothing if ID number incorrect
    if id not in range(1, 157):
        return None
    
    grades = return_results(id)
    
    # display plot
    plt.figure(figsize=(7, 4.8))
    
    plt.plot(grades['Test'], grades['Grade'], '-o')

    plt.title("Student %d's Test Results" %(id))
    plt.xlabel("Tests")
    plt.ylabel("Grade")

    plt.ylim(0, 105)

    plt.show()
   
    

## test code
#print(return_results("0"))
print(return_results(130))
print(plot_results(130))
#print(plot_results(200))
