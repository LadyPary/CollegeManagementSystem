from PyQt5 import QtCore, QtGui, QtWidgets

# Classes in this file was created by PyQt Designer.
# These create the base of QMainWindow and Qdialogs
# used to show infomation about the professor.


class Ui_prof_main_page(object):
    def setupUi(self, prof_main_page):
        prof_main_page.setObjectName("prof_main_page")
        prof_main_page.resize(480, 440)
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
        prof_main_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_main_page.setWindowIcon(icon)
        self.prof_main_page_centralwidget = QtWidgets.QWidget(prof_main_page)
        self.prof_main_page_centralwidget.setObjectName(
            "prof_main_page_centralwidget")
        self.prof_main_page_frame = QtWidgets.QFrame(
            self.prof_main_page_centralwidget)
        self.prof_main_page_frame.setGeometry(QtCore.QRect(10, 10, 461, 381))
        self.prof_main_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_main_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_main_page_frame.setObjectName("prof_main_page_frame")
        self.prof_main_page_welcome_label = QtWidgets.QLabel(
            self.prof_main_page_frame)
        self.prof_main_page_welcome_label.setGeometry(
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
        self.prof_main_page_welcome_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_main_page_welcome_label.setFont(font)
        self.prof_main_page_welcome_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.prof_main_page_welcome_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_main_page_welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_main_page_welcome_label.setObjectName(
            "prof_main_page_welcome_label")
        self.prof_main_page_qoute_title_label = QtWidgets.QLabel(
            self.prof_main_page_frame)
        self.prof_main_page_qoute_title_label.setGeometry(
            QtCore.QRect(10, 150, 171, 31))
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
        self.prof_main_page_qoute_title_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_main_page_qoute_title_label.setFont(font)
        self.prof_main_page_qoute_title_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.prof_main_page_qoute_title_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_main_page_qoute_title_label.setObjectName(
            "prof_main_page_qoute_title_label")
        self.prof_main_page_quote_body_label = QtWidgets.QLabel(
            self.prof_main_page_frame)
        self.prof_main_page_quote_body_label.setGeometry(
            QtCore.QRect(10, 193, 441, 171))
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
        self.prof_main_page_quote_body_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(12)
        self.prof_main_page_quote_body_label.setFont(font)
        self.prof_main_page_quote_body_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.prof_main_page_quote_body_label.setObjectName(
            "prof_main_page_quote_body_label")
        self.prof_main_page_name_label = QtWidgets.QLabel(
            self.prof_main_page_frame)
        self.prof_main_page_name_label.setGeometry(
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
        self.prof_main_page_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.prof_main_page_name_label.setFont(font)
        self.prof_main_page_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_main_page_name_label.setObjectName(
            "prof_main_page_name_label")
        self.prof_main_page_quote_body_label.raise_()
        self.prof_main_page_welcome_label.raise_()
        self.prof_main_page_qoute_title_label.raise_()
        self.prof_main_page_name_label.raise_()
        self.prof_main_page_utlogo = QtWidgets.QLabel(
            self.prof_main_page_centralwidget)
        self.prof_main_page_utlogo.setGeometry(QtCore.QRect(351, 11, 111, 111))
        self.prof_main_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.prof_main_page_utlogo.setText("")
        self.prof_main_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.prof_main_page_utlogo.setObjectName("prof_main_page_utlogo")
        prof_main_page.setCentralWidget(self.prof_main_page_centralwidget)
        self.prof_main_page_menu_bar = QtWidgets.QMenuBar(prof_main_page)
        self.prof_main_page_menu_bar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.prof_main_page_menu_bar.setObjectName("prof_main_page_menu_bar")
        self.prof_main_page_menu_Class_Management = QtWidgets.QMenu(
            self.prof_main_page_menu_bar)
        self.prof_main_page_menu_Class_Management.setObjectName(
            "prof_main_page_menu_Class_Management")
        self.prof_main_page_menu_Class_Request = QtWidgets.QMenu(
            self.prof_main_page_menu_Class_Management)
        self.prof_main_page_menu_Class_Request.setObjectName(
            "prof_main_page_menu_Class_Request")
        self.prof_main_page_menu_Profile = QtWidgets.QMenu(
            self.prof_main_page_menu_bar)
        self.prof_main_page_menu_Profile.setObjectName(
            "prof_main_page_menu_Profile")
        prof_main_page.setMenuBar(self.prof_main_page_menu_bar)
        self.statusbar = QtWidgets.QStatusBar(prof_main_page)
        self.statusbar.setObjectName("statusbar")
        prof_main_page.setStatusBar(self.statusbar)
        self.actionCourse_Request = QtWidgets.QAction(prof_main_page)
        self.actionCourse_Request.setObjectName("actionCourse_Request")
        self.actionMy_Classes = QtWidgets.QAction(prof_main_page)
        self.actionMy_Classes.setObjectName("actionMy_Classes")
        self.actionCourse_Request_2 = QtWidgets.QAction(prof_main_page)
        self.actionCourse_Request_2.setObjectName("actionCourse_Request_2")
        self.actionStudents = QtWidgets.QAction(prof_main_page)
        self.actionStudents.setObjectName("actionStudents")
        self.actionCourse_Request_3 = QtWidgets.QAction(prof_main_page)
        self.actionCourse_Request_3.setObjectName("actionCourse_Request_3")
        self.prof_main_page_action_Edit_Profile = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page_action_Edit_Profile.setObjectName(
            "prof_main_page_action_Edit_Profile")
        self.prof_main_page_action_Change_Password = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page_action_Change_Password.setObjectName(
            "prof_main_page_action_Change_Password")
        self.prof_main_page_action_Sign_Out = QtWidgets.QAction(prof_main_page)
        self.prof_main_page_action_Sign_Out.setObjectName(
            "prof_main_page_action_Sign_Out")
        self.actionSubmit_Grades = QtWidgets.QAction(prof_main_page)
        self.actionSubmit_Grades.setObjectName("actionSubmit_Grades")
        self.actionClass_Request = QtWidgets.QAction(prof_main_page)
        self.actionClass_Request.setObjectName("actionClass_Request")
        self.actionSubmit_Grades_2 = QtWidgets.QAction(prof_main_page)
        self.actionSubmit_Grades_2.setObjectName("actionSubmit_Grades_2")
        self.prof_main_page_action_My_Classes = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page_action_My_Classes.setObjectName(
            "prof_main_page_action_My_Classes")
        self.prof_main_page_action_Submit_Grades = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page_action_Submit_Grades.setObjectName(
            "prof_main_page_action_Submit_Grades")
        self.prof_main_page_action_Students = QtWidgets.QAction(prof_main_page)
        self.prof_main_page_action_Students.setObjectName(
            "prof_main_page_action_Students")
        self.prof_main_page_action_New_Class_Requset = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page_action_New_Class_Requset.setObjectName(
            "prof_main_page_action_New_Class_Requset")
        self.prof_main_page__action_Class_Requests_Status = QtWidgets.QAction(
            prof_main_page)
        self.prof_main_page__action_Class_Requests_Status.setObjectName(
            "prof_main_page__action_Class_Requests_Status")
        self.prof_main_page_menu_Class_Request.addAction(
            self.prof_main_page_action_New_Class_Requset)
        self.prof_main_page_menu_Class_Request.addAction(
            self.prof_main_page__action_Class_Requests_Status)
        self.prof_main_page_menu_Class_Management.addAction(
            self.prof_main_page_action_My_Classes)
        self.prof_main_page_menu_Class_Management.addAction(
            self.prof_main_page_menu_Class_Request.menuAction())
        self.prof_main_page_menu_Class_Management.addAction(
            self.prof_main_page_action_Students)
        self.prof_main_page_menu_Class_Management.addAction(
            self.prof_main_page_action_Submit_Grades)
        self.prof_main_page_menu_Profile.addAction(
            self.prof_main_page_action_Edit_Profile)
        self.prof_main_page_menu_Profile.addAction(
            self.prof_main_page_action_Change_Password)
        self.prof_main_page_menu_Profile.addSeparator()
        self.prof_main_page_menu_Profile.addAction(
            self.prof_main_page_action_Sign_Out)
        self.prof_main_page_menu_bar.addAction(
            self.prof_main_page_menu_Class_Management.menuAction())
        self.prof_main_page_menu_bar.addAction(
            self.prof_main_page_menu_Profile.menuAction())

        self.retranslateUi(prof_main_page)
        QtCore.QMetaObject.connectSlotsByName(prof_main_page)

    def retranslateUi(self, prof_main_page):
        _translate = QtCore.QCoreApplication.translate
        prof_main_page.setWindowTitle(
            _translate("prof_main_page", "Main Page"))
        self.prof_main_page_welcome_label.setText(
            _translate("prof_main_page", "Welcome"))
        self.prof_main_page_qoute_title_label.setText(
            _translate("prof_main_page", "Quote of the day:"))
        self.prof_main_page_quote_body_label.setText(_translate("prof_main_page", "\"The key to life is accepting challenges.\n"
                                                                " Once someone stops doing this, he\'s dead.\" \n"
                                                                "-Bette Davis"))
        self.prof_main_page_name_label.setText(
            _translate("prof_main_page", "**Prof Name**"))
        self.prof_main_page_menu_Class_Management.setTitle(
            _translate("prof_main_page", "&Class Management"))
        self.prof_main_page_menu_Class_Request.setTitle(
            _translate("prof_main_page", "&Class Request"))
        self.prof_main_page_menu_Profile.setTitle(
            _translate("prof_main_page", "Profi&le"))
        self.actionCourse_Request.setText(
            _translate("prof_main_page", "Course Request"))
        self.actionMy_Classes.setText(
            _translate("prof_main_page", "My Classes"))
        self.actionCourse_Request_2.setText(
            _translate("prof_main_page", "Course Request"))
        self.actionStudents.setText(_translate("prof_main_page", "Students"))
        self.actionCourse_Request_3.setText(
            _translate("prof_main_page", "Class Request"))
        self.prof_main_page_action_Edit_Profile.setText(
            _translate("prof_main_page", "&Edit Profile"))
        self.prof_main_page_action_Change_Password.setText(
            _translate("prof_main_page", "&Change Password"))
        self.prof_main_page_action_Sign_Out.setText(
            _translate("prof_main_page", "&Sign Out"))
        self.actionSubmit_Grades.setText(
            _translate("prof_main_page", "Submit Grades"))
        self.actionClass_Request.setText(
            _translate("prof_main_page", "Class Request"))
        self.actionSubmit_Grades_2.setText(
            _translate("prof_main_page", "Submit Grades"))
        self.prof_main_page_action_My_Classes.setText(
            _translate("prof_main_page", "&My Classes"))
        self.prof_main_page_action_Submit_Grades.setText(
            _translate("prof_main_page", "&Submit Grades"))
        self.prof_main_page_action_Students.setText(
            _translate("prof_main_page", "St&udents"))
        self.prof_main_page_action_New_Class_Requset.setText(
            _translate("prof_main_page", "&New Class Requset"))
        self.prof_main_page__action_Class_Requests_Status.setText(
            _translate("prof_main_page", "&Class Requests Status"))


class Ui_prof_my_classes_page(object):
    def setupUi(self, prof_my_classes_page):
        prof_my_classes_page.setObjectName("prof_my_classes_page")
        prof_my_classes_page.resize(541, 440)
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
        prof_my_classes_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_my_classes_page.setWindowIcon(icon)
        self.prof_my_classes_page_button = QtWidgets.QDialogButtonBox(
            prof_my_classes_page)
        self.prof_my_classes_page_button.setGeometry(
            QtCore.QRect(440, 390, 80, 25))
        self.prof_my_classes_page_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_my_classes_page_button.setOrientation(QtCore.Qt.Horizontal)
        self.prof_my_classes_page_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.prof_my_classes_page_button.setObjectName(
            "prof_my_classes_page_button")
        self.prof_my_classes_page_label = QtWidgets.QLabel(
            prof_my_classes_page)
        self.prof_my_classes_page_label.setGeometry(
            QtCore.QRect(20, 90, 391, 38))
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
        self.prof_my_classes_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_my_classes_page_label.setFont(font)
        self.prof_my_classes_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_my_classes_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_my_classes_page_label.setObjectName(
            "prof_my_classes_page_label")
        self.prof_my_classes_tableWidget = QtWidgets.QTableWidget(
            prof_my_classes_page)
        self.prof_my_classes_tableWidget.setGeometry(
            QtCore.QRect(20, 130, 501, 251))
        self.prof_my_classes_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.prof_my_classes_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.prof_my_classes_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prof_my_classes_tableWidget.setDragEnabled(True)
        self.prof_my_classes_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.prof_my_classes_tableWidget.setShowGrid(True)
        self.prof_my_classes_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.prof_my_classes_tableWidget.setWordWrap(True)
        self.prof_my_classes_tableWidget.setCornerButtonEnabled(True)
        self.prof_my_classes_tableWidget.setObjectName(
            "prof_my_classes_tableWidget")
        self.prof_my_classes_tableWidget.setColumnCount(5)
        self.prof_my_classes_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prof_my_classes_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_my_classes_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_my_classes_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_my_classes_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_my_classes_tableWidget.setHorizontalHeaderItem(4, item)
        self.prof_my_classes_page_utlogo = QtWidgets.QLabel(
            prof_my_classes_page)
        self.prof_my_classes_page_utlogo.setGeometry(
            QtCore.QRect(420, 20, 111, 111))
        self.prof_my_classes_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.prof_my_classes_page_utlogo.setText("")
        self.prof_my_classes_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.prof_my_classes_page_utlogo.setObjectName(
            "prof_my_classes_page_utlogo")
        self.prof_my_classes_page_frame = QtWidgets.QFrame(
            prof_my_classes_page)
        self.prof_my_classes_page_frame.setGeometry(
            QtCore.QRect(10, 9, 521, 421))
        self.prof_my_classes_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_my_classes_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_my_classes_page_frame.setObjectName(
            "prof_my_classes_page_frame")
        self.prof_my_classes_page_frame.raise_()
        self.prof_my_classes_page_button.raise_()
        self.prof_my_classes_page_label.raise_()
        self.prof_my_classes_tableWidget.raise_()
        self.prof_my_classes_page_utlogo.raise_()

        self.retranslateUi(prof_my_classes_page)
        self.prof_my_classes_page_button.accepted.connect(
            prof_my_classes_page.accept)
        self.prof_my_classes_page_button.rejected.connect(
            prof_my_classes_page.reject)
        QtCore.QMetaObject.connectSlotsByName(prof_my_classes_page)

    def retranslateUi(self, prof_my_classes_page):
        _translate = QtCore.QCoreApplication.translate
        prof_my_classes_page.setWindowTitle(
            _translate("prof_my_classes_page", "My Classes"))
        self.prof_my_classes_page_label.setText(
            _translate("prof_my_classes_page", "My Classes"))
        self.prof_my_classes_tableWidget.setSortingEnabled(False)
        item = self.prof_my_classes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("prof_my_classes_page", "Class"))
        item = self.prof_my_classes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("prof_my_classes_page", "Credit"))
        item = self.prof_my_classes_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("prof_my_classes_page", "Students"))
        item = self.prof_my_classes_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("prof_my_classes_page", "Class Schedule"))
        item = self.prof_my_classes_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("prof_my_classes_page", "Exam Date"))


