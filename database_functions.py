import random
import sqlite3
import ast

# This file contains all the functions used
# in the app for communicate with the database.


# The two following functions are used to store a dictionary
# or a list as a text-type data in databese.
def convert_str_to_othertype(string):
    """
    Takes a dictionary or a list in the string format, 
    returns it in the correct format. 
    correct input for dict: "{'a' : 1}" 
    correct input for list: "['a', 'b']"
    """
    res_othertype = ast.literal_eval(string)
    return res_othertype


def convert_othertype_to_str(othertype):
    """ 
    Takes a dictionary or a list in the correct format, 
    returns it in the string format.
    """
    res_str = str(othertype)
    return res_str


def insert_user(username, password, fullname, gender, status, field=None):
    """ 
    Adds a student, professor or a dean's information to the database
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    with conn:
        if status == 0:
            c.execute("""INSERT INTO studentapprove 
                        VALUES (:username, :password, 
                                :name, :gender, :field, 
                                :approval)""",
                      {"username": username,
                       "password": password,
                       "name": fullname, "gender": gender,
                       "field": field, "approval": 0})

        elif status == 1:
            c.execute("""INSERT INTO profs 
                        VALUES (:username, :password, 
                                :name, :status, :gender,
                                :score, :classes)""",
                      {"username": username,
                       "password": password,
                       "name": fullname,
                       "status": 1, "gender": gender,
                       "score": "none",
                       "classes": "none"})

        elif status == 2:
            c.execute("""INSERT INTO dean
                        VALUES (:username, :password,  
                                :name, :status, :gender)""",
                      {"username": username,
                       "password": password,
                       "name": fullname, "status": 2,
                       "gender": gender})
    conn.close()


def insert_new_class_to_approve(new_class, professor, credit, class_schedule, exam_date):
    """ 
    Takes a class name, professor name, class credit,
    class schedule and exam date and adds a new class
    to the database for dean to approve
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    with conn:
        c.execute("""INSERT INTO classapprove 
                    VALUES (:name, :professor, 
                            :credit, :class_schedule, 
                            :exam_date, :approval)""",
                  {"name": new_class, "professor": professor,
                   "credit": credit, "class_schedule": class_schedule,
                   "exam_date": exam_date, "approval": 0})
    conn.close()


def insert_class_for_student(username, new_class, professor):
    """
    Takes student's username, new class name and professor 
    name then adds a new class for student to the database
    and also updates the students of that class.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    # Add the new class to classes of student
    c.execute("""SELECT classes 
                FROM students  
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()[0]
    if res == "none":
        student_classes = {new_class: "none"}
    else:
        student_classes = convert_str_to_othertype(res)
        student_classes[new_class] = "none"
    student_classes = convert_othertype_to_str(student_classes)
    with conn:
        c.execute("""UPDATE students 
                    SET classes = :classes
                    WHERE username = :username """,
                  {"username": username,
                   "classes": student_classes})

    # Add the student to the students of new class
    c.execute("""SELECT classstudents
                FROM classes WHERE name = :name 
                AND professor= :professor """,
              {"name": new_class,
               "professor": professor})

    res = c.fetchone()[0]
    if res == "none":
        students_of_class = [username]
    else:
        students_of_class = convert_str_to_othertype(res)
        students_of_class.append(username)
    students_of_class = convert_othertype_to_str(students_of_class)
    with conn:
        c.execute("""UPDATE classes
                    SET classstudents = :classstudents 
                    WHERE name = :name 
                    AND professor= :professor""",
                  {"classstudents": students_of_class,
                   "name": new_class, "professor": professor})
    conn.close()


def insert_score_for_prof(name, class_name, score):
    """ 
    Takes a professor's name, class name and score,
    then adds the score for that class.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    c.execute("""SELECT score
                FROM profs 
                WHERE name = :name""",
              {"name": name})

    res = c.fetchone()[0]
    if res == "none":
        prof_score = {class_name: [score]}
    else:
        prof_score = convert_str_to_othertype(res)
        if class_name in prof_score.keys():
            prof_score[class_name].append(score)
        elif class_name not in prof_score.keys():
            prof_score[class_name] = [score]

    str_prof_score = convert_othertype_to_str(prof_score)

    with conn:
        c.execute("""UPDATE profs 
                    SET score = :score 
                    WHERE name = :name """,
                  {"name": name,
                   "score": str_prof_score})

    conn.close()


def insert_grade_for_student(student_ID, class_name, grade):
    """
    Takes the student's ID, class and grade and 
    adds the grade for that class.
    """
    classes = get_classes_of_student(student_ID)
    if classes == "none":
        return "none"
    else:
        classes[class_name] = grade
        new_classes = convert_othertype_to_str(classes)

        conn = sqlite3.connect('Modern_University.db')
        c = conn.cursor()

        with conn:
            c.execute("""UPDATE students
                        SET classes = :classes
                        WHERE username = :username """,
                      {"username": student_ID,
                       "classes": new_classes})

        conn.close()


def get_random_quote():
    """ Gets a random quote from quotes table in database."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    quote_id = random.randint(1, 36)
    c.execute("""SELECT quote 
                FROM quotes 
                WHERE quote_id = :quote_id""",
              {"quote_id": quote_id})
    res = c.fetchone()[0]
    conn.close()
    return res


