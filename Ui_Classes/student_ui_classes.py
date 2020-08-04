from PyQt5 import QtCore, QtGui, QtWidgets

# Classes in this file was created by PyQt Designer.
# These create the base of QMainWindow and Qdialogs 
# used to show infomation about the student.

class Ui_student_main_page(object):
    def setupUi(self, student_main_page):
        student_main_page.setObjectName("student_main_page")
        student_main_page.resize(480, 440)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_main_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_main_page.setWindowIcon(icon)
        self.student_main_page_centralwidget = QtWidgets.QWidget(
            student_main_page)
        self.student_main_page_centralwidget.setObjectName(
            "student_main_page_centralwidget")
        self.student_main_page_utlogo = QtWidgets.QLabel(
            self.student_main_page_centralwidget)
        self.student_main_page_utlogo.setGeometry(
            QtCore.QRect(350, 10, 111, 111))
        self.student_main_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.student_main_page_utlogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.student_main_page_utlogo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_main_page_utlogo.setText("")
        self.student_main_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.student_main_page_utlogo.setObjectName("student_main_page_utlogo")
        self.student_main_page_frame = QtWidgets.QFrame(
            self.student_main_page_centralwidget)
        self.student_main_page_frame.setGeometry(QtCore.QRect(9, 9, 461, 401))
        self.student_main_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_main_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_main_page_frame.setObjectName("student_main_page_frame")
        self.student_main_page_welcome_label = QtWidgets.QLabel(
            self.student_main_page_frame)
        self.student_main_page_welcome_label.setGeometry(
            QtCore.QRect(11, 11, 341, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_main_page_welcome_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_main_page_welcome_label.setFont(font)
        self.student_main_page_welcome_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_main_page_welcome_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_main_page_welcome_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.student_main_page_welcome_label.setObjectName(
            "student_main_page_welcome_label")
        self.student_main_page_qoute_title_label = QtWidgets.QLabel(
            self.student_main_page_frame)
        self.student_main_page_qoute_title_label.setGeometry(
            QtCore.QRect(10, 170, 161, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_main_page_qoute_title_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.student_main_page_qoute_title_label.setFont(font)
        self.student_main_page_qoute_title_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_main_page_qoute_title_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_main_page_qoute_title_label.setObjectName(
            "student_main_page_qoute_title_label")
        self.student_main_page_quote_body_label = QtWidgets.QLabel(
            self.student_main_page_frame)
        self.student_main_page_quote_body_label.setGeometry(
            QtCore.QRect(10, 210, 441, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_main_page_quote_body_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(12)
        self.student_main_page_quote_body_label.setFont(font)
        self.student_main_page_quote_body_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.student_main_page_quote_body_label.setObjectName(
            "student_main_page_quote_body_label")
        self.student_main_page_name_label = QtWidgets.QLabel(
            self.student_main_page_frame)
        self.student_main_page_name_label.setGeometry(
            QtCore.QRect(10, 60, 341, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_main_page_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_main_page_name_label.setFont(font)
        self.student_main_page_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_main_page_name_label.setObjectName(
            "student_main_page_name_label")
        self.layoutWidget = QtWidgets.QWidget(
            self.student_main_page_centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.student_main_page_gridLayout = QtWidgets.QGridLayout(
            self.layoutWidget)
        self.student_main_page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.student_main_page_gridLayout.setObjectName(
            "student_main_page_gridLayout")
        self.layoutWidget.raise_()
        self.student_main_page_frame.raise_()
        self.student_main_page_utlogo.raise_()
        student_main_page.setCentralWidget(
            self.student_main_page_centralwidget)
        self.student_main_page_menu_bar = QtWidgets.QMenuBar(student_main_page)
        self.student_main_page_menu_bar.setGeometry(
            QtCore.QRect(0, 0, 480, 22))
        self.student_main_page_menu_bar.setObjectName(
            "student_main_page_menu_bar")
        self.student_main_page_menu_Academics = QtWidgets.QMenu(
            self.student_main_page_menu_bar)
        self.student_main_page_menu_Academics.setObjectName(
            "student_main_page_menu_Academics")
        self.student_main_page_menu_Courses = QtWidgets.QMenu(
            self.student_main_page_menu_Academics)
        self.student_main_page_menu_Courses.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_main_page_menu_Courses.setObjectName(
            "student_main_page_menu_Courses")
        self.student_main_page_menu_Profile = QtWidgets.QMenu(
            self.student_main_page_menu_bar)
        self.student_main_page_menu_Profile.setObjectName(
            "student_main_page_menu_Profile")
        student_main_page.setMenuBar(self.student_main_page_menu_bar)
        self.student_main_page_action_Report_Card = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Report_Card.setObjectName(
            "student_main_page_action_Report_Card")
        self.actionentekhab_vahed = QtWidgets.QAction(student_main_page)
        self.actionentekhab_vahed.setObjectName("actionentekhab_vahed")
        self.student_main_page_action_Edit_Profile = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Edit_Profile.setObjectName(
            "student_main_page_action_Edit_Profile")
        self.student_main_page_action_Change_Password = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Change_Password.setObjectName(
            "student_main_page_action_Change_Password")
        self.student_main_page_action_Courses = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Courses.setObjectName(
            "student_main_page_action_Courses")
        self.student_main_page_action_Exam_Schedule = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Exam_Schedule.setObjectName(
            "student_main_page_action_Exam_Schedule")
        self.student_main_page_action_Course_Enrollment = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Course_Enrollment.setObjectName(
            "student_main_page_action_Course_Enrollment")
        self.student_main_page_action_Sign_Out = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Sign_Out.setObjectName(
            "student_main_page_action_Sign_Out")
        self.student_main_page_action_Instructor_Evaluation = QtWidgets.QAction(
            student_main_page)
        self.student_main_page_action_Instructor_Evaluation.setObjectName(
            "student_main_page_action_Instructor_Evaluation")
        self.student_main_page_menu_Courses.addAction(
            self.student_main_page_action_Courses)
        self.student_main_page_menu_Courses.addAction(
            self.student_main_page_action_Exam_Schedule)
        self.student_main_page_menu_Courses.addAction(
            self.student_main_page_action_Course_Enrollment)
        self.student_main_page_menu_Academics.addAction(
            self.student_main_page_menu_Courses.menuAction())
        self.student_main_page_menu_Academics.addAction(
            self.student_main_page_action_Report_Card)
        self.student_main_page_menu_Academics.addSeparator()
        self.student_main_page_menu_Academics.addAction(
            self.student_main_page_action_Instructor_Evaluation)
        self.student_main_page_menu_Profile.addAction(
            self.student_main_page_action_Edit_Profile)
        self.student_main_page_menu_Profile.addAction(
            self.student_main_page_action_Change_Password)
        self.student_main_page_menu_Profile.addSeparator()
        self.student_main_page_menu_Profile.addAction(
            self.student_main_page_action_Sign_Out)
        self.student_main_page_menu_bar.addAction(
            self.student_main_page_menu_Academics.menuAction())
        self.student_main_page_menu_bar.addAction(
            self.student_main_page_menu_Profile.menuAction())

        self.retranslateUi(student_main_page)
        QtCore.QMetaObject.connectSlotsByName(student_main_page)

    def retranslateUi(self, student_main_page):
        _translate = QtCore.QCoreApplication.translate
        student_main_page.setWindowTitle(
            _translate("student_main_page", "Main Page"))
        self.student_main_page_welcome_label.setText(
            _translate("student_main_page", "Welcome"))
        self.student_main_page_qoute_title_label.setText(
            _translate("student_main_page", "Quote of the day:"))
        self.student_main_page_quote_body_label.setText(_translate("student_main_page", "\"The key to life is accepting challenges.\n"
                                                                   " Once someone stops doing this, he\'s dead.\" \n"
                                                                   "-Bette Davis"))
        self.student_main_page_name_label.setText(
            _translate("student_main_page", "**Person\'s Name**"))
        self.student_main_page_menu_Academics.setTitle(
            _translate("student_main_page", "Aca&demics"))
        self.student_main_page_menu_Courses.setTitle(
            _translate("student_main_page", "&Courses"))
        self.student_main_page_menu_Profile.setTitle(
            _translate("student_main_page", "Profi&le"))
        self.student_main_page_action_Report_Card.setText(
            _translate("student_main_page", "&Report Card"))
        self.actionentekhab_vahed.setText(_translate(
            "student_main_page", "Course Enrollment"))
        self.student_main_page_action_Edit_Profile.setText(
            _translate("student_main_page", "&Edit Profile"))
        self.student_main_page_action_Change_Password.setText(
            _translate("student_main_page", "&Change Password"))
        self.student_main_page_action_Courses.setText(
            _translate("student_main_page", "&My Courses"))
        self.student_main_page_action_Exam_Schedule.setText(
            _translate("student_main_page", "&Exam Schedule"))
        self.student_main_page_action_Course_Enrollment.setText(
            _translate("student_main_page", "&Class Enrollment"))
        self.student_main_page_action_Sign_Out.setText(
            _translate("student_main_page", "&Sign Out"))
        self.student_main_page_action_Instructor_Evaluation.setText(
            _translate("student_main_page", "I&nstructor Evaluation"))


class Ui_student_my_courses_page(object):
    def setupUi(self, student_my_courses_page):
        student_my_courses_page.setObjectName("student_my_courses_page")
        student_my_courses_page.resize(541, 440)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_my_courses_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_my_courses_page.setWindowIcon(icon)
        self.student_my_courses_frame = QtWidgets.QFrame(
            student_my_courses_page)
        self.student_my_courses_frame.setGeometry(
            QtCore.QRect(10, 10, 521, 421))
        self.student_my_courses_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_my_courses_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_my_courses_frame.setObjectName("student_my_courses_frame")
        self.student_my_courses_page_label = QtWidgets.QLabel(
            self.student_my_courses_frame)
        self.student_my_courses_page_label.setGeometry(
            QtCore.QRect(10, 80, 401, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_my_courses_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_my_courses_page_label.setFont(font)
        self.student_my_courses_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.student_my_courses_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_my_courses_page_label.setObjectName(
            "student_my_courses_page_label")
        self.student_my_courses_page_utlogo = QtWidgets.QLabel(
            self.student_my_courses_frame)
        self.student_my_courses_page_utlogo.setGeometry(
            QtCore.QRect(410, 10, 111, 111))
        self.student_my_courses_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_my_courses_page_utlogo.setText("")
        self.student_my_courses_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_my_courses_page_utlogo.setObjectName(
            "student_my_courses_page_utlogo")
        self.student_my_courses_button = QtWidgets.QDialogButtonBox(
            self.student_my_courses_frame)
        self.student_my_courses_button.setGeometry(
            QtCore.QRect(430, 380, 80, 25))
        self.student_my_courses_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_my_courses_button.setOrientation(QtCore.Qt.Horizontal)
        self.student_my_courses_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.student_my_courses_button.setObjectName(
            "student_my_courses_button")
        self.student_my_courses_tableWidget = QtWidgets.QTableWidget(
            student_my_courses_page)
        self.student_my_courses_tableWidget.setGeometry(
            QtCore.QRect(20, 130, 501, 251))
        self.student_my_courses_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_my_courses_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.student_my_courses_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.student_my_courses_tableWidget.setDragEnabled(True)
        self.student_my_courses_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.student_my_courses_tableWidget.setShowGrid(True)
        self.student_my_courses_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.student_my_courses_tableWidget.setWordWrap(True)
        self.student_my_courses_tableWidget.setCornerButtonEnabled(True)
        self.student_my_courses_tableWidget.setObjectName(
            "student_my_courses_tableWidget")
        self.student_my_courses_tableWidget.setColumnCount(5)
        self.student_my_courses_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.student_my_courses_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.student_my_courses_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_my_courses_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_my_courses_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_my_courses_tableWidget.setHorizontalHeaderItem(4, item)

        self.retranslateUi(student_my_courses_page)
        self.student_my_courses_button.accepted.connect(
            student_my_courses_page.accept)
        self.student_my_courses_button.rejected.connect(
            student_my_courses_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_my_courses_page)

    def retranslateUi(self, student_my_courses_page):
        _translate = QtCore.QCoreApplication.translate
        student_my_courses_page.setWindowTitle(
            _translate("student_my_courses_page", "My Courses"))
        self.student_my_courses_page_label.setText(
            _translate("student_my_courses_page", "My Courses"))
        self.student_my_courses_tableWidget.setSortingEnabled(False)
        item = self.student_my_courses_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student_my_courses_page", "Class"))
        item = self.student_my_courses_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student_my_courses_page", "Credit"))
        item = self.student_my_courses_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student_my_courses_page", "Professor"))
        item = self.student_my_courses_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student_my_courses_page", "Class Schedule"))
        item = self.student_my_courses_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("student_my_courses_page", "Exam Date"))


class Ui_student_exam_schedule_page(object):
    def setupUi(self, student_exam_schedule_page):
        student_exam_schedule_page.setObjectName("student_exam_schedule_page")
        student_exam_schedule_page.resize(442, 481)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_exam_schedule_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_exam_schedule_page.setWindowIcon(icon)
        self.student_exam_schedule_page_utlogo = QtWidgets.QLabel(
            student_exam_schedule_page)
        self.student_exam_schedule_page_utlogo.setGeometry(
            QtCore.QRect(320, 20, 111, 111))
        self.student_exam_schedule_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_exam_schedule_page_utlogo.setText("")
        self.student_exam_schedule_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_exam_schedule_page_utlogo.setObjectName(
            "student_exam_schedule_page_utlogo")
        self.student_exam_schedule_tableWidget = QtWidgets.QTableWidget(
            student_exam_schedule_page)
        self.student_exam_schedule_tableWidget.setGeometry(
            QtCore.QRect(20, 130, 401, 291))
        self.student_exam_schedule_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_exam_schedule_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.student_exam_schedule_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.student_exam_schedule_tableWidget.setDragEnabled(True)
        self.student_exam_schedule_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.student_exam_schedule_tableWidget.setShowGrid(True)
        self.student_exam_schedule_tableWidget.setGridStyle(
            QtCore.Qt.SolidLine)
        self.student_exam_schedule_tableWidget.setWordWrap(True)
        self.student_exam_schedule_tableWidget.setCornerButtonEnabled(True)
        self.student_exam_schedule_tableWidget.setObjectName(
            "student_exam_schedule_tableWidget")
        self.student_exam_schedule_tableWidget.setColumnCount(4)
        self.student_exam_schedule_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.student_exam_schedule_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_exam_schedule_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_exam_schedule_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_exam_schedule_tableWidget.setHorizontalHeaderItem(3, item)
        self.student_main_page_frame = QtWidgets.QFrame(
            student_exam_schedule_page)
        self.student_main_page_frame.setGeometry(
            QtCore.QRect(10, 10, 421, 461))
        self.student_main_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_main_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_main_page_frame.setObjectName("student_main_page_frame")
        self.student_exam_schedule_button = QtWidgets.QDialogButtonBox(
            self.student_main_page_frame)
        self.student_exam_schedule_button.setGeometry(
            QtCore.QRect(330, 420, 80, 25))
        self.student_exam_schedule_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_exam_schedule_button.setOrientation(QtCore.Qt.Horizontal)
        self.student_exam_schedule_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.student_exam_schedule_button.setObjectName(
            "student_exam_schedule_button")
        self.student_exam_schedule_page_label = QtWidgets.QLabel(
            self.student_main_page_frame)
        self.student_exam_schedule_page_label.setGeometry(
            QtCore.QRect(10, 80, 301, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_exam_schedule_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_exam_schedule_page_label.setFont(font)
        self.student_exam_schedule_page_label.setFrameShape(
            QtWidgets.QFrame.Box)
        self.student_exam_schedule_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.student_exam_schedule_page_label.setObjectName(
            "student_exam_schedule_page_label")
        self.student_main_page_frame.raise_()
        self.student_exam_schedule_page_utlogo.raise_()
        self.student_exam_schedule_tableWidget.raise_()

        self.retranslateUi(student_exam_schedule_page)
        self.student_exam_schedule_button.accepted.connect(
            student_exam_schedule_page.accept)
        self.student_exam_schedule_button.rejected.connect(
            student_exam_schedule_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_exam_schedule_page)

    def retranslateUi(self, student_exam_schedule_page):
        _translate = QtCore.QCoreApplication.translate
        student_exam_schedule_page.setWindowTitle(
            _translate("student_exam_schedule_page", "Exam Schedule"))
        self.student_exam_schedule_tableWidget.setSortingEnabled(False)
        item = self.student_exam_schedule_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student_exam_schedule_page", "Class"))
        item = self.student_exam_schedule_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student_exam_schedule_page", "Credit"))
        item = self.student_exam_schedule_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student_exam_schedule_page", "Professor"))
        item = self.student_exam_schedule_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student_exam_schedule_page", "Exam Date"))
        self.student_exam_schedule_page_label.setText(
            _translate("student_exam_schedule_page", "Exam Schedule"))


class Ui_student_class_enroll_page(object):
    def setupUi(self, student_class_enroll_page):
        student_class_enroll_page.setObjectName("student_class_enroll_page")
        student_class_enroll_page.resize(542, 440)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_class_enroll_page.setPalette(palette)
        student_class_enroll_page.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_class_enroll_page.setWindowIcon(icon)
        self.student_class_enroll_buttons = QtWidgets.QDialogButtonBox(
            student_class_enroll_page)
        self.student_class_enroll_buttons.setGeometry(
            QtCore.QRect(440, 390, 80, 25))
        self.student_class_enroll_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_class_enroll_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.student_class_enroll_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.student_class_enroll_buttons.setObjectName(
            "student_class_enroll_buttons")
        self.student_class_enroll_page_frame = QtWidgets.QFrame(
            student_class_enroll_page)
        self.student_class_enroll_page_frame.setGeometry(
            QtCore.QRect(10, 10, 521, 421))
        self.student_class_enroll_page_frame.setFrameShape(
            QtWidgets.QFrame.Box)
        self.student_class_enroll_page_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.student_class_enroll_page_frame.setObjectName(
            "student_class_enroll_page_frame")
        self.student_class_enroll_page_label = QtWidgets.QLabel(
            self.student_class_enroll_page_frame)
        self.student_class_enroll_page_label.setGeometry(
            QtCore.QRect(10, 90, 401, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_class_enroll_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_class_enroll_page_label.setFont(font)
        self.student_class_enroll_page_label.setFrameShape(
            QtWidgets.QFrame.Box)
        self.student_class_enroll_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.student_class_enroll_page_label.setObjectName(
            "student_class_enroll_page_label")
        self.student_class_enroll_page_utlogo = QtWidgets.QLabel(
            self.student_class_enroll_page_frame)
        self.student_class_enroll_page_utlogo.setGeometry(
            QtCore.QRect(410, 10, 111, 111))
        self.student_class_enroll_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_class_enroll_page_utlogo.setText("")
        self.student_class_enroll_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_class_enroll_page_utlogo.setObjectName(
            "student_class_enroll_page_utlogo")
        self.student_class_enroll_tableWidget = QtWidgets.QTableWidget(
            self.student_class_enroll_page_frame)
        self.student_class_enroll_tableWidget.setGeometry(
            QtCore.QRect(10, 130, 501, 241))
        self.student_class_enroll_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_class_enroll_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.student_class_enroll_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.student_class_enroll_tableWidget.setDragEnabled(True)
        self.student_class_enroll_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.student_class_enroll_tableWidget.setShowGrid(True)
        self.student_class_enroll_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.student_class_enroll_tableWidget.setWordWrap(True)
        self.student_class_enroll_tableWidget.setCornerButtonEnabled(True)
        self.student_class_enroll_tableWidget.setObjectName(
            "student_class_enroll_tableWidget")
        self.student_class_enroll_tableWidget.setColumnCount(5)
        self.student_class_enroll_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.student_class_enroll_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_class_enroll_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_class_enroll_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_class_enroll_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_class_enroll_tableWidget.setHorizontalHeaderItem(4, item)
        self.student_class_enroll_note_label = QtWidgets.QLabel(
            self.student_class_enroll_page_frame)
        self.student_class_enroll_note_label.setGeometry(
            QtCore.QRect(10, 380, 371, 17))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(12)
        font.setItalic(True)
        self.student_class_enroll_note_label.setFont(font)
        self.student_class_enroll_note_label.setObjectName(
            "student_class_enroll_note_label")
        self.student_class_enroll_page_frame.raise_()
        self.student_class_enroll_buttons.raise_()

        self.retranslateUi(student_class_enroll_page)
        self.student_class_enroll_buttons.accepted.connect(
            student_class_enroll_page.accept)
        self.student_class_enroll_buttons.rejected.connect(
            student_class_enroll_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_class_enroll_page)

    def retranslateUi(self, student_class_enroll_page):
        _translate = QtCore.QCoreApplication.translate
        student_class_enroll_page.setWindowTitle(_translate(
            "student_class_enroll_page", "Class Enrollment"))
        self.student_class_enroll_page_label.setText(
            _translate("student_class_enroll_page", "Class Enrollment"))
        self.student_class_enroll_tableWidget.setSortingEnabled(False)
        item = self.student_class_enroll_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student_class_enroll_page", "Class"))
        item = self.student_class_enroll_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student_class_enroll_page", "Credit"))
        item = self.student_class_enroll_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student_class_enroll_page", "Professor"))
        item = self.student_class_enroll_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student_class_enroll_page", "Class Schedule"))
        item = self.student_class_enroll_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("student_class_enroll_page", "Exam Date"))
        self.student_class_enroll_note_label.setText(_translate(
            "student_class_enroll_page", "Note: Double click on the class that you want to add."))


class Ui_student_report_card_page(object):
    def setupUi(self, student_report_card_page):
        student_report_card_page.setObjectName("student_report_card_page")
        student_report_card_page.resize(444, 440)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_report_card_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_report_card_page.setWindowIcon(icon)
        self.student_report_card_page_frame = QtWidgets.QFrame(
            student_report_card_page)
        self.student_report_card_page_frame.setGeometry(
            QtCore.QRect(10, 10, 421, 421))
        self.student_report_card_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_report_card_page_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.student_report_card_page_frame.setObjectName(
            "student_report_card_page_frame")
        self.student_report_card_page_label = QtWidgets.QLabel(
            self.student_report_card_page_frame)
        self.student_report_card_page_label.setGeometry(
            QtCore.QRect(10, 80, 291, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_report_card_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_report_card_page_label.setFont(font)
        self.student_report_card_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.student_report_card_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_report_card_page_label.setObjectName(
            "student_report_card_page_label")
        self.student_report_card_page_utlogo = QtWidgets.QLabel(
            self.student_report_card_page_frame)
        self.student_report_card_page_utlogo.setGeometry(
            QtCore.QRect(310, 0, 111, 111))
        self.student_report_card_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_report_card_page_utlogo.setText("")
        self.student_report_card_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_report_card_page_utlogo.setObjectName(
            "student_report_card_page_utlogo")
        self.student_report_card_tableWidget = QtWidgets.QTableWidget(
            self.student_report_card_page_frame)
        self.student_report_card_tableWidget.setGeometry(
            QtCore.QRect(10, 120, 401, 211))
        self.student_report_card_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.student_report_card_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.student_report_card_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.student_report_card_tableWidget.setDragEnabled(True)
        self.student_report_card_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.student_report_card_tableWidget.setShowGrid(True)
        self.student_report_card_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.student_report_card_tableWidget.setWordWrap(True)
        self.student_report_card_tableWidget.setCornerButtonEnabled(True)
        self.student_report_card_tableWidget.setObjectName(
            "student_report_card_tableWidget")
        self.student_report_card_tableWidget.setColumnCount(4)
        self.student_report_card_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.student_report_card_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_report_card_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_report_card_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_report_card_tableWidget.setHorizontalHeaderItem(3, item)
        self.student_report_card_gpa_label = QtWidgets.QLabel(
            self.student_report_card_page_frame)
        self.student_report_card_gpa_label.setGeometry(
            QtCore.QRect(10, 340, 311, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_report_card_gpa_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_report_card_gpa_label.setFont(font)
        self.student_report_card_gpa_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_report_card_gpa_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_report_card_gpa_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_report_card_gpa_label.setObjectName(
            "student_report_card_gpa_label")
        self.student_report_card_note_label = QtWidgets.QLabel(
            self.student_report_card_page_frame)
        self.student_report_card_note_label.setGeometry(
            QtCore.QRect(10, 370, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setItalic(True)
        self.student_report_card_note_label.setFont(font)
        self.student_report_card_note_label.setObjectName(
            "student_report_card_note_label")
        self.student_report_card_button = QtWidgets.QDialogButtonBox(
            self.student_report_card_page_frame)
        self.student_report_card_button.setGeometry(
            QtCore.QRect(330, 340, 80, 25))
        self.student_report_card_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_report_card_button.setOrientation(QtCore.Qt.Horizontal)
        self.student_report_card_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.student_report_card_button.setObjectName(
            "student_report_card_button")

        self.retranslateUi(student_report_card_page)
        self.student_report_card_button.accepted.connect(
            student_report_card_page.accept)
        self.student_report_card_button.rejected.connect(
            student_report_card_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_report_card_page)

    def retranslateUi(self, student_report_card_page):
        _translate = QtCore.QCoreApplication.translate
        student_report_card_page.setWindowTitle(
            _translate("student_report_card_page", "Report Card"))
        self.student_report_card_page_label.setText(
            _translate("student_report_card_page", "Report Card"))
        self.student_report_card_tableWidget.setSortingEnabled(False)
        item = self.student_report_card_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student_report_card_page", "Class"))
        item = self.student_report_card_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student_report_card_page", "Professor"))
        item = self.student_report_card_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student_report_card_page", "Credit"))
        item = self.student_report_card_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student_report_card_page", "Grade"))
        self.student_report_card_gpa_label.setText(
            _translate("student_report_card_page", "GPA = "))
        self.student_report_card_note_label.setText(_translate("student_report_card_page", "NOTE: These statistics does not define you nor \n"
                                                               "your intelligence."))


class Ui_student_instru_eval_page(object):
    def setupUi(self, student_instru_eval_page):
        student_instru_eval_page.setObjectName("student_instru_eval_page")
        student_instru_eval_page.resize(499, 488)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_instru_eval_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_instru_eval_page.setWindowIcon(icon)
        self.student_instru_eval_page_frame = QtWidgets.QFrame(
            student_instru_eval_page)
        self.student_instru_eval_page_frame.setGeometry(
            QtCore.QRect(10, 10, 481, 471))
        self.student_instru_eval_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_instru_eval_page_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.student_instru_eval_page_frame.setObjectName(
            "student_instru_eval_page_frame")
        self.student_instru_eval_page_label = QtWidgets.QLabel(
            self.student_instru_eval_page_frame)
        self.student_instru_eval_page_label.setGeometry(
            QtCore.QRect(10, 80, 341, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_instru_eval_page_label.setFont(font)
        self.student_instru_eval_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.student_instru_eval_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_instru_eval_page_label.setObjectName(
            "student_instru_eval_page_label")
        self.student_instru_eval_page_utlogo = QtWidgets.QLabel(
            self.student_instru_eval_page_frame)
        self.student_instru_eval_page_utlogo.setGeometry(
            QtCore.QRect(360, 0, 111, 111))
        self.student_instru_eval_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_instru_eval_page_utlogo.setText("")
        self.student_instru_eval_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_instru_eval_page_utlogo.setObjectName(
            "student_instru_eval_page_utlogo")
        self.layoutWidget = QtWidgets.QWidget(
            self.student_instru_eval_page_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 183, 364, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        self.student_instru_eval_verticalLayout = QtWidgets.QVBoxLayout(
            self.layoutWidget)
        self.student_instru_eval_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.student_instru_eval_verticalLayout.setObjectName(
            "student_instru_eval_verticalLayout")
        self.student_instru_eval_Q1 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q1.setFont(font)
        self.student_instru_eval_Q1.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q1.setObjectName("student_instru_eval_Q1")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q1)
        self.student_instru_eval_Q2 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q2.setFont(font)
        self.student_instru_eval_Q2.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q2.setObjectName("student_instru_eval_Q2")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q2)
        self.student_instru_eval_Q3 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q3.setFont(font)
        self.student_instru_eval_Q3.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q3.setObjectName("student_instru_eval_Q3")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q3)
        self.student_instru_eval_Q4 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q4.setFont(font)
        self.student_instru_eval_Q4.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q4.setObjectName("student_instru_eval_Q4")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q4)
        self.student_instru_eval_Q5 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q5.setFont(font)
        self.student_instru_eval_Q5.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q5.setObjectName("student_instru_eval_Q5")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q5)
        self.student_instru_eval_Q6 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q6.setFont(font)
        self.student_instru_eval_Q6.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q6.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q6.setObjectName("student_instru_eval_Q6")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q6)
        self.student_instru_eval_Q7 = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_Q7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.student_instru_eval_Q7.setFont(font)
        self.student_instru_eval_Q7.setFrameShape(QtWidgets.QFrame.Panel)
        self.student_instru_eval_Q7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_instru_eval_Q7.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.student_instru_eval_Q7.setObjectName("student_instru_eval_Q7")
        self.student_instru_eval_verticalLayout.addWidget(
            self.student_instru_eval_Q7)
        self.layoutWidget1 = QtWidgets.QWidget(
            self.student_instru_eval_page_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(380, 180, 82, 244))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.student_instru_eval_verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.layoutWidget1)
        self.student_instru_eval_verticalLayout_2.setContentsMargins(
            0, 0, 0, 0)
        self.student_instru_eval_verticalLayout_2.setObjectName(
            "student_instru_eval_verticalLayout_2")
        self.student_instru_eval_Q1comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q1comboBox.setObjectName(
            "student_instru_eval_Q1comboBox")
        self.student_instru_eval_Q1comboBox.addItem("")
        self.student_instru_eval_Q1comboBox.addItem("")
        self.student_instru_eval_Q1comboBox.addItem("")
        self.student_instru_eval_Q1comboBox.addItem("")
        self.student_instru_eval_Q1comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q1comboBox)
        self.student_instru_eval_Q2comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q2comboBox.setObjectName(
            "student_instru_eval_Q2comboBox")
        self.student_instru_eval_Q2comboBox.addItem("")
        self.student_instru_eval_Q2comboBox.addItem("")
        self.student_instru_eval_Q2comboBox.addItem("")
        self.student_instru_eval_Q2comboBox.addItem("")
        self.student_instru_eval_Q2comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q2comboBox)
        self.student_instru_eval_Q3comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q3comboBox.setObjectName(
            "student_instru_eval_Q3comboBox")
        self.student_instru_eval_Q3comboBox.addItem("")
        self.student_instru_eval_Q3comboBox.addItem("")
        self.student_instru_eval_Q3comboBox.addItem("")
        self.student_instru_eval_Q3comboBox.addItem("")
        self.student_instru_eval_Q3comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q3comboBox)
        self.student_instru_eval_Q4comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q4comboBox.setObjectName(
            "student_instru_eval_Q4comboBox")
        self.student_instru_eval_Q4comboBox.addItem("")
        self.student_instru_eval_Q4comboBox.addItem("")
        self.student_instru_eval_Q4comboBox.addItem("")
        self.student_instru_eval_Q4comboBox.addItem("")
        self.student_instru_eval_Q4comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q4comboBox)
        self.student_instru_eval_Q5comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q5comboBox.setObjectName(
            "student_instru_eval_Q5comboBox")
        self.student_instru_eval_Q5comboBox.addItem("")
        self.student_instru_eval_Q5comboBox.addItem("")
        self.student_instru_eval_Q5comboBox.addItem("")
        self.student_instru_eval_Q5comboBox.addItem("")
        self.student_instru_eval_Q5comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q5comboBox)
        self.student_instru_eval_Q6comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q6comboBox.setObjectName(
            "student_instru_eval_Q6comboBox")
        self.student_instru_eval_Q6comboBox.addItem("")
        self.student_instru_eval_Q6comboBox.addItem("")
        self.student_instru_eval_Q6comboBox.addItem("")
        self.student_instru_eval_Q6comboBox.addItem("")
        self.student_instru_eval_Q6comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q6comboBox)
        self.student_instru_eval_Q7comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        self.student_instru_eval_Q7comboBox.setObjectName(
            "student_instru_eval_Q7comboBox")
        self.student_instru_eval_Q7comboBox.addItem("")
        self.student_instru_eval_Q7comboBox.addItem("")
        self.student_instru_eval_Q7comboBox.addItem("")
        self.student_instru_eval_Q7comboBox.addItem("")
        self.student_instru_eval_Q7comboBox.addItem("")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_Q7comboBox)
        self.student_instru_eval_add_button = QtWidgets.QPushButton(
            self.layoutWidget1)
        self.student_instru_eval_add_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_instru_eval_add_button.setObjectName(
            "student_instru_eval_add_button")
        self.student_instru_eval_verticalLayout_2.addWidget(
            self.student_instru_eval_add_button)
        self.student_instru_eval_buttons = QtWidgets.QDialogButtonBox(
            self.student_instru_eval_page_frame)
        self.student_instru_eval_buttons.setGeometry(
            QtCore.QRect(380, 430, 80, 25))
        self.student_instru_eval_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_instru_eval_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.student_instru_eval_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.student_instru_eval_buttons.setObjectName(
            "student_instru_eval_buttons")
        self.widget = QtWidgets.QWidget(self.student_instru_eval_page_frame)
        self.widget.setGeometry(QtCore.QRect(10, 120, 121, 60))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.student_instru_eval_name_label = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.student_instru_eval_name_label.setFont(font)
        self.student_instru_eval_name_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_instru_eval_name_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_instru_eval_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_instru_eval_name_label.setObjectName(
            "student_instru_eval_name_label")
        self.gridLayout.addWidget(
            self.student_instru_eval_name_label, 0, 0, 1, 1)
        self.student_instru_eval_class_label = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_instru_eval_class_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.student_instru_eval_class_label.setFont(font)
        self.student_instru_eval_class_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_instru_eval_class_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_instru_eval_class_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.student_instru_eval_class_label.setObjectName(
            "student_instru_eval_class_label")
        self.gridLayout.addWidget(
            self.student_instru_eval_class_label, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.student_instru_eval_page_frame)
        self.widget1.setGeometry(QtCore.QRect(130, 120, 331, 58))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.student_instru_eval_name_comboBox = QtWidgets.QComboBox(
            self.widget1)
        self.student_instru_eval_name_comboBox.setObjectName(
            "student_instru_eval_name_comboBox")
        self.student_instru_eval_name_comboBox.addItem("")
        self.gridLayout_2.addWidget(
            self.student_instru_eval_name_comboBox, 0, 0, 1, 1)
        self.student_instru_eval_class_comboBox = QtWidgets.QComboBox(
            self.widget1)
        self.student_instru_eval_class_comboBox.setObjectName(
            "student_instru_eval_class_comboBox")
        self.gridLayout_2.addWidget(
            self.student_instru_eval_class_comboBox, 1, 0, 1, 1)

        self.retranslateUi(student_instru_eval_page)
        self.student_instru_eval_buttons.accepted.connect(
            student_instru_eval_page.accept)
        self.student_instru_eval_buttons.rejected.connect(
            student_instru_eval_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_instru_eval_page)

    def retranslateUi(self, student_instru_eval_page):
        _translate = QtCore.QCoreApplication.translate
        student_instru_eval_page.setWindowTitle(_translate(
            "student_instru_eval_page", "Instructor Evaluation"))
        self.student_instru_eval_page_label.setText(_translate(
            "student_instru_eval_page", "Instructor Evaluation"))
        self.student_instru_eval_Q1.setText(_translate(
            "student_instru_eval_page", "1. Related course materials to class needs."))
        self.student_instru_eval_Q2.setText(_translate(
            "student_instru_eval_page", "2. Tolerated differences of opinion."))
        self.student_instru_eval_Q3.setText(_translate(
            "student_instru_eval_page", "3. Answered questions completely. "))
        self.student_instru_eval_Q4.setText(_translate(
            "student_instru_eval_page", "4. Stayed on subject."))
        self.student_instru_eval_Q5.setText(_translate("student_instru_eval_page", "5.  Made course requirements and \n"
                                                       "objectives clear. "))
        self.student_instru_eval_Q6.setText(_translate(
            "student_instru_eval_page", "6. Encouraged class participation."))
        self.student_instru_eval_Q7.setText(_translate(
            "student_instru_eval_page", "7. Knew subject thouroughly."))

        self.student_instru_eval_name_comboBox.setItemText(
            0, _translate("student_instru_eval_page", "Choose"))

        self.student_instru_eval_Q1comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q1comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q1comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q1comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q1comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q2comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q2comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q2comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q2comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q2comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q3comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q3comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q3comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q3comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q3comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q4comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q4comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q4comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q4comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q4comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q5comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q5comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q5comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q5comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q5comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q6comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q6comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q6comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q6comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q6comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_Q7comboBox.setItemText(
            0, _translate("student_instru_eval_page", "5"))
        self.student_instru_eval_Q7comboBox.setItemText(
            1, _translate("student_instru_eval_page", "4"))
        self.student_instru_eval_Q7comboBox.setItemText(
            2, _translate("student_instru_eval_page", "3"))
        self.student_instru_eval_Q7comboBox.setItemText(
            3, _translate("student_instru_eval_page", "2"))
        self.student_instru_eval_Q7comboBox.setItemText(
            4, _translate("student_instru_eval_page", "1"))
        self.student_instru_eval_add_button.setText(
            _translate("student_instru_eval_page", "Add"))
        self.student_instru_eval_name_label.setText(
            _translate("student_instru_eval_page", "Instructor:"))
        self.student_instru_eval_class_label.setText(
            _translate("student_instru_eval_page", "Class:"))


class Ui_student_edit_profile_page(object):
    def setupUi(self, student_edit_profile_page):
        student_edit_profile_page.setObjectName("student_edit_profile_page")
        student_edit_profile_page.resize(480, 440)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        student_edit_profile_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_edit_profile_page.setWindowIcon(icon)
        self.student_edit_profile_frame = QtWidgets.QFrame(
            student_edit_profile_page)
        self.student_edit_profile_frame.setGeometry(
            QtCore.QRect(10, 10, 461, 421))
        self.student_edit_profile_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.student_edit_profile_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_edit_profile_frame.setLineWidth(1)
        self.student_edit_profile_frame.setObjectName(
            "student_edit_profile_frame")
        self.student_edit_profile_page_ut_logo = QtWidgets.QLabel(
            self.student_edit_profile_frame)
        self.student_edit_profile_page_ut_logo.setGeometry(
            QtCore.QRect(350, 0, 111, 111))
        self.student_edit_profile_page_ut_logo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.student_edit_profile_page_ut_logo.setMaximumSize(
            QtCore.QSize(111, 16777215))
        self.student_edit_profile_page_ut_logo.setText("")
        self.student_edit_profile_page_ut_logo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.student_edit_profile_page_ut_logo.setObjectName(
            "student_edit_profile_page_ut_logo")
        self.student_edit_profile_page_label = QtWidgets.QLabel(
            self.student_edit_profile_frame)
        self.student_edit_profile_page_label.setGeometry(
            QtCore.QRect(49, 134, 341, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_edit_profile_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.student_edit_profile_page_label.setFont(font)
        self.student_edit_profile_page_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_edit_profile_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.student_edit_profile_page_label.setObjectName(
            "student_edit_profile_page_label")
        self.layoutWidget = QtWidgets.QWidget(self.student_edit_profile_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 180, 116, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.student_edit_profile_verticalLayout = QtWidgets.QVBoxLayout(
            self.layoutWidget)
        self.student_edit_profile_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.student_edit_profile_verticalLayout.setObjectName(
            "student_edit_profile_verticalLayout")
        self.student_edit_profile_fullname_label = QtWidgets.QLabel(
            self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_edit_profile_fullname_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.student_edit_profile_fullname_label.setFont(font)
        self.student_edit_profile_fullname_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_edit_profile_fullname_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_edit_profile_fullname_label.setObjectName(
            "student_edit_profile_fullname_label")
        self.student_edit_profile_verticalLayout.addWidget(
            self.student_edit_profile_fullname_label)
        self.student_edit_profile_gender_label = QtWidgets.QLabel(
            self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_edit_profile_gender_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.student_edit_profile_gender_label.setFont(font)
        self.student_edit_profile_gender_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_edit_profile_gender_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_edit_profile_gender_label.setObjectName(
            "student_edit_profile_gender_label")
        self.student_edit_profile_verticalLayout.addWidget(
            self.student_edit_profile_gender_label)
        self.student_edit_profile_field_label = QtWidgets.QLabel(
            self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 154, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.student_edit_profile_field_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.student_edit_profile_field_label.setFont(font)
        self.student_edit_profile_field_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.student_edit_profile_field_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.student_edit_profile_field_label.setObjectName(
            "student_edit_profile_field_label")
        self.student_edit_profile_verticalLayout.addWidget(
            self.student_edit_profile_field_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.student_edit_profile_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 180, 221, 153))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.student_edit_profile_verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.layoutWidget1)
        self.student_edit_profile_verticalLayout_2.setContentsMargins(
            0, 0, 0, 0)
        self.student_edit_profile_verticalLayout_2.setObjectName(
            "student_edit_profile_verticalLayout_2")
        self.student_edit_profile_fullname_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget1)
        self.student_edit_profile_fullname_lineEdit.setText("")
        self.student_edit_profile_fullname_lineEdit.setFrame(True)
        self.student_edit_profile_fullname_lineEdit.setObjectName(
            "student_edit_profile_fullname_lineEdit")
        self.student_edit_profile_verticalLayout_2.addWidget(
            self.student_edit_profile_fullname_lineEdit)
        self.student_edit_profile_gender_comboBox = QtWidgets.QComboBox(
            self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student_edit_profile_gender_comboBox.setFont(font)
        self.student_edit_profile_gender_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_edit_profile_gender_comboBox.setObjectName(
            "student_edit_profile_gender_comboBox")
        self.student_edit_profile_gender_comboBox.addItem("")
        self.student_edit_profile_gender_comboBox.addItem("")
        self.student_edit_profile_verticalLayout_2.addWidget(
            self.student_edit_profile_gender_comboBox)
        self.student_edit_profile_field_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget1)
        self.student_edit_profile_field_lineEdit.setText("")
        self.student_edit_profile_field_lineEdit.setFrame(True)
        self.student_edit_profile_field_lineEdit.setObjectName(
            "student_edit_profile_field_lineEdit")
        self.student_edit_profile_verticalLayout_2.addWidget(
            self.student_edit_profile_field_lineEdit)
        self.student_edit_profile_buttons = QtWidgets.QDialogButtonBox(
            self.layoutWidget1)
        self.student_edit_profile_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student_edit_profile_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.student_edit_profile_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.student_edit_profile_buttons.setObjectName(
            "student_edit_profile_buttons")
        self.student_edit_profile_verticalLayout_2.addWidget(
            self.student_edit_profile_buttons)
        self.layoutWidget_2 = QtWidgets.QWidget(student_edit_profile_page)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.student_edit_profile_page_layout = QtWidgets.QGridLayout(
            self.layoutWidget_2)
        self.student_edit_profile_page_layout.setContentsMargins(0, 0, 0, 0)
        self.student_edit_profile_page_layout.setObjectName(
            "student_edit_profile_page_layout")

        self.retranslateUi(student_edit_profile_page)
        self.student_edit_profile_buttons.accepted.connect(
            student_edit_profile_page.accept)
        self.student_edit_profile_buttons.rejected.connect(
            student_edit_profile_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_edit_profile_page)

    def retranslateUi(self, student_edit_profile_page):
        _translate = QtCore.QCoreApplication.translate
        student_edit_profile_page.setWindowTitle(
            _translate("student_edit_profile_page", "Edit Profile"))
        self.student_edit_profile_page_label.setToolTip(_translate(
            "student_edit_profile_page", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.student_edit_profile_page_label.setText(
            _translate("student_edit_profile_page", "Edit Profile"))
        self.student_edit_profile_fullname_label.setText(
            _translate("student_edit_profile_page", "Full Name:"))
        self.student_edit_profile_gender_label.setText(
            _translate("student_edit_profile_page", "Gender:"))
        self.student_edit_profile_field_label.setText(
            _translate("student_edit_profile_page", "Field :"))
        self.student_edit_profile_gender_comboBox.setItemText(
            1, _translate("student_edit_profile_page", "Female"))
        self.student_edit_profile_gender_comboBox.setItemText(
            0, _translate("student_edit_profile_page", "Male"))
