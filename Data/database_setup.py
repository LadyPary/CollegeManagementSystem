import random
import sqlite3

from quotes import quotes

# Creating the database
# This file has been used to create the tabels in database
# Delete the existing database file before creating a new one


conn = sqlite3.connect('Modern_University.db')
c = conn.cursor()

# Creating the tables, Only needs to run the first time

# Table for quote of the day in main pages
c.execute("""CREATE TABLE quotes (
            quote_id integer,
            quote text
            )""")

# Table for students
# status ==> *0: student*, 1: professor, 2: dean
# gender ==> 0: male, 1: female
# classes is a dictionary in this format ==> "{"class" : grade}"
c.execute("""CREATE TABLE students (
            username integer,
            password text,
            name text,
            status integer,
            gender integer,
            field text,
            gpa real,
            classes text
            )""")

# Table for professors
# status ==> 0: student, *1: professor*, 2: dean
# gender ==> 0: male, 1: female
# classes is a list of professor's classes' names in string format
# score is a dictionary in this format ==> "{"class" : [each student score]}"
c.execute("""CREATE TABLE profs (
            username text,
            password text,
            name text,
            status integer,
            gender integer,
            score text,
            classes text
            )""")

# Table for dean of the faculty
# status ==> 0: student, 1: professor, *2: dean*
# gender ==> 0: male, 1: female
c.execute("""CREATE TABLE dean (
            username text,
            password text,
            name text,
            status integer,
            gender integer
            )""")

# Table for classes
# classstudents is a list with student ID's of students in that class.
c.execute("""CREATE TABLE classes (
            name text,
            professor text,
            classstudents text,
            credit integer,
            class_schedule text,
            exam_date text
            )""")

# Table for new students waiting for approval
# approval ==> 0: not decided yet, 1: approved, 2: rejected
c.execute("""CREATE TABLE studentapprove (
            username integer,
            password text,
            name text,
            gender integer,
            field text,
            approval integer
            )""")

# Table for new classes waiting for approval
# approval ==> 0: not decided yet, 1: approved, 2: rejected
c.execute("""CREATE TABLE classapprove (
            name text,
            professor text,
            credit integer,
            class_schedule text,
            exam_date text,
            approval integer
            )""")


# The following is for showing random quotes.
def add_all_quotes_to_database():
    """When called, Adds all the quote to the database."""
    for each_quote in quotes.items():
        with conn:
            c.execute("INSERT INTO quotes VALUES (:quote_id, :quote)",
                      {"quote_id": each_quote[0], "quote": each_quote[1]})


# Add all quotes to database, only needs to run once
add_all_quotes_to_database()


conn.close()
