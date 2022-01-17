from DAFunction import *
import functools
import sqlite3
import pandas as pd

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

## test code
print(IntersecOfSets([1, 2, 3],
                     [3, 4, 5],
                     [3, 1, 6],
                     [0, 5, 3],
                     [9, 3, 8]))
print(underperf_grades([10, 60, 13]))
print(underperforming())


