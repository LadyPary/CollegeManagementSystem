import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from database_functions import (change_password, edit_profile,
                                get_all_student_classes_one_prof,
                                get_class_for_enroll,
                                get_class_information_student,
                                get_classes_of_student, get_gpa_of_student,
                                get_name_by_username, get_random_quote,
                                get_student_edit_info,
                                insert_class_for_student,
                                insert_score_for_prof)
from Ui_Classes.same_ui_classes import Ui_change_password_page
from Ui_Classes.student_ui_classes import (Ui_student_class_enroll_page,
                                           Ui_student_edit_profile_page,
                                           Ui_student_exam_schedule_page,
                                           Ui_student_instru_eval_page,
                                           Ui_student_main_page,
                                           Ui_student_my_courses_page,
                                           Ui_student_report_card_page)


class MyCourses(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """MyCourses constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_my_courses_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.student_my_courses_tableWidget.setRowCount(0)
        self.ui.student_my_courses_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        self.show_courses()

    def show_courses(self):
        """ Shows courses of student"""
        student_classes = get_classes_of_student(self.username)
        if student_classes != "none":
            for row_num, each_class in enumerate(student_classes.keys()):
                class_info = get_class_information_student(
                    self.username, each_class)
                if class_info != "none":
                    self.ui.student_my_courses_tableWidget.insertRow(row_num)
                    for col_num, data in enumerate(class_info.keys()):
                        self.ui.student_my_courses_tableWidget.setItem(row_num, col_num,
                                                                       qtw.QTableWidgetItem(str(class_info[data])))


class ExamSchedule(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ExamSchedule constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_exam_schedule_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.student_exam_schedule_tableWidget.setRowCount(0)
        self.ui.student_exam_schedule_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        self.show_exams()

    def show_exams(self):
        """ Shows courses and exam dates of student"""
        student_classes = get_classes_of_student(self.username)
        if student_classes != "none":
            for row_num, each_class in enumerate(student_classes.keys()):
                class_info = get_class_information_student(
                    self.username, each_class)
                del class_info["class_schedule"]
                self.ui.student_exam_schedule_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(class_info.keys()):
                    self.ui.student_exam_schedule_tableWidget.setItem(row_num, col_num,
                                                                      qtw.QTableWidgetItem(str(class_info[data])))


class ClassEnroll(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ClassEnroll constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_class_enroll_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.student_class_enroll_tableWidget.setRowCount(0)
        self.ui.student_class_enroll_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        self.show_class_enroll()

        # When double clicked on a row, will signal choose_class function
        self.ui.student_class_enroll_tableWidget.itemDoubleClicked.connect(
            self.choose_class)

    def show_class_enroll(self):
        """ Shows classes for student to enroll"""
        available_classes = get_class_for_enroll(self.username)
        if available_classes != "none":
            for row_num, each_class_info in enumerate(available_classes):
                self.ui.student_class_enroll_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_class_info.keys()):
                    self.ui.student_class_enroll_tableWidget.setItem(row_num, col_num,
                                                                     qtw.QTableWidgetItem(str(each_class_info[data])))

    def choose_class(self):
        """ Enroll when double clicked on the class."""
        selected_class = self.ui.student_class_enroll_tableWidget.selectedItems()
        selected_class_index = self.ui.student_class_enroll_tableWidget.selectedIndexes()
        selected_class_index_row = selected_class_index[0].row()
        class_to_enroll = []
        for each_item in selected_class:
            class_to_enroll.append(each_item.text())
        insert_class_for_student(
            self.username, class_to_enroll[0], class_to_enroll[2])
        self.ui.student_class_enroll_tableWidget.removeRow(
            selected_class_index_row)
        qtw.QMessageBox.information(
            self, "Done", "{} successfully added to your classes.".format(class_to_enroll[0]))

        self.close()


class ReportCard(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ReportCard constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_report_card_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.student_report_card_tableWidget.setRowCount(0)
        self.ui.student_report_card_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        gpa = get_gpa_of_student(self.username)

        self.ui.student_report_card_gpa_label.setText("GPA = " + str(gpa))
        self.ui.student_report_card_gpa_label.adjustSize()

        self.show_report()

    def show_report(self):
        """ Shows student's report card"""
        student_classes = get_classes_of_student(self.username)
        if student_classes != 'none':
            for row_num, each_class in enumerate(student_classes.keys()):
                class_info = get_class_information_student(
                    self.username, each_class)
                del class_info["class_schedule"]
                del class_info["exam_date"]
                class_info["grade"] = student_classes[each_class]
                self.ui.student_report_card_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(class_info.keys()):
                    self.ui.student_report_card_tableWidget.setItem(row_num, col_num,
                                                                    qtw.QTableWidgetItem(str(class_info[data])))


class InstruEval(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ReportCard constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_instru_eval_page()
        self.ui.setupUi(self)

        self.username = username
        self.ui.student_instru_eval_add_button.clicked.connect(
            self.input_instru_result)
        self.show_instu_info()

    def show_instu_info(self):
        """Shows the names of student's professors in combobox"""
        student_classes = get_classes_of_student(self.username)
        if student_classes != "none":
            added_profs = []
            for each_class in student_classes:
                class_info = get_class_information_student(
                    self.username, each_class)
                if class_info["professor"] not in added_profs:
                    self.ui.student_instru_eval_name_comboBox.addItem(
                        class_info["professor"])
                    added_profs.append(class_info["professor"])
            self.ui.student_instru_eval_name_comboBox.currentIndexChanged.connect(
                lambda: self.show_classes(self.ui.student_instru_eval_name_comboBox.currentText()))

    def show_classes(self, professor):
        """Shows the classes of the professor in combobox"""
        self.ui.student_instru_eval_class_comboBox.clear()
        all_classes = get_all_student_classes_one_prof(
            self.username, professor)
        if all_classes != "none":
            self.ui.student_instru_eval_class_comboBox.addItems(all_classes)

    def input_instru_result(self):
        """Takes the scores for instructor evaluation and adds the score for that instructer."""
        input_instru_name = self.ui.student_instru_eval_name_comboBox.currentText()
        input_class = self.ui.student_instru_eval_class_comboBox.currentText()
        input_class_index = self.ui.student_instru_eval_class_comboBox.currentIndex()

        input_Q1 = self.ui.student_instru_eval_Q1comboBox.currentText()
        input_Q2 = self.ui.student_instru_eval_Q2comboBox.currentText()
        input_Q3 = self.ui.student_instru_eval_Q3comboBox.currentText()
        input_Q4 = self.ui.student_instru_eval_Q4comboBox.currentText()
        input_Q5 = self.ui.student_instru_eval_Q5comboBox.currentText()
        input_Q6 = self.ui.student_instru_eval_Q6comboBox.currentText()
        input_Q7 = self.ui.student_instru_eval_Q7comboBox.currentText()
        instru_score = round(((int(input_Q1) + int(input_Q2) + int(input_Q3)
                               + int(input_Q4) + int(input_Q5) + int(input_Q6) + int(input_Q7)) / 7), 2)

        if input_instru_name != "Choose":
            self.ui.student_instru_eval_class_comboBox.removeItem(
                input_class_index)

            qtw.QMessageBox.information(self, "Done", """Score %s was added for %s's
                        %s class.""" % (instru_score, input_instru_name, input_class))

            insert_score_for_prof(input_instru_name, input_class, instru_score)


class StuEditPro(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ReportCard constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_edit_profile_page()
        self.ui.setupUi(self)

        self.ui.student_edit_profile_buttons.accepted.connect(
            self.input_student_edit_profile_information)

        student_info = get_student_edit_info(username)
        default_name = student_info[0]
        default_gender = student_info[1]
        default_field = student_info[2]
        # Show student's default data
        self.ui.student_edit_profile_fullname_lineEdit.setText(default_name)
        self.ui.student_edit_profile_gender_comboBox.setCurrentIndex(
            default_gender)
        self.ui.student_edit_profile_field_lineEdit.setText(default_field)

        self.username = username

    def input_student_edit_profile_information(self):
        """Inputs the user's information to update the profile."""
        input_name = self.ui.student_edit_profile_fullname_lineEdit.text()
        input_gender = self.ui.student_edit_profile_gender_comboBox.currentIndex()
        input_field = self.ui.student_edit_profile_field_lineEdit.text()
        edit_profile(self.username, input_name, input_gender, input_field)
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


class StudentMainPage(qtw.QMainWindow):

    def __init__(self, username, *args, **kwargs):
        """StudentMainPage constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_student_main_page()
        self.ui.setupUi(self)
        self.username = username

        self.exit = False

        # Set welcome label to users name
        self.ui.student_main_page_name_label.setText(
            get_name_by_username(self.username))

        # Set random quote of the day label
        self.ui.student_main_page_quote_body_label.setText(get_random_quote())
        self.ui.student_main_page_quote_body_label.adjustSize()

        # Connects the menu actions to functions for corresponding QDialogs
        self.ui.student_main_page_action_Courses.triggered.connect(
            self.open_my_courses_dialog)
        self.ui.student_main_page_action_Exam_Schedule.triggered.connect(
            self.open_exam_schedule_dialog)
        self.ui.student_main_page_action_Course_Enrollment.triggered.connect(
            self.open_class_enroll_dialog)
        self.ui.student_main_page_action_Report_Card.triggered.connect(
            self.open_report_card_dialog)
        self.ui.student_main_page_action_Instructor_Evaluation.triggered.connect(
            self.open_instru_eval_dialog)
        self.ui.student_main_page_action_Edit_Profile.triggered.connect(
            self.open_student_edit_profile_dialog)
        self.ui.student_main_page_action_Change_Password.triggered.connect(
            self.open_change_password_dialog)
        self.ui.student_main_page_action_Sign_Out.triggered.connect(
            self.sign_out)

        self.show()

    # The following functions opens the QDialogs for Student QMainWindow.
    def open_my_courses_dialog(self):
        """ Opens the My Courses page."""
        self.student_my_courses_page = MyCourses(self.username)
        self.student_my_courses_page.show()

    def open_exam_schedule_dialog(self):
        """ Opens the Exam Scedule page."""
        self.student_exam_schedule_page = ExamSchedule(self.username)
        self.student_exam_schedule_page.show()

    def open_class_enroll_dialog(self):
        """ Opens the Class Enrollment page."""
        self.student_class_enroll_page = ClassEnroll(self.username)
        self.student_class_enroll_page.show()

    def open_report_card_dialog(self):
        """ Opens the Report Card page."""
        self.student_report_card_page = ReportCard(self.username)
        self.student_report_card_page.show()

    def open_instru_eval_dialog(self):
        """ Opens the Instructor Evaluation page."""
        self.student_instru_eval_page = InstruEval(self.username)
        self.student_instru_eval_page.show()

    def open_student_edit_profile_dialog(self):
        """ Opens the Edit Profile page."""
        self.student_edit_profile_page = StuEditPro(self.username)
        self.student_edit_profile_page.show()

    def open_change_password_dialog(self):
        """ Opens the Change Password page."""
        self.change_password_page = ChangePass(self.username)
        self.change_password_page.show()

    def sign_out(self):
        """ Signs Out."""
        buttonReply = qtw.QMessageBox.question(
            self, "Note", "Are you sure you want to sign out?", qtw.QMessageBox.Yes, qtw.QMessageBox.No)
        if buttonReply == qtw.QMessageBox.Yes:
            self.exit = True
            self.close()
