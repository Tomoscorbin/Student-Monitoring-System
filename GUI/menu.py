from DAFunction import *
from tkinter import *
from tkinter import ttk

### test results window & functions
def test_results_window():
     
    tr_window = Tk()
    tr_window.geometry("400x300")
    tr_window.pack_propagate(False)
    tr_window.resizable(0, 0)

    def clear_data():
        tv.delete(*tv.get_children())


    def display_df():
        clear_data()

        #validating ID
        id_num = e.get()
        id_num = int(id_num)
        label_ts["text"] = ""
        if id_num not in range(1, 157):
            label_ts["text"] = "Invalid ID, try again."
            return None
        else:
            pass
        
        df = return_results(e.get())
    
        tv["column"] = list(df.columns)
        tv["show"] = "headings"
        for column in tv["columns"]:
              tv.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv.insert("", "end", values=row)

        e.delete(0, 'end')

    def res_plot():
        # validating ID
        id_num = e.get()
        id_num = int(id_num)
        label_ts["text"] = ""
        if id_num not in range(1, 157):
            label_ts["text"] = "Invalid ID, try again."
            return None
        else:
            pass
        
        myLabel = Label(tr_window, text=plot_results(e.get()))
        myLabel.pack()

        e.delete(0, 'end')
        
    # frame for Treeview
    frame1 = LabelFrame(tr_window, text="Student Results")
    frame1.place(height=200, width=400)

    # frame for button and entry box
    frame2 = LabelFrame(tr_window, text="Enter student ID")
    frame2.place(height=75, width=300, rely=0.70, relx=0)

    label_ts = Label(frame2,)
    label_ts.place(rely=0, relx=0)

    # entry box
    e = Entry(frame2, width=13)
    e.place(rely=0.57, relx=0.21)

    # results button
    results_button = Button(frame2, text="Results", command=lambda: display_df())
    results_button.place(rely=0.50, relx=0.50)

    # plot button
    plot_btn = Button(frame2, text="Plot Results", command=res_plot)
    plot_btn.place(rely=0.50, relx=0.68)

    #Treeview widget
    tv = ttk.Treeview(frame1)
    tv.place(relheight=1, relwidth=1)

    

### student performance window
def student_perf_window():
    
    performance_window = Tk()
    performance_window.geometry("350x250")
    performance_window.pack_propagate(False)
    performance_window.resizable(0, 0)

    # creating test variable
    def func_1():
        global test
        test = e_1.get()

    # creating id variable
    def func_2():
        global id
        id = e_2.get()

    # absolute grade 
    def get_abs_grade():
        clear_data()
        func_1()
        func_2()

        #validating ID and test name
        id_num = int(id)
        label_frame2["text"] = "" 
        test_names = ["Formative_Test_1",
                      "Formative_Test_2",
                      "Formative_Test_3",
                      "Formative_Test_4",
                      "SumTest"]
        if id_num not in range(1, 157):
            label_frame2["text"] = "Invalid ID, try again."
            return None
        elif test not in test_names:   
            label_frame2["text"] = "Incorrect test name, try again."
            return None
        else:
            pass
        
        e_1.delete(0, 'end')
        e_2.delete(0, 'end')
        abs_grade = absolute_grade(test, id)
        tv.insert("", "end", values=abs_grade)

    # relative grade
    def get_rel_grade():
        clear_data()
        func_1()
        func_2()

        #validating ID and test name
        id_num = int(id)
        label_frame2["text"] = "" 
        test_names = ["Formative_Test_1",
                      "Formative_Test_2",
                      "Formative_Test_3",
                      "Formative_Test_4",
                      "SumTest"]
        if id_num not in range(1, 157):
            label_frame2["text"] = "Invalid ID, try again."
            return None
        elif test not in test_names:   
            label_frame2["text"] = "Incorrect test name, try again."
            return None
        else:
            pass
        e_1.delete(0, 'end')
        e_2.delete(0, 'end')
        rel_grade = relative_grade(test, id)
        tv.insert("", "end", values=rel_grade)

    def clear_data():
        tv.delete(*tv.get_children())

    # frame for Treeview
    frame1 = LabelFrame(performance_window, text="Student Performance")
    frame1.place(height=70, width=125)

    # frame for buttons and entryboxes
    frame2 = LabelFrame(performance_window, text="Enter Test and Student ID")
    frame2.place(height=155, width=350, rely=0.35, relx=0)

    label_frame2 = Label(frame2, text="")
    label_frame2.place(rely=0, relx=0)

    # entry boxes        
    e_1 = Entry(frame2)
    e_1.place(rely=0.30, relx=0.32)
    e_2 = Entry(frame2)
    e_2.place(rely=0.46, relx=0.32)

    # buttons
    btn1 = Button(frame2, text="Absolute Grade", command=lambda: get_abs_grade())
    btn1.place(rely=0.65, relx=0.23)
    btn2 = Button(frame2, text="Relative Grade", command=lambda: get_rel_grade())
    btn2.place(rely=0.65, relx=0.51)

    # labels
    label_1 = Label(frame2, text="Test:")
    label_1.place(rely=0.30, relx=0.20)
    label_2 = Label(frame2, text="ID:")
    label_2.place(rely=0.46, relx=0.21)
    label_3 = Label(frame2, text="E.g. Formative_Test_1 \n or SumTest")
    label_3.place(rely=0, relx=0.60)

    # Treeview widget
    tv = ttk.Treeview(frame1)
    tv['columns'] = ("Grade")
    tv.column("#0", width=0)
    tv.column("Grade", anchor=W)
    tv.heading("#0")
    tv.place(relheight=1, relwidth=1)


