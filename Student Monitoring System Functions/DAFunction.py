import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import functools
from statistics import *


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



def absolute_grade(test, id):
    """
    Given a student ID and test, returns the grade the
    student received for that test.

        Parameters:
            test(str): The name of the test.
            id(int): The student's ID.

        Returns:
            Returns the grade earned as a float.
    """

    # converting strings to ints if needed
    if isinstance(id, str) == True:
        id = int(id)

    # return nothing if ID number incorrect or test name incorrect
    test_names = ["Formative_Test_1",
                      "Formative_Test_2",
                      "Formative_Test_3",
                      "Formative_Test_4",
                      "SumTest"]
    if id not in range(1, 157):
        return None
    elif test not in test_names:
        return None

    
    
    # database connection
    conn = sqlite3.connect("ResultDatabase.db")
    # cursor
    c = conn.cursor()

    c.execute("SELECT Grade FROM %s WHERE Research_id == %s" %(test, id))
    
    grade = c.fetchall()
    grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
    
    return grade



def relative_grade(test, id):
    """
    Given a student ID and test, returns the student's relative
    grade for that test. The relative grade is calculated by
    subtracting the student's absolute grade from the average
    grade earned by all students.

        Parameters:
            test(str): The name of the test.
            id(int): The student's ID.

        Returns:
            Returns the relative grade as a float.     
    """
    # converting strings to ints if needed
    if isinstance(id, str) == True:
        id = int(id)

    # return nothing if ID number incorrect or test name incorrect
    test_names = ["Formative_Test_1",
                      "Formative_Test_2",
                      "Formative_Test_3",
                      "Formative_Test_4",
                      "SumTest"]
    if id not in range(1, 157):
        return None
    elif test not in test_names:
        return None
    
    ## calculating average grade

    # database connection
    conn = sqlite3.connect("ResultDatabase.db")
    # cursor
    c = conn.cursor()

    c.execute("SELECT Grade FROM %s" %(test))
    tuple_grades = c.fetchall()

    grades = []
    for item in tuple_grades:
        grade = functools.reduce(lambda sub, ele: sub * 10 + ele, item)
        grades.append(grade)

    avg_grade = mean(grades)
    
    ## calculating relative grade (average minus absolute grade)

    # getting absolute grade
    abs_grade = absolute_grade(test, id)

    return round(abs_grade - avg_grade, 2)



def IntersecOfSets(list1, list2, list3, list4, list5):
    """
    Returns the common elements in multiple lists. In this context,
    returns returns the IDs of students who underperformed in every
    test.

        Parameters:
            list1(list): List of student ids who underperformed in test 1.
            list2(list): List of student ids who underperformed in test 2.
            list3(list): List of student ids who underperformed in test 3.
            list4(list): List of student ids who underperformed in test 4.
            list5(list): List of student ids who underperformed in the
                         summative test.

        Return:
            Returns a list containing the ids of students who underperformed
            in all tests.
    """
    
    # Converting arrays into sets
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)
    s4 = set(list4)
    s5 = set(list5)
      
    # Calculating intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)
      
    # Calculates intersection of sets
    # on set1 and s3
    set1 = set1.intersection(s3)

    # Calculates intersection of sets
    # on set1 and s4
    set1 = set1.intersection(s4)

    # Calculates intersection of sets
    # on set1 and s5
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)

    return final_list



def underperf_grades(ids):
    """
    Given a list of IDs, returns each student's results for every test.

        Parameters:
            ids(list): List of student IDs.

        Returns:
            Returns a dataframe containing each students results for each
            test.
    """

    # database connection
    conn = sqlite3.connect("ResultDatabase.db")
    # cursor
    c = conn.cursor()

    grades_dict = {}
    keys = ["ID",
            "Formative Test 1",
            "Formative Test 2",
            "Formative Test 3",
            "Formative Test 4",
            "Summative Test"]
    values = []

    ft1 = []
    ft2 = []
    ft3 = []
    ft4 = []
    st = []

    for i in ids:
    
        c.execute("SELECT Grade FROM Formative_Test_1 WHERE Research_id == %d" % (i))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = 0
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        ft1.append(grade)

        c.execute("SELECT Grade FROM Formative_Test_2 WHERE Research_id == %d" % (i))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = 0
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        ft2.append(grade)

        c.execute("SELECT Grade FROM Formative_Test_3 WHERE Research_id == %d" % (i))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = 0
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        ft3.append(grade)

        c.execute("SELECT Grade FROM Formative_Test_4 WHERE Research_id == %d" % (i))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = 0
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        ft4.append(grade)

        c.execute("SELECT Grade FROM SumTest WHERE Research_id == %d" % (i))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = 0
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        st.append(grade)

    conn.close()

    # creating dataframe columns
    values.extend([ids, ft1, ft2, ft3, ft4, st])

    # creating dataframe
    for key, value in zip(keys, values):
        grades_dict[key] = value

    grades_df = pd.DataFrame(grades_dict)

    # getting index of rows with 0 for more than 1 test
    index_list = []
    for (index_label, row_series) in grades_df.iterrows():
        count = 0
        for i in row_series:
            if i == 0.0:
                count += 1
            if count >= 2 & index_label not in index_list:
                index_list.append(index_label)

    # removing said rows
    grades_df.drop(index_list, inplace=True)

    # sorting dataframe by Summative Test
    grades_df.sort_values(by=['Summative Test'], inplace=True)
        
    return grades_df




