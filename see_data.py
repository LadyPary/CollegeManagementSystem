import sqlite3
import random

# This file prints all the information form database.

# Creating the database
conn = sqlite3.connect('Modern_University.db')
c = conn.cursor()


print("students")
c.execute("""SELECT * FROM students""")
res1 = c.fetchall()
for each in res1:
    print(each)

print("-----")

print("profs")
c.execute("""SELECT * FROM profs""")
res2 = c.fetchall()
for each in res2:
    print(each)

print("-----")

print("dean")
c.execute("""SELECT * FROM dean""")
res3 = c.fetchall()
for each in res3:
    print(each)

print("-----")

print("classes")
c.execute("""SELECT * FROM classes""")
res4 = c.fetchall()
for each in res4:
    print(each)

print("-----")

print("studentapprove")
c.execute("""SELECT * FROM studentapprove""")
res5 = c.fetchall()
for each in res5:
    print(each)


print("-----")

print("classapprove")
c.execute("""SELECT * FROM classapprove""")
res6 = c.fetchall()
for each in res6:
    print(each)

print("-----")
