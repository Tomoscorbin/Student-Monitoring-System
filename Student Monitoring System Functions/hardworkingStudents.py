import pandas as pd
import numpy as np
import functools
import sqlite3


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

print(hardworking())