def underperforming():
    """
    Returns the grades earned for each test for underperforming students.

        Returns:
            Returns a dataframe containing grades earned by underperforming
            students.
    """

    # database connection
    conn = sqlite3.connect("ResultDatabase.db")
    # cursor
    c = conn.cursor()

    # getting ids of underperforming students of test 1
    
    c.execute("SELECT Research_id, Grade FROM Formative_Test_1")
    ids_and_grades = c.fetchall()
        
    ft1_underperforming = []

    for pair in ids_and_grades:
        if relative_grade("Formative_Test_1", pair[0]) < -10:
            ft1_underperforming.append(pair[0])

    # getting ids of underperforming students of test 2
        
    c.execute("SELECT Research_id, Grade FROM Formative_Test_2")
    ids_and_grades = c.fetchall()
    
    ft2_underperforming = []

    for pair in ids_and_grades:
        if relative_grade("Formative_Test_2", pair[0]) < -10:
            ft2_underperforming.append(pair[0])

    # getting ids of underperforming students of test 3
        
    c.execute("SELECT Research_id, Grade FROM Formative_Test_3")
    ids_and_grades = c.fetchall()
    
    ft3_underperforming = []

    for pair in ids_and_grades:
        if relative_grade("Formative_Test_3", pair[0]) < -10:
            ft3_underperforming.append(pair[0])

    # getting ids of underperforming students of test 4
        
    c.execute("SELECT Research_id, Grade FROM Formative_Test_4")
    ids_and_grades = c.fetchall()
    
    ft4_underperforming = []

    for pair in ids_and_grades:
        if relative_grade("Formative_Test_4", pair[0]) < -10:
            ft4_underperforming.append(pair[0])

    # getting ids of underperforming students of SumTest
        
    c.execute("SELECT Research_id, Grade FROM SumTest")
    ids_and_grades = c.fetchall()
    
    st_underperforming = []

    for pair in ids_and_grades:
        if relative_grade("SumTest", pair[0]) < -10:
            st_underperforming.append(pair[0])

    conn.close()

    # getting a list of students who underperformed on every test        

    underperf_ids = IntersecOfSets(ft1_underperforming, ft2_underperforming, ft3_underperforming, ft4_underperforming, st_underperforming)
       
    final_df = underperf_grades(underperf_ids)

    # getting indexes of min test scores
    index_list = []
    for row in final_df.itertuples():
        min_val = min(row[2:6])
        index = row.index(min_val)
        index_list.append(index)
    index_list = np.array(index_list)
    index_list = index_list - 1

    # highlighting min test scores
    num = 0
    for index, row in final_df.iterrows():
        index = index - 1
        final_df.iloc[index, index_list[num]] = "*{}*".format(final_df.iloc[index, index_list[num]])
        num += 1
    
    return final_df

def hardworking():
    student_rate = pd.read_csv("StudentRate.csv")

    # slicing relevant columns
    student_rate = student_rate.iloc[:, [0,3]]

    # changing column name
    student_rate.rename(columns={student_rate.columns[1]: 'rate'}, inplace=True)

    # filtering students with 'below beginner' or 'beginner' level
    student_rate = student_rate[(student_rate.rate == "Below beginner")|(student_rate.rate == "Beginner")]


    #creating grades column

    # database connection
    conn = sqlite3.connect("ResultDatabase.db")
    # cursor
    c = conn.cursor()
    
    grade_col = []
    for row in student_rate['research id']:
        id = row
        c.execute("SELECT Grade FROM SumTest WHERE Research_id == %d" % (id))
        grade = c.fetchall()
        if len(grade) == 0:
            grade = '0'
        else:
            grade = functools.reduce(lambda sub, ele: sub * 10 + ele, grade[0])
        grade_col.append(grade)
    
    student_rate['grade'] = grade_col
    student_rate['grade'] = student_rate['grade'].astype(int)

    # creating hardworking column
    student_rate = student_rate[(student_rate['grade'] > 60)]
    student_rate = student_rate.sort_values(['grade'], ascending=[False])
    
    # renaming columns
    student_rate.columns = ['ID', 'Rate', 'Grade']
    
    return student_rate