### underperformance window and functions

def underperf_window():
    underperformance_window = Tk()
    underperformance_window.geometry("620x300")
    underperformance_window.pack_propagate(False)
    underperformance_window.resizable(0, 0)

    def clear_data():
        tv.delete(*tv.get_children())

    df = underperforming()
    def display_df():
        clear_data()
    
        tv["column"] = list(df.columns)
        tv["show"] = "headings"
        for column in tv["columns"]:
              tv.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv.insert("", "end", values=row)

    # frame for Treeview
    frame1 = LabelFrame(underperformance_window, text="Underperforming Students")
    frame1.place(height=200, width=600)

    # frame for button
    button_frame = LabelFrame(underperformance_window)
    button_frame.place(height=75, width=500, rely=0.73, relx=0)

    #button
    button = Button(button_frame, text="Click here", command=lambda: display_df())
    button.place(rely=0.60, relx=0.50)

    label_button_frame = Label(button_frame, text="Press the button to view underperforming students")
    label_button_frame.place(rely=0, relx=0)

    #Treeview widget
    tv = ttk.Treeview(frame1)
    tv.place(relheight=1, relwidth=1)

    treescrolly = Scrollbar(frame1, orient="vertical", command=tv.yview)
    treescrollx = Scrollbar(frame1, orient="horizontal", command=tv.xview)

    tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrolly.pack(side="right", fill="y")
    treescrollx.pack(side="bottom", fill="x")


### hardworking window and functions

def hardworking_window():
    hardworking_window = Tk()
    hardworking_window.geometry("600x400")
    hardworking_window.pack_propagate(False)
    hardworking_window.resizable(0, 0)

    def clear_data():
        tv.delete(*tv.get_children())

    df = hardworking()
    def display_df():

        clear_data()
    
        tv["column"] = list(df.columns)
        tv["show"] = "headings"
        for column in tv["columns"]:
            tv.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv.insert("", "end", values=row)
    
        return None

    # frame for Treeview
    frame1 = LabelFrame(hardworking_window, text="Hardworking Students")
    frame1.place(height=250, width=600)

    # frame for opening dataframe
    open_df_frame = LabelFrame(hardworking_window)
    open_df_frame.place(height=75, width=500, rely=0.65, relx=0)

    # button
    button = Button(open_df_frame, text="Click here", command=lambda: display_df())
    button.place(rely=0.65, relx=0.50)

    label_open_df = Label(open_df_frame, text="Press the button to view hardworking students")
    label_open_df.place(rely=0, relx=0)

    #Treeview widget
    tv = ttk.Treeview(frame1)
    tv.place(relheight=1, relwidth=1)

    treescrolly = Scrollbar(frame1, orient="vertical", command=tv.yview)
    tv.configure(yscrollcommand=treescrolly.set)
    treescrolly.pack(side="right", fill="y")
                                                       

# main menu window
root = Tk()
root.title("Main Menu")
root.geometry("155x250")
label = Label(root,
              text="Main Menu")
label.pack(pady=10)

# test results button
tr_btn = Button(root,
                text="Test Results",
                command=test_results_window)
tr_btn.pack(pady=10)

#student performance button
perf_btn = Button(root,
                  text = "Student Performance",
                  command=student_perf_window)
perf_btn.pack(pady=10)

# underperforming students button
underperf_btn = Button(root,
                       text="Underperforming Students",
                       command=underperf_window)
underperf_btn.pack(pady=10)

# hardworking students button
hardworking_btn = Button(root,
                         text="Hardworking Students",
                         command=hardworking_window)
hardworking_btn.pack(pady=10)

root.mainloop()