class Ui_prof_class_request_page(object):
    def setupUi(self, prof_class_request_page):
        prof_class_request_page.setObjectName("prof_class_request_page")
        prof_class_request_page.resize(480, 440)
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
        prof_class_request_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_class_request_page.setWindowIcon(icon)
        self.prof_class_request_button = QtWidgets.QDialogButtonBox(
            prof_class_request_page)
        self.prof_class_request_button.setGeometry(
            QtCore.QRect(370, 390, 80, 25))
        self.prof_class_request_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_class_request_button.setOrientation(QtCore.Qt.Horizontal)
        self.prof_class_request_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel)
        self.prof_class_request_button.setObjectName(
            "prof_class_request_button")
        self.prof_class_request_frame = QtWidgets.QFrame(
            prof_class_request_page)
        self.prof_class_request_frame.setGeometry(
            QtCore.QRect(10, 10, 461, 421))
        self.prof_class_request_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_class_request_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_class_request_frame.setObjectName("prof_class_request_frame")
        self.prof_class_request_page_utlogo = QtWidgets.QLabel(
            self.prof_class_request_frame)
        self.prof_class_request_page_utlogo.setGeometry(
            QtCore.QRect(360, 10, 111, 111))
        self.prof_class_request_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.prof_class_request_page_utlogo.setText("")
        self.prof_class_request_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.prof_class_request_page_utlogo.setObjectName(
            "prof_class_request_page_utlogo")
        self.widget = QtWidgets.QWidget(self.prof_class_request_frame)
        self.widget.setGeometry(QtCore.QRect(20, 131, 421, 201))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.prof_class_request_page_label = QtWidgets.QLabel(self.widget)
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
        self.prof_class_request_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_request_page_label.setFont(font)
        self.prof_class_request_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_class_request_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_class_request_page_label.setObjectName(
            "prof_class_request_page_label")
        self.gridLayout_3.addWidget(
            self.prof_class_request_page_label, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.prof_class_request_class_name_label = QtWidgets.QLabel(
            self.widget)
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
        self.prof_class_request_class_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_request_class_name_label.setFont(font)
        self.prof_class_request_class_name_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_class_request_class_name_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_class_request_class_name_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_class_request_class_name_label.setObjectName(
            "prof_class_request_class_name_label")
        self.gridLayout.addWidget(
            self.prof_class_request_class_name_label, 0, 0, 1, 1)
        self.prof_class_request_exam_date_label_2 = QtWidgets.QLabel(
            self.widget)
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
        self.prof_class_request_exam_date_label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_request_exam_date_label_2.setFont(font)
        self.prof_class_request_exam_date_label_2.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_class_request_exam_date_label_2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_class_request_exam_date_label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_class_request_exam_date_label_2.setObjectName(
            "prof_class_request_exam_date_label_2")
        self.gridLayout.addWidget(
            self.prof_class_request_exam_date_label_2, 1, 0, 1, 1)
        self.prof_class_request_schedule_label = QtWidgets.QLabel(self.widget)
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
        self.prof_class_request_schedule_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_request_schedule_label.setFont(font)
        self.prof_class_request_schedule_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_class_request_schedule_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_class_request_schedule_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_class_request_schedule_label.setObjectName(
            "prof_class_request_schedule_label")
        self.gridLayout.addWidget(
            self.prof_class_request_schedule_label, 2, 0, 1, 1)
        self.prof_class_request_exam_date_label = QtWidgets.QLabel(self.widget)
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
        self.prof_class_request_exam_date_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_request_exam_date_label.setFont(font)
        self.prof_class_request_exam_date_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_class_request_exam_date_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_class_request_exam_date_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_class_request_exam_date_label.setObjectName(
            "prof_class_request_exam_date_label")
        self.gridLayout.addWidget(
            self.prof_class_request_exam_date_label, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.prof_class_request_name_lineEdit = QtWidgets.QLineEdit(
            self.widget)
        self.prof_class_request_name_lineEdit.setObjectName(
            "prof_class_request_name_lineEdit")
        self.gridLayout_2.addWidget(
            self.prof_class_request_name_lineEdit, 0, 0, 1, 1)
        self.prof_class_request_credit_lineEdit = QtWidgets.QLineEdit(
            self.widget)
        self.prof_class_request_credit_lineEdit.setText("")
        self.prof_class_request_credit_lineEdit.setObjectName(
            "prof_class_request_credit_lineEdit")
        self.gridLayout_2.addWidget(
            self.prof_class_request_credit_lineEdit, 1, 0, 1, 1)
        self.prof_class_request_sche_lineEdit = QtWidgets.QLineEdit(
            self.widget)
        self.prof_class_request_sche_lineEdit.setObjectName(
            "prof_class_request_sche_lineEdit")
        self.gridLayout_2.addWidget(
            self.prof_class_request_sche_lineEdit, 2, 0, 1, 1)
        self.prof_class_request_exam_lineEdit = QtWidgets.QLineEdit(
            self.widget)
        self.prof_class_request_exam_lineEdit.setText("")
        self.prof_class_request_exam_lineEdit.setObjectName(
            "prof_class_request_exam_lineEdit")
        self.gridLayout_2.addWidget(
            self.prof_class_request_exam_lineEdit, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.prof_class_request_request_button = QtWidgets.QPushButton(
            self.widget)
        self.prof_class_request_request_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_class_request_request_button.setObjectName(
            "prof_class_request_request_button")
        self.gridLayout_3.addWidget(
            self.prof_class_request_request_button, 2, 1, 1, 1)
        self.prof_class_request_frame.raise_()
        self.prof_class_request_button.raise_()

        self.retranslateUi(prof_class_request_page)
        self.prof_class_request_button.accepted.connect(
            prof_class_request_page.accept)
        self.prof_class_request_button.rejected.connect(
            prof_class_request_page.reject)
        QtCore.QMetaObject.connectSlotsByName(prof_class_request_page)

    def retranslateUi(self, prof_class_request_page):
        _translate = QtCore.QCoreApplication.translate
        prof_class_request_page.setWindowTitle(
            _translate("prof_class_request_page", "Class Request"))
        self.prof_class_request_page_label.setText(
            _translate("prof_class_request_page", "Class Request"))
        self.prof_class_request_class_name_label.setText(
            _translate("prof_class_request_page", "Class:"))
        self.prof_class_request_exam_date_label_2.setText(
            _translate("prof_class_request_page", "Credit:"))
        self.prof_class_request_schedule_label.setText(
            _translate("prof_class_request_page", "Schedule:"))
        self.prof_class_request_exam_date_label.setText(
            _translate("prof_class_request_page", "Exam Date:"))
        self.prof_class_request_request_button.setText(
            _translate("prof_class_request_page", "Request"))


class Ui_prof_class_requsts_status_page(object):
    def setupUi(self, prof_class_requsts_status_page):
        prof_class_requsts_status_page.setObjectName(
            "prof_class_requsts_status_page")
        prof_class_requsts_status_page.resize(542, 433)
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
        prof_class_requsts_status_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_class_requsts_status_page.setWindowIcon(icon)
        self.prof_class_requsts_status_page_frame = QtWidgets.QFrame(
            prof_class_requsts_status_page)
        self.prof_class_requsts_status_page_frame.setGeometry(
            QtCore.QRect(10, 10, 521, 411))
        self.prof_class_requsts_status_page_frame.setFrameShape(
            QtWidgets.QFrame.Box)
        self.prof_class_requsts_status_page_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.prof_class_requsts_status_page_frame.setObjectName(
            "prof_class_requsts_status_page_frame")
        self.prof_class_requsts_status_page_tableWidget = QtWidgets.QTableWidget(
            self.prof_class_requsts_status_page_frame)
        self.prof_class_requsts_status_page_tableWidget.setGeometry(
            QtCore.QRect(10, 120, 501, 251))
        self.prof_class_requsts_status_page_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.prof_class_requsts_status_page_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.prof_class_requsts_status_page_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prof_class_requsts_status_page_tableWidget.setDragEnabled(True)
        self.prof_class_requsts_status_page_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.prof_class_requsts_status_page_tableWidget.setShowGrid(True)
        self.prof_class_requsts_status_page_tableWidget.setGridStyle(
            QtCore.Qt.SolidLine)
        self.prof_class_requsts_status_page_tableWidget.setWordWrap(True)
        self.prof_class_requsts_status_page_tableWidget.setCornerButtonEnabled(
            True)
        self.prof_class_requsts_status_page_tableWidget.setObjectName(
            "prof_class_requsts_status_page_tableWidget")
        self.prof_class_requsts_status_page_tableWidget.setColumnCount(5)
        self.prof_class_requsts_status_page_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prof_class_requsts_status_page_tableWidget.setHorizontalHeaderItem(
            0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_class_requsts_status_page_tableWidget.setHorizontalHeaderItem(
            1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_class_requsts_status_page_tableWidget.setHorizontalHeaderItem(
            2, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_class_requsts_status_page_tableWidget.setHorizontalHeaderItem(
            3, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_class_requsts_status_page_tableWidget.setHorizontalHeaderItem(
            4, item)
        self.prof_class_requsts_status_page_buttonBox = QtWidgets.QDialogButtonBox(
            self.prof_class_requsts_status_page_frame)
        self.prof_class_requsts_status_page_buttonBox.setGeometry(
            QtCore.QRect(430, 380, 80, 25))
        self.prof_class_requsts_status_page_buttonBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_class_requsts_status_page_buttonBox.setOrientation(
            QtCore.Qt.Horizontal)
        self.prof_class_requsts_status_page_buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel)
        self.prof_class_requsts_status_page_buttonBox.setObjectName(
            "prof_class_requsts_status_page_buttonBox")
        self.prof_class_requsts_status_page_label = QtWidgets.QLabel(
            prof_class_requsts_status_page)
        self.prof_class_requsts_status_page_label.setGeometry(
            QtCore.QRect(20, 90, 391, 38))
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
        self.prof_class_requsts_status_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_class_requsts_status_page_label.setFont(font)
        self.prof_class_requsts_status_page_label.setFrameShape(
            QtWidgets.QFrame.Box)
        self.prof_class_requsts_status_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.prof_class_requsts_status_page_label.setObjectName(
            "prof_class_requsts_status_page_label")
        self.prof_class_requsts_status_page_utlogo = QtWidgets.QLabel(
            prof_class_requsts_status_page)
        self.prof_class_requsts_status_page_utlogo.setGeometry(
            QtCore.QRect(420, 10, 111, 111))
        self.prof_class_requsts_status_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.prof_class_requsts_status_page_utlogo.setText("")
        self.prof_class_requsts_status_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.prof_class_requsts_status_page_utlogo.setObjectName(
            "prof_class_requsts_status_page_utlogo")

        self.retranslateUi(prof_class_requsts_status_page)
        self.prof_class_requsts_status_page_buttonBox.accepted.connect(
            prof_class_requsts_status_page.accept)
        self.prof_class_requsts_status_page_buttonBox.rejected.connect(
            prof_class_requsts_status_page.reject)
        QtCore.QMetaObject.connectSlotsByName(prof_class_requsts_status_page)

    def retranslateUi(self, prof_class_requsts_status_page):
        _translate = QtCore.QCoreApplication.translate
        prof_class_requsts_status_page.setWindowTitle(_translate(
            "prof_class_requsts_status_page", "Class Reguests Status"))
        self.prof_class_requsts_status_page_tableWidget.setSortingEnabled(
            False)
        item = self.prof_class_requsts_status_page_tableWidget.horizontalHeaderItem(
            0)
        item.setText(_translate("prof_class_requsts_status_page", "Status"))
        item = self.prof_class_requsts_status_page_tableWidget.horizontalHeaderItem(
            1)
        item.setText(_translate("prof_class_requsts_status_page", "Class"))
        item = self.prof_class_requsts_status_page_tableWidget.horizontalHeaderItem(
            2)
        item.setText(_translate("prof_class_requsts_status_page", "Credit"))
        item = self.prof_class_requsts_status_page_tableWidget.horizontalHeaderItem(
            3)
        item.setText(_translate(
            "prof_class_requsts_status_page", "Class Schedule"))
        item = self.prof_class_requsts_status_page_tableWidget.horizontalHeaderItem(
            4)
        item.setText(_translate("prof_class_requsts_status_page", "Exam Date"))
        self.prof_class_requsts_status_page_label.setText(
            _translate("prof_class_requsts_status_page", "Class Requests"))


class Ui_prof_students_page(object):
    def setupUi(self, prof_students_page):
        prof_students_page.setObjectName("prof_students_page")
        prof_students_page.resize(374, 490)
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
        prof_students_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_students_page.setWindowIcon(icon)
        self.prof_students_frame = QtWidgets.QFrame(prof_students_page)
        self.prof_students_frame.setGeometry(QtCore.QRect(10, 10, 351, 471))
        self.prof_students_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_students_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_students_frame.setObjectName("prof_students_frame")
        self.prof_students_page_utlogo = QtWidgets.QLabel(
            self.prof_students_frame)
        self.prof_students_page_utlogo.setGeometry(
            QtCore.QRect(240, 10, 111, 111))
        self.prof_students_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.prof_students_page_utlogo.setText("")
        self.prof_students_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.prof_students_page_utlogo.setObjectName(
            "prof_students_page_utlogo")
        self.prof_students_tableWidget = QtWidgets.QTableWidget(
            self.prof_students_frame)
        self.prof_students_tableWidget.setGeometry(
            QtCore.QRect(10, 190, 331, 231))
        self.prof_students_tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.prof_students_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.prof_students_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prof_students_tableWidget.setDragEnabled(True)
        self.prof_students_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.prof_students_tableWidget.setShowGrid(True)
        self.prof_students_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.prof_students_tableWidget.setWordWrap(True)
        self.prof_students_tableWidget.setCornerButtonEnabled(True)
        self.prof_students_tableWidget.setObjectName(
            "prof_students_tableWidget")
        self.prof_students_tableWidget.setColumnCount(3)
        self.prof_students_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prof_students_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_students_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prof_students_tableWidget.setHorizontalHeaderItem(2, item)
        self.prof_students_button = QtWidgets.QDialogButtonBox(
            self.prof_students_frame)
        self.prof_students_button.setGeometry(QtCore.QRect(260, 430, 80, 25))
        self.prof_students_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_students_button.setOrientation(QtCore.Qt.Horizontal)
        self.prof_students_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.prof_students_button.setObjectName("prof_students_button")
        self.prof_students_page_label = QtWidgets.QLabel(
            self.prof_students_frame)
        self.prof_students_page_label.setGeometry(
            QtCore.QRect(10, 80, 231, 38))
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
        self.prof_students_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_students_page_label.setFont(font)
        self.prof_students_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_students_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_students_page_label.setObjectName("prof_students_page_label")
        self.layoutWidget = QtWidgets.QWidget(self.prof_students_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 125, 331, 59))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.prof_students_class_name_label = QtWidgets.QLabel(
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
        self.prof_students_class_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_students_class_name_label.setFont(font)
        self.prof_students_class_name_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_students_class_name_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_students_class_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_students_class_name_label.setObjectName(
            "prof_students_class_name_label")
        self.gridLayout.addWidget(
            self.prof_students_class_name_label, 0, 0, 1, 1)
        self.prof_students_class_name_comboBox = QtWidgets.QComboBox(
            self.layoutWidget)
        self.prof_students_class_name_comboBox.setObjectName(
            "prof_students_class_name_comboBox")
        self.gridLayout.addWidget(
            self.prof_students_class_name_comboBox, 0, 1, 1, 1)
        self.prof_students_show_button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.prof_students_show_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_students_show_button.setObjectName(
            "prof_students_show_button")
        self.gridLayout.addWidget(self.prof_students_show_button, 1, 1, 1, 1)

        self.retranslateUi(prof_students_page)
        self.prof_students_button.accepted.connect(prof_students_page.accept)
        self.prof_students_button.rejected.connect(prof_students_page.reject)
        QtCore.QMetaObject.connectSlotsByName(prof_students_page)

    def retranslateUi(self, prof_students_page):
        _translate = QtCore.QCoreApplication.translate
        prof_students_page.setWindowTitle(
            _translate("prof_students_page", "Students"))
        self.prof_students_tableWidget.setSortingEnabled(False)
        item = self.prof_students_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("prof_students_page", "Student ID"))
        item = self.prof_students_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("prof_students_page", "Name"))
        item = self.prof_students_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("prof_students_page", "Field"))
        self.prof_students_page_label.setText(
            _translate("prof_students_page", "Students"))
        self.prof_students_class_name_label.setText(
            _translate("prof_students_page", "Class:"))
        self.prof_students_show_button.setText(
            _translate("prof_students_page", "Show"))


class Ui_prof_submit_grades_page(object):
    def setupUi(self, prof_submit_grades_page):
        prof_submit_grades_page.setObjectName("prof_submit_grades_page")
        prof_submit_grades_page.resize(480, 440)
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
        prof_submit_grades_page.setPalette(palette)
        prof_submit_grades_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prof_submit_grades_page.setWindowIcon(icon)
        self.prof_submit_grades_frame = QtWidgets.QFrame(
            prof_submit_grades_page)
        self.prof_submit_grades_frame.setGeometry(
            QtCore.QRect(10, 10, 461, 421))
        self.prof_submit_grades_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_submit_grades_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_submit_grades_frame.setObjectName("prof_submit_grades_frame")
        self.prof_submit_grades_page_utlogo = QtWidgets.QLabel(
            self.prof_submit_grades_frame)
        self.prof_submit_grades_page_utlogo.setGeometry(
            QtCore.QRect(360, 10, 111, 111))
        self.prof_submit_grades_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.prof_submit_grades_page_utlogo.setText("")
        self.prof_submit_grades_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.prof_submit_grades_page_utlogo.setObjectName(
            "prof_submit_grades_page_utlogo")
        self.layoutWidget = QtWidgets.QWidget(self.prof_submit_grades_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 131, 421, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.prof_submit_grades_student_id_comboBox = QtWidgets.QComboBox(
            self.layoutWidget)
        self.prof_submit_grades_student_id_comboBox.setObjectName(
            "prof_submit_grades_student_id_comboBox")
        self.gridLayout.addWidget(
            self.prof_submit_grades_student_id_comboBox, 3, 1, 1, 1)
        self.prof_submit_grades_page_label = QtWidgets.QLabel(
            self.layoutWidget)
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
        self.prof_submit_grades_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.prof_submit_grades_page_label.setFont(font)
        self.prof_submit_grades_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_submit_grades_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_submit_grades_page_label.setObjectName(
            "prof_submit_grades_page_label")
        self.gridLayout.addWidget(
            self.prof_submit_grades_page_label, 0, 0, 1, 2)
        self.prof_submit_grades_ID_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.prof_submit_grades_ID_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_submit_grades_ID_label.setFont(font)
        self.prof_submit_grades_ID_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.prof_submit_grades_ID_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_submit_grades_ID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_submit_grades_ID_label.setObjectName(
            "prof_submit_grades_ID_label")
        self.gridLayout.addWidget(self.prof_submit_grades_ID_label, 3, 0, 1, 1)
        self.prof_submit_grades_grade_label = QtWidgets.QLabel(
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
        self.prof_submit_grades_grade_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_submit_grades_grade_label.setFont(font)
        self.prof_submit_grades_grade_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_submit_grades_grade_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_submit_grades_grade_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_submit_grades_grade_label.setObjectName(
            "prof_submit_grades_grade_label")
        self.gridLayout.addWidget(
            self.prof_submit_grades_grade_label, 4, 0, 1, 1)
        self.prof_submit_grades_grade_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget)
        self.prof_submit_grades_grade_lineEdit.setObjectName(
            "prof_submit_grades_grade_lineEdit")
        self.gridLayout.addWidget(
            self.prof_submit_grades_grade_lineEdit, 4, 1, 1, 1)
        self.prof_submit_grades_submit_button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.prof_submit_grades_submit_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_submit_grades_submit_button.setObjectName(
            "prof_submit_grades_submit_button")
        self.gridLayout.addWidget(
            self.prof_submit_grades_submit_button, 6, 1, 1, 1)
        self.prof_submit_grades_class_name_comboBox = QtWidgets.QComboBox(
            self.layoutWidget)
        self.prof_submit_grades_class_name_comboBox.setObjectName(
            "prof_submit_grades_class_name_comboBox")
        self.gridLayout.addWidget(
            self.prof_submit_grades_class_name_comboBox, 1, 1, 1, 1)
        self.prof_submit_grades_class_label = QtWidgets.QLabel(
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
        self.prof_submit_grades_class_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prof_submit_grades_class_label.setFont(font)
        self.prof_submit_grades_class_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.prof_submit_grades_class_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.prof_submit_grades_class_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.prof_submit_grades_class_label.setObjectName(
            "prof_submit_grades_class_label")
        self.gridLayout.addWidget(
            self.prof_submit_grades_class_label, 1, 0, 1, 1)
        self.prof_submit_grades_button = QtWidgets.QDialogButtonBox(
            self.prof_submit_grades_frame)
        self.prof_submit_grades_button.setGeometry(
            QtCore.QRect(360, 380, 80, 25))
        self.prof_submit_grades_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_submit_grades_button.setOrientation(QtCore.Qt.Horizontal)
        self.prof_submit_grades_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel)
        self.prof_submit_grades_button.setObjectName(
            "prof_submit_grades_button")

        self.retranslateUi(prof_submit_grades_page)
        self.prof_submit_grades_button.accepted.connect(
            prof_submit_grades_page.accept)
        self.prof_submit_grades_button.rejected.connect(
            prof_submit_grades_page.reject)
        QtCore.QMetaObject.connectSlotsByName(prof_submit_grades_page)

    def retranslateUi(self, prof_submit_grades_page):
        _translate = QtCore.QCoreApplication.translate
        prof_submit_grades_page.setWindowTitle(
            _translate("prof_submit_grades_page", "Submit Grades"))
        self.prof_submit_grades_page_label.setText(
            _translate("prof_submit_grades_page", "Submit Grades"))
        self.prof_submit_grades_ID_label.setText(
            _translate("prof_submit_grades_page", "Student ID:"))
        self.prof_submit_grades_grade_label.setText(
            _translate("prof_submit_grades_page", "Grade:"))
        self.prof_submit_grades_submit_button.setText(
            _translate("prof_submit_grades_page", "Submit"))
        self.prof_submit_grades_class_label.setText(
            _translate("prof_submit_grades_page", "Class:"))
