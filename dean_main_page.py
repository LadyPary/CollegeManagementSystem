import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from database_functions import (change_password, class_approve_or_reject,
                                edit_profile, get_all_classes, get_all_profs,
                                get_all_students, get_class_info_for_approval,
                                get_class_score_prof, get_dean_edit_info,
                                get_gpa_of_student, get_name_by_username,
                                get_random_quote,
                                get_students_info_for_approval, get_top_profs,
                                get_top_students, get_username_by_name,
                                student_approve_or_reject,convert_str_to_othertype)

from Ui_Classes.dean_ui_classes import (Ui_dean_classes_page, Ui_dean_main_page,
                             Ui_dean_new_class_request_page,
                             Ui_dean_new_student_request_page,
                             Ui_dean_profs_page, Ui_dean_students_page,
                             Ui_dean_top_profs_page, Ui_dean_top_students_page)
                             
from Ui_Classes.same_ui_classes import Ui_change_password_page, Ui_edit_profile_page



class DeanStudents(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_students_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.dean_students_tableWidget.setRowCount(0)

        self.show_students()

    def show_students(self):
        """Shows all students' student ID,
            name, field, classes in table"""
        all_students = get_all_students()
        if all_students != "none":
            for row_num, each_student in enumerate(all_students):
                self.ui.dean_students_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_student):
                    self.ui.dean_students_tableWidget.setItem(row_num, col_num,
                                                              qtw.QTableWidgetItem(str(data)))


class DeanProfessors(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_profs_page()
        self.ui.setupUi(self)
        self.username = username

        self.show_profs()

    def show_profs(self):
        """Shows all professors' classes and names"""
        all_profs = get_all_profs()
        if all_profs != "none":
            for row_num, each_prof in enumerate(all_profs):
                self.ui.dean_profs_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_prof):
                    self.ui.dean_profs_tableWidget.setItem(row_num, col_num,
                                                           qtw.QTableWidgetItem(data))


