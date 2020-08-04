import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from database_functions import (change_password, class_is_approved,
                                edit_profile, get_class_information_prof,
                                get_class_req_status_prof, get_classes_of_prof,
                                get_name_by_username, get_prof_edit_info,
                                get_random_quote, get_student_info,
                                get_students_of_class_id_prof,
                                insert_grade_for_student,
                                insert_new_class_to_approve)
from Ui_Classes.professors_ui_classes import (
    Ui_prof_class_request_page, Ui_prof_class_requsts_status_page,
    Ui_prof_main_page, Ui_prof_my_classes_page, Ui_prof_students_page,
    Ui_prof_submit_grades_page)
from Ui_Classes.same_ui_classes import (Ui_change_password_page,
                                        Ui_edit_profile_page)


class MyClasses(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """MyClasses constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_my_classes_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.prof_my_classes_tableWidget.setRowCount(0)
        self.ui.prof_my_classes_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        self.show_classes()

    def show_classes(self):
        """ Shows classes of professor"""
        prof_classes = get_classes_of_prof(self.username)
        prof_name = get_name_by_username(self.username)

        if prof_classes != "none":
            for row_num, each_class in enumerate(prof_classes):
                class_info = get_class_information_prof(prof_name, each_class)
                self.ui.prof_my_classes_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(class_info.keys()):
                    self.ui.prof_my_classes_tableWidget.setItem(row_num, col_num,
                                                                qtw.QTableWidgetItem(str(class_info[data])))


class ClassRequest(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ClassRequest constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_class_request_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.prof_class_request_request_button.clicked.connect(
            self.input_class_to_request)

    def input_class_to_request(self):
        """Takes the class name, schedule, credit and exam
            date and submits a new class request to dean."""

        input_class_name = self.ui.prof_class_request_name_lineEdit.text()
        input_class_credit = self.ui.prof_class_request_credit_lineEdit.text()
        input_class_sche = self.ui.prof_class_request_sche_lineEdit.text()
        input_class_exam = self.ui.prof_class_request_exam_lineEdit.text()
        prof_name = get_name_by_username(self.username)

        # Check if all are filled
        if input_class_name == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input a name for your class.")
        elif input_class_credit == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input a credit for your class.")
        elif not input_class_credit.isdecimal():
            qtw.QMessageBox.critical(
                self, "Note", "Credit should be a number.")
        elif input_class_sche == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input a schedule for your class.")
        elif input_class_exam == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input an exam date for your class.")
        else:
            res = class_is_approved(input_class_name, prof_name)
            # The request is new
            if res is None:
                insert_new_class_to_approve(input_class_name,
                                            prof_name,
                                            input_class_credit,
                                            input_class_sche,
                                            input_class_exam)

                msg = """Your {} class request has been submitted successfully.""".format(
                    input_class_name)
                qtw.QMessageBox.information(
                    self, "Done", msg)

            # The request already exists and not decided yet.
            elif res[0] == 0:
                msg = "Your request has been submitted before and it's pending."
                qtw.QMessageBox.critical(
                    self, "Prnding", msg)
            # The request already has been rejected.
            elif res[0] == 2:
                msg = "Your request has been submitted before and has been rejected."
                qtw.QMessageBox.critical(
                    self, "Rejected", msg)


class ClassReqStat(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ClassReqStat constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_class_requsts_status_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.prof_class_requsts_status_page_tableWidget.setRowCount(0)
        self.ui.prof_class_requsts_status_page_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        self.show_class_req()

    def show_class_req(self):
        """ Shows class requests of professor."""
        class_reqs = get_class_req_status_prof(self.username)

        for row_num, each_class_info in enumerate(class_reqs):
            self.ui.prof_class_requsts_status_page_tableWidget.insertRow(
                row_num)
            for col_num, data in enumerate(each_class_info.keys()):
                self.ui.prof_class_requsts_status_page_tableWidget.setItem(row_num, col_num,
                                                                           qtw.QTableWidgetItem(str(each_class_info[data])))


class ProfStudents(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_students_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.prof_students_show_button.clicked.connect(self.show_students)
        self.show_classes()

    def show_classes(self):
        """Shows professor's classes in combobox"""
        prof_classes = get_classes_of_prof(self.username)
        if prof_classes != "none":
            for each_class in prof_classes:
                self.ui.prof_students_class_name_comboBox.addItem(each_class)

    def show_students(self):
        """Shows professor's students from that class in table"""
        self.ui.prof_students_tableWidget.setRowCount(0)
        input_class_name = self.ui.prof_students_class_name_comboBox.currentText()
        if input_class_name != "":
            students_in_class = get_students_of_class_id_prof(
                self.username, input_class_name)
            if students_in_class != "none":
                for row_num, each_id in enumerate(students_in_class):
                    student_info = get_student_info(each_id)
                    del student_info["classes"]
                    del student_info["gpa"]
                    self.ui.prof_students_tableWidget.insertRow(row_num)
                    for col_num, data in enumerate(student_info.keys()):
                        self.ui.prof_students_tableWidget.setItem(row_num, col_num,
                                                                  qtw.QTableWidgetItem(str(student_info[data])))


class SubmitGrades(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """SubmitGrades constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_submit_grades_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.prof_submit_grades_submit_button.clicked.connect(
            self.submit_student_grade)
        self.ui.prof_submit_grades_class_name_comboBox.currentTextChanged.connect(
            self.show_students)
        self.show_classes()

    def show_classes(self):
        """Shows professor's classes in combobox"""
        prof_classes = get_classes_of_prof(self.username)
        if prof_classes != "none":
            for each_class in prof_classes:
                self.ui.prof_submit_grades_class_name_comboBox.addItem(
                    each_class)

    def show_students(self):
        """Shows professor's students from that class in combobox"""
        self.ui.prof_submit_grades_student_id_comboBox.clear()
        input_class_name = self.ui.prof_submit_grades_class_name_comboBox.currentText()
        students_in_class = get_students_of_class_id_prof(
            self.username, input_class_name)
        if students_in_class != "none":
            self.ui.prof_submit_grades_student_id_comboBox.addItems(
                students_in_class)

    def submit_student_grade(self):
        """Takes the student's ID, class and grade and adds the grade for that class."""
        input_class_name = self.ui.prof_submit_grades_class_name_comboBox.currentText()
        input_student_ID = self.ui.prof_submit_grades_student_id_comboBox.currentText()
        input_student_ID_index = self.ui.prof_submit_grades_student_id_comboBox.currentIndex()
        input_student_grade = self.ui.prof_submit_grades_grade_lineEdit.text()

        if input_student_grade == "":
            qtw.QMessageBox.critical(self, "Note", "Please input the grade")

        elif not input_student_grade.isdecimal():
            qtw.QMessageBox.critical(self, "Note", "Grade should be a number")

        elif input_student_ID == "":
            qtw.QMessageBox.critical(self, "Note", "Please choose a student")

        else:
            insert_grade_for_student(
                input_student_ID, input_class_name, input_student_grade)
            qtw.QMessageBox.information(self, "Done", "Grade %s for class %s was submitted for %s." % (
                input_student_grade, input_class_name, input_student_ID))
            self.ui.prof_submit_grades_student_id_comboBox.removeItem(
                input_student_ID_index)


class EditPro(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """EditPro constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_edit_profile_page()
        self.ui.setupUi(self)

        self.ui.edit_profile_button.accepted.connect(
            self.input_edit_profile_information)

        prof_info = get_prof_edit_info(username)
        default_name = prof_info[0]
        default_gender = prof_info[1]

        # Show student's default data
        self.ui.edit_profile_fullname_lineEdit.setText(default_name)
        self.ui.edit_profile_gender_comboBox.setCurrentIndex(default_gender)

        self.username = username

    def input_edit_profile_information(self):
        """Inputs the user's information to and updates the profile."""
        input_name = self.ui.edit_profile_fullname_lineEdit.text()
        input_gender = self.ui.edit_profile_gender_comboBox.currentIndex()
        edit_profile(self.username, input_name, input_gender)
        qtw.QMessageBox.information(
            self, "Done", "Your profile info has successfully changed.")


class ChangePass(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ReportCard constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_change_password_page()
        self.ui.setupUi(self)

        self.ui.change_pass_buttons.accepted.connect(
            self.input_username_password_passwordconfirm)

        self.username = username

    def input_username_password_passwordconfirm(self):
        """Inputs the user's username, password and password confirmation and changes the password"""
        input_password = self.ui.change_pass_password_lineEdit.text()
        input_passwordconfirm = self.ui.change_pass_passconfirm_lineEdit.text()

        # Check all are filled
        if input_password == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input your password.")
        elif input_passwordconfirm == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please confirm your password.")

        elif input_password != input_passwordconfirm:
            qtw.QMessageBox.critical(
                self, "Note", "Password and password confirmation doesn't match.")

        else:
            # Changes the password
            change_password(self.username, input_password)
            qtw.QMessageBox.information(
                self, "Done", "Your password has been successfully changed.")
            self.accept()


class ProfessorMainPage(qtw.QMainWindow):

    def __init__(self, username, *args, **kwargs):
        """ProfessorMainPage constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_prof_main_page()
        self.ui.setupUi(self)
        self.username = username

        # Set welcome label to users name
        self.ui.prof_main_page_name_label.setText(
            get_name_by_username(self.username))

        # Set random quote of the day label
        self.ui.prof_main_page_quote_body_label.setText(get_random_quote())
        self.ui.prof_main_page_quote_body_label.adjustSize()

        # Connects the menu actions to functions for corresponding QDialogs
        self.ui.prof_main_page_action_My_Classes.triggered.connect(
            self.open_my_classes_dialog)
        self.ui.prof_main_page__action_Class_Requests_Status.triggered.connect(
            self.open_class_request_status_dialog)
        self.ui.prof_main_page_action_New_Class_Requset.triggered.connect(
            self.open_class_request_dialog)
        self.ui.prof_main_page_action_Students.triggered.connect(
            self.open_students_dialog)
        self.ui.prof_main_page_action_Submit_Grades.triggered.connect(
            self.open_submit_grades_dialog)
        self.ui.prof_main_page_action_Edit_Profile.triggered.connect(
            self.open_edit_profile_dialog)
        self.ui.prof_main_page_action_Change_Password.triggered.connect(
            self.open_change_password_dialog)
        self.ui.prof_main_page_action_Sign_Out.triggered.connect(self.sign_out)

    #    self.show()

    # The following functions opens the QDialogs for Professor QMainWindow.
    def open_my_classes_dialog(self):
        """ Opens the My Classes page."""
        self.prof_my_classes_page = MyClasses(self.username)
        self.prof_my_classes_page.show()

    def open_class_request_dialog(self):
        """ Opens the New Class Request page."""
        self.prof_class_request_page = ClassRequest(self.username)
        self.prof_class_request_page.show()

    def open_class_request_status_dialog(self):
        """ Opens the Class Requests Status page."""
        self.prof_class_request_status_page = ClassReqStat(self.username)
        self.prof_class_request_status_page.show()

    def open_students_dialog(self):
        """ Opens the Students page."""
        self.prof_students_page = ProfStudents(self.username)
        self.prof_students_page.show()

    def open_submit_grades_dialog(self):
        """ Opens the Submit Grade page."""
        self.prof_submit_grades_page = SubmitGrades(self.username)
        self.prof_submit_grades_page.show()

    def open_edit_profile_dialog(self):
        """ Opens the Edit Profile page."""
        self.prof_edit_profile_page = EditPro(self.username)
        self.prof_edit_profile_page.show()

    def open_change_password_dialog(self):
        """ Opens the Change Password page."""
        self.prof_change_password_page = ChangePass(self.username)
        self.prof_change_password_page.show()

    def sign_out(self):
        """ Signs Out."""
        buttonReply = qtw.QMessageBox.question(
            self, "Note", "Are you sure you want to sign out?", qtw.QMessageBox.Yes, qtw.QMessageBox.No)
        if buttonReply == qtw.QMessageBox.Yes:
            self.exit = True
            self.close()
