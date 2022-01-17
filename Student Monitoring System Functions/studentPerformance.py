import sqlite3
import functools
from statistics import *


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


## test code
print(absolute_grade("Formative_Test_1", -1))
print(absolute_grade("Formative_Test_5", 13))
print(absolute_grade("Formative_Test_1", 13))
print(relative_grade("Formative_Test_", 60))
print(relative_grade("Formative_Test_1", 0))
print(relative_grade("Formative_Test_1", 13))
