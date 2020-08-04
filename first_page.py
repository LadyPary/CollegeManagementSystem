import sys

from jdatetime import datetime
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from database_functions import (check_password_signin, check_user_exists,
                                get_password_by_username,
                                get_status_by_username, insert_user,
                                student_is_approved)
from dean_main_page import DeanMainPage
from professor_main_page import ProfessorMainPage
from student_main_page import StudentMainPage
from Ui_Classes.same_ui_classes import (Ui_first_page, Ui_signin_page,
                                        Ui_signup_page)


class SignIn(qtw.QDialog):

    def __init__(self, *args, **kwargs):
        """SignIn constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_signin_page()
        self.ui.setupUi(self)

        # Connects the function that inputs data for sign in to the OK button.
        self.ui.signin_buttons.accepted.connect(self.sign_in_authenticate)

    def sign_in_authenticate(self):
        """Inputs the user's username and password for sign in process and checks validations"""
        input_username = self.ui.signin_username_lineEdit.text()
        input_password = self.ui.signin_password_lineEdit.text()

        # Check if both are filled
        if input_username == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input your username.")

        elif input_password == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input your password.")
        else:
            # Student is waiting for approval
            student_approval = student_is_approved(input_username)
            if student_approval is not None:
                # Dean has not approved the student yet.
                if student_approval[0] == 0:
                    qtw.QMessageBox.critical(
                        self, "Pending", "Your student approval is pending.")
                # Dean has rejected the student.
                elif student_approval[0] == 2:
                    qtw.QMessageBox.critical(
                        self, "Rejected", "Your approval has been rejected.")
            else:
                res = check_password_signin(input_username, input_password)
                # User does not exist:
                if res is None:
                    qtw.QMessageBox.critical(
                        self, "Failed", "You have to sign up first.")

                # Password is wrong :
                elif not res:
                    qtw.QMessageBox.critical(
                        self, "Failed", "Password is incorrect.")
                else:
                    # Password and Username match.
                    # Goes to main page
                    status = get_status_by_username(input_username)
                    self.accept()
                    self.open_main_page(input_username, status)

    def open_main_page(self, username, status):
        """ Opens the main page after sign in"""
        if status == 0:
            self.student_main_page = StudentMainPage(username)
            self.student_main_page.show()

        elif status == 1:
            self.prof_main_page = ProfessorMainPage(username)
            self.prof_main_page.show()

        elif status == 2:
            self.dean_main_page = DeanMainPage(username)
            self.dean_main_page.show()


class SignUp(qtw.QDialog):

    def __init__(self, *args, **kwargs):
        """SignUp constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_signup_page()
        self.ui.setupUi(self)

        # Connects the function that inputs data for sign up to the OK button.
        self.ui.signup_buttons.accepted.connect(self.sign_up_submit)

    def sign_up_submit(self):
        """Inputs the user's information for sign up process and checks validations."""
        input_username = self.ui.signup_username_lineEdit.text()
        input_password = self.ui.signup_password_lineEdit.text()
        input_passwordconfirm = self.ui.signup_passconfirm_lineEdit.text()
        input_name = self.ui.signup_fullname_lineEdit.text()
        input_gender = self.ui.signup_gender_comboBox.currentIndex()
        input_status = self.ui.signup_status_comboBox.currentIndex()
        input_field = self.ui.signup_field_lineEdit.text()

        # Check if all are filled
        if input_username == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input your username.")
        elif input_password == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please input your password.")
        elif input_passwordconfirm == "":
            qtw.QMessageBox.critical(
                self, "Note", "Please confirm your password.")
        elif input_name == "":
            qtw.QMessageBox.critical(self, "Note", "Please input your name.")
        elif input_status == 0 and input_field == "":
            qtw.QMessageBox.critical(self, "Note", "Please input your field.")

        # Check if student ID has correct format
        elif input_status == 0 and not input_username.isdecimal():
            qtw.QMessageBox.critical(
                self, "Note", "Student ID should consist of numbers only.")
        elif input_status == 0 and len(input_username) != 9:
            qtw.QMessageBox.critical(
                self, "Note", "Student ID is not correct.")

         # Check if dean or professor's username has @ in it.
        elif (input_status != 0) and ("@" not in input_username):
            qtw.QMessageBox.critical(
                self, "Note", "Username should be your email.")

        # Check if password and its confirmation match
        elif input_password != input_passwordconfirm:
            qtw.QMessageBox.critical(
                self, "Note", "Password and password confirmation doesn't match")

        # Check if user already exist
        elif check_user_exists(input_username):
            qtw.QMessageBox.critical(
                self, "Note", "User with this username already exists.")

        else:
            student_approval = student_is_approved(input_username)
            # Student is waiting for approval
            if student_approval is not None:
                # Dean has not approved the student yet.
                if student_approval[0] == 0:
                    qtw.QMessageBox.critical(
                        self, "Pending", "Your student approval is pending. Cannot sign up again.")
                # Dean has rejected the student.
                elif student_approval[0] == 2:
                    qtw.QMessageBox.critical(
                        self, "Rejected", "Your approval has been rejected. Cannot sign up again.")
            else:
                if input_status != 0:
                    input_field == None
                # Add new user to database
                insert_user(input_username, input_password, input_name,
                            input_gender, input_status, input_field)
                qtw.QMessageBox.information(
                    self, "Done", "The SignUp process was successful.")
                self.close()


class FirstPage(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        """FirstPage constructor."""
        super().__init__(*args, **kwargs)

        self.ui = Ui_first_page()
        self.ui.setupUi(self)

        # Connecting the buttons to open Sign in and Sign out pages
        self.ui.first_page_sign_in_button.clicked.connect(
            self.open_sign_in_page)
        self.ui.first_page_sign_up_button.clicked.connect(
            self.open_sign_up_page)

        # Set the date and time label to show the current date and time
        t1 = datetime.now()
        date_and_time = "<%s %s %s> - <%s:%s %s>." % (t1.day, t1.strftime("%B"),
                                                      t1.year, t1.strftime(
                                                          "%I"),
                                                      t1.minute, t1.strftime("%p"))
        self.ui.first_page_date_and_time_Label.setText(date_and_time)
        self.ui.layoutWidget.adjustSize()

        self.show()

    def open_sign_in_page(self):
        self.sigin = SignIn()
        self.sigin.show()

    def open_sign_up_page(self):
        self.signup = SignUp()
        self.signup.show()
