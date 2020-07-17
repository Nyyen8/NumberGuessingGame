"""
Program: DatabaseQueryGUI.py
Author: Paul Elsea
Last Modified: 07/16/2020

Program to display a GUI for querying a database.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from Database.Code import DatabaseSetup as ds
from Database.Code import Validation as v

''''''
def create_person_press():
    global conn
    if v.valid_name_check(fName.get()):
        if v.valid_name_check(lName.get()):
            with conn:
                person = (fName.get(), lName.get())
                ds.create_person(conn, person)
        else:
            mb.showinfo(title='Last name input error', message='Invalid last name.')
    else:
        mb.showinfo(title='First name input error', message='Invalid first name.')

''''''
def create_student_press():
    global conn
    if v.valid_name_check(fName.get()):
        if v.valid_name_check(lName.get()):
            if v.valid_alpha_check(major.get()):
                if v.valid_date(sDate.get()):
                    if ds.find_person_id(conn, fName.get(), lName.get()) == None:
                        mb.showinfo(title='No person found', message='Person not found. Please check the name.')
                    else:
                        with conn:
                            student = (ds.find_person_id(conn, fName.get(), lName.get()), major.get(), sDate.get())
                            student_id = ds.create_student(conn, student)
                else:
                    mb.showinfo(title='Date input error', message='Invalid date. Please use DD-MM-YYYY format.')
            else:
                mb.showinfo(title='Major input error', message='Invalid major. Please use alphabetic characters'
                                                              ' and spaces only.')
        else:
            mb.showinfo(title='Last name input error', message='Invalid last name.')
    else:
        mb.showinfo(title='First name input error', message='Invalid first name.')


def reset_press():
    global conn
    with conn:
        ds.drop_tables("StudentInfo.db")
        ds.create_tables("StudentInfo.db")
        outputLabel.config(text = 'Database reset')

''''''
def view_person_table():
    global conn
    outputStr = []
    with conn:
        rows = ds.select_all_persons(conn)
        for row in rows:
            outputStr.append(row)

    outputLabel.config(text = print_table_output(outputStr))


''''''
def view_student_table():
    global conn
    outputStr = []
    with conn:
        rows = ds.select_all_students(conn)
        for row in rows:
            outputStr.append(row)

    outputLabel.config(text = print_table_output(outputStr))

''''''
def print_table_output(inputList):
    outputString = ''
    for i in inputList:
        outputString = (outputString + str(i) + '\n')
    return outputString

def test_press():
    global conn
    if ds.find_person_id(conn, fName.get(), lName.get()) == None:
        outputLabel.config(text='No matching person found.')
    else:
        outputLabel.config(text =ds.find_person_id(conn, fName.get(), lName.get()))

'''Defining gui object'''
DatabaseGUI = tk.Tk()
DatabaseGUI.title('Student Records')

'''Establishing DB connection'''
conn = ds.create_connection("StudentInfo.db")

testButton = tk.Button(DatabaseGUI, text='test', width=15, command=test_press).grid(row=7, column=4)

'''Defining input prompt labels'''
fNameLabel = ttk.Label(DatabaseGUI, text="First Name")
fNameLabel.grid(column=0, row=0)

lNameLabel = ttk.Label(DatabaseGUI, text="Last Name")
lNameLabel.grid(column=0, row=1)

majorLabel = ttk.Label(DatabaseGUI, text="Major")
majorLabel.grid(column=0, row=2)

startDateLabel = ttk.Label(DatabaseGUI, text="Start Date")
startDateLabel.grid(column=0, row=3)

'''Defining output label'''
outputLabel = ttk.Label(DatabaseGUI, text="Output")
outputLabel.grid(row=5, columnspan = 3, sticky = tk.W+tk.E)

'''Defining input variables and their text boxes'''
fName = tk.StringVar()
fNameEntered = ttk.Entry(DatabaseGUI, width=20,textvariable=fName)
fNameEntered.grid(column=1, row=0)

lName = tk.StringVar()
lNameEntered = ttk.Entry(DatabaseGUI, width=20, textvariable=lName)
lNameEntered.grid(column=1, row=1)

major = tk.StringVar()
majorEntered = ttk.Entry(DatabaseGUI, width=20, textvariable=major)
majorEntered.grid(column=1, row=2)

sDate = tk.StringVar()
sDateEntered = ttk.Entry(DatabaseGUI, width=20, textvariable=sDate)
sDateEntered.grid(column=1, row=3)

'''Defining button to create person entry in DB'''
createPersonButton = tk.Button(DatabaseGUI, text='Add person', width=15, command=create_person_press).\
    grid(row=0, column=2)

'''Defining button to create student entry in DB'''
createStudentButton = tk.Button(DatabaseGUI, text='Add student', width=15, command=create_student_press).\
    grid(row=1, column=2)

'''Defining button to view all person entries in DB'''
viewPersonButton = tk.Button(DatabaseGUI, text='View person table', width=15, command=view_person_table).\
    grid(row=2, column=2)

'''Defining button to view all student entries in DB'''
viewStudentButton = tk.Button(DatabaseGUI, text='View student table', width=15, command=view_student_table).\
    grid(row=3, column=2)

'''Defining button to reset the database'''
resetDatabaseButton = tk.Button(DatabaseGUI, text='Reset', width=15, command=reset_press). \
    grid(row=4, column=6)

'''Defining button to exit program'''
exitButton = tk.Button(DatabaseGUI, text='Exit', width=15, command=DatabaseGUI.destroy).grid(row=4, column=1)

'''Loop to wait for input'''
DatabaseGUI.mainloop()