class DeanClasses(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_classes_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.dean_classes_tableWidget.setRowCount(0)

        self.show_classes()

    def show_classes(self):
        """Shows all classes' name, credit, professor,
            number of students, schedule, exam date"""

        all_classes = get_all_classes()

        if all_classes != "none":

            for row_num, each_class in enumerate(all_classes):

                students_in_class = each_class[2]
                if students_in_class == "none":
                    number_students = 0
                else:
                    students_in_class = convert_str_to_othertype(
                        students_in_class)
                    number_students = len(students_in_class)
                self.ui.dean_classes_tableWidget.insertRow(row_num)

                new_class_info = (each_class[0],
                                  each_class[3],
                                  each_class[1],
                                  number_students,
                                  each_class[4],
                                  each_class[5]
                                  )

                for col_num, data in enumerate(new_class_info):
                    self.ui.dean_classes_tableWidget.setItem(row_num, col_num,
                                                             qtw.QTableWidgetItem(str(data)))


class NewStuReq(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ClassRequest constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_new_student_request_page()
        self.ui.setupUi(self)
        self.username = username

        self.ui.dean_new_student_request_tableWidget.setRowCount(0)
        self.ui.dean_new_student_request_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        # When double clicked on a row, will signal choose_class function
        self.ui.dean_new_student_request_tableWidget.itemDoubleClicked.connect(
            self.choose_student)

        self.ui.dean_new_student_request_accept_Button.clicked.connect(
            self.student_accepted)
        self.ui.dean_new_student_request_decline_button.clicked.connect(
            self.student_rejected)

        self.show_students_request()

    def show_students_request(self):
        """Show the new student's ID, name and field"""
        all_students = get_students_info_for_approval()
        if all_students != "none":
            for row_num, each_student in enumerate(all_students):
                self.ui.dean_new_student_request_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_student):
                    self.ui.dean_new_student_request_tableWidget.setItem(row_num, col_num,
                                                                         qtw.QTableWidgetItem(str(data)))

    def choose_student(self):
        """Select the student and change the
            label's text to their student ID."""
        selected_student = self.ui.dean_new_student_request_tableWidget.selectedItems()

        self.selected_row_index = selected_student[0].row()

        student_ID = selected_student[0].text()
        self.ui.dean_new_student_request_id_label.setText(student_ID)
        self.ui.dean_new_student_request_id_label.adjustSize()

    def student_accepted(self):
        """Adds the student to students table and removes it from new requests."""
        student_ID = self.ui.dean_new_student_request_id_label.text()
        if student_ID == "Student ID":
            qtw.QMessageBox.critical(
                self, "Note", "Please select a student first.")
        else:
            self.ui.dean_new_student_request_id_label.setText("Student ID")
            self.ui.dean_new_student_request_id_label.adjustSize()

            student_approve_or_reject(student_ID, 1)
            qtw.QMessageBox.information(
                self, "Done", "%s is successfully added to students." % (student_ID))
            self.ui.dean_new_student_request_tableWidget.removeRow(
                self.selected_row_index)

    def student_rejected(self):
        """Rejects the student removes it from new requests."""
        student_ID = self.ui.dean_new_student_request_id_label.text()
        if student_ID == "Student ID":
            qtw.QMessageBox.critical(
                self, "Note", "Please select a student first.")

        else:
            self.ui.dean_new_student_request_id_label.setText("Student ID")
            self.ui.dean_new_student_request_id_label.adjustSize()

            student_approve_or_reject(student_ID, 2)
            qtw.QMessageBox.information(
                self, "Done", "%s has been rejected." % (student_ID))
            self.ui.dean_new_student_request_tableWidget.removeRow(
                self.selected_row_index)


class NewClassReq(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ClassReqStat constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_new_class_request_page()
        self.ui.setupUi(self)

        self.username = username

        self.ui.dean_new_class_request_tableWidget.setRowCount(0)
        self.ui.dean_new_class_request_tableWidget.setSelectionBehavior(
            qtw.QTableView.SelectRows)

        # When double clicked on a row, will signal choose_class function
        self.ui.dean_new_class_request_tableWidget.itemDoubleClicked.connect(
            self.choose_class)

        self.ui.dean_new_class_request_accept_Button.clicked.connect(
            self.class_accepted)
        self.ui.dean_new_class_request_decline_button.clicked.connect(
            self.class_rejected)

        self.show_classes_request()

    def show_classes_request(self):
        """Show the new class name, professor,
            credit, schedule, exam date."""

        all_classes = get_class_info_for_approval()
        if all_classes != "none":
            for row_num, each_student in enumerate(all_classes):
                self.ui.dean_new_class_request_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_student):
                    self.ui.dean_new_class_request_tableWidget.setItem(row_num, col_num,
                                                                       qtw.QTableWidgetItem(str(data)))

    def choose_class(self):
        """Select the class and change the
            labels text to its name and professor."""

        selected_class = self.ui.dean_new_class_request_tableWidget.selectedItems()

        self.selected_row_index = selected_class[0].row()

        class_name = selected_class[0].text()
        class_prof = selected_class[1].text()

        self.ui.dean_new_class_request_class_label.setText(class_name)
        self.ui.dean_new_class_request_prof_label.setText(class_prof)
        self.ui.dean_new_class_request_class_label.adjustSize()
        self.ui.dean_new_class_request_prof_label.adjustSize()

    def class_accepted(self):
        """Adds the class to classes table and its professor's classes
            and removes it from new requests."""

        class_name = self.ui.dean_new_class_request_class_label.text()
        class_prof = self.ui.dean_new_class_request_prof_label.text()

        if class_name == "Class":
            qtw.QMessageBox.critical(
                self, "Note", "Please select a class first.")
        else:
            self.ui.dean_new_class_request_class_label.setText("Class")
            self.ui.dean_new_class_request_prof_label.setText("Professor")
            self.ui.dean_new_class_request_class_label.adjustSize()
            self.ui.dean_new_class_request_prof_label.adjustSize()

            class_approve_or_reject(class_name, class_prof, 1)
            qtw.QMessageBox.information(
                self, "Done", "%s's %s class is successfully added to classes." % (class_prof, class_name))
            self.ui.dean_new_class_request_tableWidget.removeRow(
                self.selected_row_index)

    def class_rejected(self):
        """Rejects the class and removes it from new requests."""

        class_name = self.ui.dean_new_class_request_class_label.text()
        class_prof = self.ui.dean_new_class_request_prof_label.text()

        if class_name == "Class":
            qtw.QMessageBox.critical(
                self, "Note", "Please select a class first.")
        else:
            self.ui.dean_new_class_request_class_label.setText("Class")
            self.ui.dean_new_class_request_prof_label.setText("Professor")
            self.ui.dean_new_class_request_class_label.adjustSize()
            self.ui.dean_new_class_request_prof_label.adjustSize()

            class_approve_or_reject(class_name, class_prof, 2)
            qtw.QMessageBox.information(
                self, "Done", "%s's %s class has been rejected." % (class_prof, class_name))
            self.ui.dean_new_class_request_tableWidget.removeRow(
                self.selected_row_index)


class TopStudents(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_top_students_page()
        self.ui.setupUi(self)
        self.username = username

        self.show_students()

    def show_students(self):
        """Shows top students' rank, student ID,
            name and gpa in table"""

        all_students = get_all_students()

        # Updates the student's gpa
        for each_student in all_students:
            get_gpa_of_student(each_student[0])

        top_students = get_top_students()

        if top_students != "none":
            for row_num, each_student in enumerate(top_students):
                self.ui.dean_top_students_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_student):
                    self.ui.dean_top_students_tableWidget.setItem(row_num, col_num,
                                                                  qtw.QTableWidgetItem(str(data)))


class TopProfs(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """ProfStudents constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_top_profs_page()
        self.ui.setupUi(self)
        self.username = username

        self.show_profs()

    def show_profs(self):
        """Shows top professors' rank,
            name and class in table"""

        top_profs = get_top_profs()

        if top_profs != "none":
            for row_num, each_prof in enumerate(top_profs):
                self.ui.dean_top_profs_tableWidget.insertRow(row_num)
                for col_num, data in enumerate(each_prof):
                    self.ui.dean_top_profs_tableWidget.setItem(row_num, col_num,
                                                               qtw.QTableWidgetItem(str(data)))
        self.ui.dean_top_profs_tableWidget.sortItems(0, qtc.Qt.DescendingOrder)


class EditPro(qtw.QDialog):

    def __init__(self, username, *args, **kwargs):
        """EditPro constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_edit_profile_page()
        self.ui.setupUi(self)

        self.ui.edit_profile_button.accepted.connect(
            self.input_edit_profile_information)

        dean_info = get_dean_edit_info(username)
        default_name = dean_info[0]
        default_gender = dean_info[1]

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


class DeanMainPage(qtw.QMainWindow):

    def __init__(self, username, *args, **kwargs):
        """ProfessorMainPage constructor."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_dean_main_page()
        self.ui.setupUi(self)
        self.username = username

        # Set welcome label to users name
        self.ui.dean_main_page_name_label.setText(
            get_name_by_username(self.username))

        # Set random quote of the day label
        self.ui.dean_main_page_quote_body_label.setText(get_random_quote())
        self.ui.dean_main_page_quote_body_label.adjustSize()

        # Connects the menu actions to functions for corresponding QDialogs
        self.ui.dean_main_page_action_All_Students.triggered.connect(
            self.open_students_dialog)
        self.ui.dean_main_page_action_Top_Students.triggered.connect(
            self.open_top_students_dialog)
        self.ui.dean_main_page_action_All_Professors.triggered.connect(
            self.open_profs_dialog)
        self.ui.adean_main_page_action_Top_Professors.triggered.connect(
            self.open_top_profs_dialog)
        self.ui.dean_main_page_action_Classes.triggered.connect(
            self.open_classes_dialog)
        self.ui.dean_main_page_action_Student_Request.triggered.connect(
            self.open_new_student_request_dialog)
        self.ui.dean_main_page_action_Class_Request.triggered.connect(
            self.open_new_classes_request_dialog)
        self.ui.dean_main_page_action_Edit_Profile.triggered.connect(
            self.open_edit_profile_dialog)
        self.ui.dean_main_page_action_Change_Password.triggered.connect(
            self.open_change_password_dialog)
        self.ui.dean_main_page_action_Sign_Out.triggered.connect(self.sign_out)

        self.show()

    # The following functions opens the QDialogs for deanessor QMainWindow.

    def open_students_dialog(self):
        """ Opens the Students page."""
        self.dean_students_page = DeanStudents(self.username)
        self.dean_students_page.show()

    def open_profs_dialog(self):
        """ Opens the Professors page."""
        self.dean_profs_page = DeanProfessors(self.username)
        self.dean_profs_page.show()

    def open_classes_dialog(self):
        """ Opens the Classes page."""
        self.dean_classes_page = DeanClasses(self.username)
        self.dean_classes_page.show()

    def open_top_students_dialog(self):
        """ Opens the Top Students page."""
        self.dean_top_students_page = TopStudents(self.username)
        self.dean_top_students_page.show()

    def open_top_profs_dialog(self):
        """ Opens the Top Professors page."""
        self.dean_top_profs_page = TopProfs(self.username)
        self.dean_top_profs_page.show()

    def open_new_student_request_dialog(self):
        """ Opens the New Student Request page."""
        self.dean_new_student_request_page = NewStuReq(self.username)
        self.dean_new_student_request_page.show()

    def open_new_classes_request_dialog(self):
        """ Opens the New Student Request page."""
        self.dean_new_classes_request_page = NewClassReq(self.username)
        self.dean_new_classes_request_page.show()

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


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = DeanMainPage("yasemi@gmail.com")
    sys.exit(app.exec_())