def get_password_by_username(username):
    """
    Takes a username and returns its password.
    if user doesn't exists returns None.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT password
                FROM (
                SELECT username, password FROM students 
                UNION ALL
                SELECT username, password FROM profs
                UNION ALL
                SELECT username, password FROM dean
                )
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()
    conn.close()
    if res is None:
        return res
    else:
        return res[0]


def get_name_by_username(username):
    """Takes a username, returns the name for that user."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name
                FROM (
                SELECT username, name FROM students 
                UNION ALL
                SELECT username, name FROM profs
                UNION ALL
                SELECT username, name FROM dean
                )
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()[0]
    conn.close()
    return res


def get_username_by_name(name):
    """ Takes the name of the person, returns its username"""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT username
                FROM (
                SELECT username, name FROM students 
                UNION ALL
                SELECT username, name FROM profs
                UNION ALL
                SELECT username, name FROM dean
                )
                WHERE name = :name""",
              {"name": name})
    res = c.fetchone()[0]
    conn.close()
    return res


def get_status_by_username(username):
    """ Takes the username of the person, returns its status"""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT status
                FROM (
                SELECT username, status FROM students 
                UNION ALL
                SELECT username, status FROM profs
                UNION ALL
                SELECT username, status FROM dean
                )
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()[0]
    conn.close()
    return res


def get_classes_of_student(username):
    """
    Takes a username, returns students classes dictionary
    with this format ==> "{"class" : grade}"
    returns "none" if there are no classes. 
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT classes 
                FROM students 
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()[0]
    conn.close()
    if res != "none":
        student_classes = convert_str_to_othertype(res)
        return student_classes
    else:
        return "none"


def get_all_classes():
    """
    When called, returns a list of tuples like:
    [(name, credit, professor, students,
    schedule, exam date)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT *
                FROM classes""")

    all_classes = c.fetchall()
    conn.close()

    if all_classes == []:
        return "none"
    else:
        return all_classes


def get_all_profs():
    """
    When called, returns a list of tuples like:
    [(professor, classes)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, classes
                FROM profs""")
    list_of_profs = c.fetchall()
    conn.close()
    if list_of_profs == None:
        return "none"
    else:
        return list_of_profs


def get_all_students():
    """
    When called, returns a list of tuples like:
    [(student ID, name, field, classes)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT username, name,
                        field, classes
                FROM students""")

    list_of_students = c.fetchall()
    conn.close()

    if list_of_students == None:
        return "none"
    else:
        return list_of_students


def get_top_students():
    """
    When called, returns a list of tuples of 
    top students' information in decreasing 
    order of gpa. like:[(Student ID, name, GPA)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT username, 
                        name,gpa
                FROM students
                WHERE gpa != "none"
                ORDER BY gpa DESC""")

    list_of_top_students = c.fetchall()
    conn.close()

    if list_of_top_students == None:
        return "none"
    else:
        return list_of_top_students


