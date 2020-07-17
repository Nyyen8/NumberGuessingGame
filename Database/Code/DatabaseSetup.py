"""
Program: DatabaseSetup.py
Author: Paul Elsea
Last Modified: 07/16/2020

Program to connect to a database and perform necessary functions.
"""

import sqlite3
from sqlite3 import Error

''''''
def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

''''''
def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

''''''
def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        per_id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    std_id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    start_date text NOT NULL,
                                    FOREIGN KEY (std_id) REFERENCES person (per_id)
                                );"""

    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

        ''''''

def drop_tables(database):
    sql_drop_person_table = """DROP TABLE person;"""

    sql_drop_student_table = """DROP TABLE student;"""

    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_drop_person_table)
        # create tasks table
        create_table(conn, sql_drop_student_table)
    else:
        print("Unable to connect to " + str(database))

''''''
def select_all_persons(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows

def find_person_id(conn, fName, lName):
    cur = conn.cursor()
    cur.execute("SELECT per_id FROM person WHERE firstname = (?) AND lastname = (?)", (fName, lName))

    return cur.fetchone()

''''''
def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows

''''''
def create_person(conn, person):
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id

''''''
def create_student(conn, student):
    sql = ''' INSERT INTO student(std_id, major, start_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id


if __name__ == '__main__':
    pass