def get_top_profs():
    """
    When called, returns a list of tuples of 
    top professors' information.
    like:[(score, name, class)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    c.execute("""SELECT username, name,
                        classes
                FROM profs""")

    list_of_top_profs = c.fetchall()
    conn.close()
    if list_of_top_profs == None:
        return "none"

    else:
        res_list = []
        for each_prof in list_of_top_profs:
            username = each_prof[0]
            name = each_prof[1]
            classes = each_prof[2]
            # Professor has classes
            if classes != "none":
                prof_classes = convert_str_to_othertype(classes)
                for each_class_name in prof_classes:
                    score = get_class_score_prof(username, each_class_name)
                    if (score != "none") and (score != None):
                        prof_info = (score, name, each_class_name)
                        res_list.append(prof_info)
    if res_list == []:
        return "none"
    else:
        return res_list


def get_class_information_student(username, class_name):
    """
    Takes a student's username and class name,
    returns the dictionari information for that 
    class for student.
    like: {
            "name": 
            "credit": 
            "professor":
            "class_schedule": 
            "exam_date":
                }
    returns "none" if None if found.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT *
                FROM classes WHERE name = :name""",
              {"name": class_name})

    all_class_info = c.fetchall()
    conn.close()

    if all_class_info == None:
        return "none"

    else:
        for each_class in all_class_info:
            students_in_class = convert_str_to_othertype(each_class[2])
            if str(username) in students_in_class:
                res = {
                    "name": class_name,
                    "credit": each_class[3],
                    "professor": each_class[1],
                    "class_schedule": each_class[4],
                    "exam_date": each_class[5]
                }
                if res != None:
                    return res


def get_class_information_prof(professor, class_name):
    """
    Takes a professors name and a class name,
    returns a dictionary of class information.
    {'name':, 'credit':, 'class_schedule':, 
    'exam_date':, 'num_of_students':}
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    c.execute("""SELECT *
                FROM classes
                WHERE name = :name
                AND professor = :professor """,
              {"name": class_name,
               "professor": professor})

    class_info = c.fetchone()
    conn.close()

    if class_info == None:
        return "none"
    else:
        # No students in class
        if class_info[2] == "none":
            class_num = 0
        else:
            class_num = len(convert_str_to_othertype(class_info[2]))
        res = {
            "name": class_name,
            "credit": class_info[3],
            "num_of_students": class_num,
            "class_schedule": class_info[4],
            "exam_date": class_info[5]
        }
    return res


def get_class_req_status_prof(username):
    """
    Takes a professor's username, returns their 
    class requests as a list of dictionaries.
    Like: [{
            "status":
            "name":
            "credit":
            "class_schedule":
            "exam_date":
            }]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    prof_name = get_name_by_username(username)
    c.execute("""SELECT *
                FROM classapprove
                WHERE professor = :professor""",
              {"professor": prof_name})

    all_class_info = c.fetchall()

    class_requests = []

    if all_class_info is not None:
        for each_class in all_class_info:
            if each_class[5] == 0:
                status = "Not decided yet"
            else:
                status = "Rejected"

            res = {
                "status": status,
                "name": each_class[0],
                "credit": each_class[2],
                "class_schedule": each_class[3],
                "exam_date": each_class[4]
            }
            class_requests.append(res)
    conn.close()
    return class_requests


def get_class_for_enroll(username):
    """
    Takes a username, Returns all the classes information
    that the student is not already enrolled in as a list 
    of dictionaries.
    Like:[{
            "name": 
            "credit": 
            "professor": 
            "class_schedule":
            "exam_date": 
            }]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    student_classes = get_classes_of_student(username)
    if student_classes != "none":
        student_classes = get_classes_of_student(username).keys()
    else:
        student_classes = []
    c.execute("""SELECT * FROM classes""")

    classes = c.fetchall()
    availabe_classes = []
    for each_class in classes:
        if each_class[0] not in student_classes:
            res = {
                "name": each_class[0],
                "credit": each_class[3],
                "professor": each_class[1],
                "class_schedule": each_class[4],
                "exam_date": each_class[5]
            }
            availabe_classes.append(res)
    conn.close()

    return availabe_classes


def get_gpa_of_student(username):
    """Calculates the GPA for that student and adds it to the database."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT classes
                FROM students
                WHERE username = :username""",
              {"username": username})

    res = c.fetchone()[0]

    if res == "none":
        conn.close()
        return "none"

    student_classes = convert_str_to_othertype(res)

    grades_count = 0
    credit_count = 0

    for each_class in student_classes.items():
        c.execute("""SELECT credit FROM classes WHERE name = :name""",
                  {"name": each_class[0]})
        credit_temp = c.fetchone()[0]
        if each_class[1] != "none":
            grades_count += int(each_class[1]) * int(credit_temp)
            credit_count += int(credit_temp)

    if credit_count != 0:
        gpa = round(grades_count / credit_count, 2)
        with conn:
            c.execute("""UPDATE students SET gpa = :gpa
                    WHERE username = :username""",
                      {"gpa": gpa, "username": username})
        conn.close()
        return gpa


def get_class_score_prof(username, class_name):
    """
    Takes a professor's username and one of their classes,
    returns the professor's score for that class.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    with conn:
        c.execute("""SELECT score
                    FROM profs
                    WHERE username = :username""",
                  {"username": username})
    scores = c.fetchone()[0]
    conn.close()
    if scores == "none":
        return "none"

    else:
        scores = convert_str_to_othertype(scores)
        if class_name in scores.keys():
            if scores[class_name] == []:
                return "none"
            else:
                class_score = sum(scores[class_name]) / len(scores[class_name])
                return class_score


def get_all_student_classes_one_prof(username, professor):
    """ 
    Takes a username and professor, returns all the
    classes which the student has with that professor.
    """
    classes = get_classes_of_student(username)
    if classes == "none":
        return "none"
    else:
        profs = []
        for each_class in classes:
            class_info = get_class_information_student(username, each_class)
            if class_info["professor"] == professor:
                profs.append(class_info["name"])

        return profs


def get_student_edit_info(username):
    """ Takes a username, returns students fullname, gender and field."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, gender, field 
                FROM students 
                WHERE username = :username""",
              {"username": username})

    res = c.fetchone()
    conn.close()

    return res


def get_prof_edit_info(username):
    """ Takes a username, returns professor's fullname and gender."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, gender
                FROM profs 
                WHERE username = :username""",
              {"username": username})

    res = c.fetchone()
    conn.close()

    return res


def get_dean_edit_info(username):
    """ Takes a username, returns dean's fullname and gender."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, gender
                FROM dean 
                WHERE username = :username""",
              {"username": username})

    res = c.fetchone()
    conn.close()

    return res


def get_classes_of_prof(username):
    """
    Takes a username, returns a list of professors's classes. 
    returns "none" if there are no classes.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    c.execute("""SELECT classes
                FROM profs
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()[0]
    conn.close()
    if res != "none":
        profs_classes = convert_str_to_othertype(res)
        return profs_classes
    else:
        return "none"


def get_students_of_class_id_prof(username, class_name):
    """
    Takes a professors username and a class name, returns student IDs,
    names and fields of all students in their class.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()

    professor = get_name_by_username(username)

    c.execute("""SELECT classstudents    
                FROM classes 
                WHERE name = :name
                AND professor = :professor""",
              {"name": class_name,
               "professor": professor})

    students = c.fetchone()[0]
    conn.close()

    if students != "none":
        students = convert_str_to_othertype(students)
        return students
    else:
        return "none"


def get_student_info(username):
    """
    Takes a student ID, returns a dictionary of its information.
    {"id":, "name":, "field":, "gpa":, "classes":}
    """

    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, field, gpa, classes
                FROM students
                WHERE username = :username""",
              {"username": username})

    student_info = c.fetchone()
    conn.close()

    if student_info == None:
        return "none"

    else:
        res = {
            "id": username,
            "name": student_info[0],
            "field": student_info[1],
            "gpa": student_info[2],
            "classes": student_info[3],
        }
        return res


def get_students_info_for_approval():
    """
    When called, returns a list of tuples 
    like:[(student ID, name, field)]
    """

    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT username, name,
                        field
                FROM studentapprove
                WHERE approval != 2""")

    list_of_students = c.fetchall()
    conn.close()

    if list_of_students == []:
        return "none"
    else:
        return list_of_students


def get_class_info_for_approval():
    """
    When called, returns a list of tuples 
    like:[(name, professor, credit, schedule, exam date)]
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT name, professor, 
                        credit, class_schedule, 
                        exam_date
                FROM classapprove
                WHERE approval != 2""")

    list_of_classes = c.fetchall()
    conn.close()

    if list_of_classes == []:
        return "none"
    else:
        return list_of_classes


def check_user_exists(username):
    """ Takes a username, returns True if it exists False otherwise."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT username
                FROM (
                SELECT username FROM students 
                UNION ALL
                SELECT username FROM profs
                UNION ALL
                SELECT username FROM dean
                )
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()
    conn.close()
    if res is None:
        return False
    else:
        return True


def check_password_signin(username, password):
    """ Takes a username and a password and checks if it's correct. """
    user_password = get_password_by_username(username)
    if user_password is None:
        return None
    else:
        if user_password == password:
            return True
        else:
            return False


def change_password(username, new_password):
    """ Changes the password of the user in database"""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    status = get_status_by_username(username)
    with conn:
        if status == 0:
            c.execute("""UPDATE students 
                        SET password = :password
                        WHERE username = :username""",
                      {"password": new_password,
                       "username": username})

        elif status == 1:
            c.execute("""UPDATE profs 
                        SET password = :password
                        WHERE username = :username""",
                      {"password": new_password,
                       "username": username})

        elif status == 2:
            c.execute("""UPDATE dean 
                        SET password = :password
                        WHERE username = :username""",
                      {"password": new_password,
                       "username": username})
    conn.close()


def edit_profile(username, new_name, new_gender, new_field=None):
    """Edits user's profile info"""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    status = get_status_by_username(username)
    with conn:
        if status == 0:
            c.execute("""UPDATE students
                        SET name = :name,
                            gender = :gender, 
                            field = :field
                        WHERE 
                            username = :username""",
                      {"username": username, "name": new_name,
                       "gender": new_gender, "field": new_field})

        elif status == 1:
            old_name = get_name_by_username(username)

            c.execute("""UPDATE classes
                        SET professor = :new_professor
                        WHERE 
                            professor = :old_professor""",
                      {"old_professor": old_name,
                       "new_professor": new_name})

            c.execute("""UPDATE classapprove
                        SET professor = :new_professor
                        WHERE 
                            professor = :old_professor""",
                      {"old_professor": old_name,
                       "new_professor": new_name})

            c.execute("""UPDATE profs
                        SET name = :name,
                            gender = :gender
                        WHERE 
                            username = :username""",
                      {"username": username,
                       "name": new_name,
                       "gender": new_gender})

        elif status == 2:
            c.execute("""UPDATE dean
                        SET name = :name,
                            gender = :gender
                        WHERE 
                            username = :username""",
                      {"username": username, "name": new_name,
                       "gender": new_gender})

    conn.close()


def student_approve_or_reject(username, approval):
    """ 
    Updates the approval situation of student, 
    If accepted adds it to database.
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    if approval == 1:
        # Student is Approved
        with conn:
            c.execute("""SELECT * 
                        FROM studentapprove 
                        WHERE username = :username""",
                      {"username": username})

            student_info = c.fetchone()
            username = student_info[0]
            password = student_info[1]
            fullname = student_info[2]
            gender = student_info[3]
            field = student_info[4]

            # Add student to database
            c.execute("""INSERT INTO students 
                        VALUES (:username, :password,
                                :name, :status, :gender,
                                :field, :gpa, :classes)""",
                      {"username": username, "password": password,
                       "name": fullname, "status": 0, "gender": gender,
                       "field": field, "gpa": "none", "classes": "none",
                       "approval": "none"})

            # Delete student from approval table
            c.execute("""DELETE FROM studentapprove
                        WHERE username = :username""",
                      {"username": username})

    if approval == 2:
        # Student is Rejected
        with conn:
            c.execute("""UPDATE studentapprove
                        SET approval = :approval
                        WHERE username = :username""",
                      {"approval": 2, "username": username})
    conn.close()


def student_is_approved(username):
    """ Takes a username, returns student's approval situation"""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT approval 
                FROM studentapprove
                WHERE username = :username""",
              {"username": username})
    res = c.fetchone()
    conn.close()
    return res


def class_approve_or_reject(name, professor, approval):
    """ Updates the approval situation of class."""
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    if approval == 1:
        # Class is Approved
        with conn:
            c.execute("""SELECT * FROM classapprove
                        WHERE name = :name
                        AND professor = :professor""",
                      {"name": name, "professor": professor})
            class_info = c.fetchone()
            name = class_info[0]
            professor = class_info[1]
            credit = class_info[2]
            class_schedule = class_info[3]
            exam_date = class_info[4]

            # Add Class to classes table
            c.execute("""INSERT INTO classes
                        VALUES (:name, :professor,
                                :classstudents, :credit, 
                                :class_schedule, :exam_date)""",
                      {"name": name, "professor": professor,
                       "classstudents": "none", "credit": credit,
                       "class_schedule": class_schedule,
                       "exam_date": exam_date})

            # Add Class to professor's classes
            c.execute("""SELECT classes 
                        FROM profs 
                        WHERE name = :name""",
                      {"name": professor})
            classes = c.fetchone()[0]
            if classes == "none":
                classes = [name]
            else:
                classes = convert_str_to_othertype(classes)
                classes.append(name)
            classes = convert_othertype_to_str(classes)
            c.execute("""UPDATE profs 
                        SET classes = :classes 
                        WHERE name = :name""",
                      {"classes": classes, "name": professor})

            # Delete Class from approval table
            c.execute("""DELETE FROM classapprove 
                        WHERE name = :name 
                        AND professor = :professor""",
                      {"name": name, "professor": professor})

    if approval == 2:
        # Class is Rejected
        with conn:
            c.execute("""UPDATE classapprove 
                        SET approval = :approval
                        WHERE name = :name 
                        AND professor = :professor""",
                      {"approval": 2, "name": name,
                       "professor": professor})
    conn.close()


def class_is_approved(name, professor):
    """ 
    Takes a class' name and professor,
    returns its approval situation
    """
    conn = sqlite3.connect('Modern_University.db')
    c = conn.cursor()
    c.execute("""SELECT approval 
                FROM classapprove
                WHERE name = :name
                AND professor = :professor""",
              {"name": name, "professor": professor})
    res = c.fetchone()
    conn.close()
    return res
