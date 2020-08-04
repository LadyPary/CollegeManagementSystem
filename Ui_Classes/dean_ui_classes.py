from PyQt5 import QtCore, QtGui, QtWidgets

# Classes in this file was created by PyQt Designer.
# These create the base of QMainWindow and Qdialogs
# used to show infomation about the dean.


class Ui_dean_main_page(object):
    def setupUi(self, dean_main_page):
        dean_main_page.setObjectName("dean_main_page")
        dean_main_page.resize(480, 426)
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
        dean_main_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_main_page.setWindowIcon(icon)
        self.dean_main_page_centralwidget = QtWidgets.QWidget(dean_main_page)
        self.dean_main_page_centralwidget.setObjectName(
            "dean_main_page_centralwidget")
        self.dean_main_page_frame = QtWidgets.QFrame(
            self.dean_main_page_centralwidget)
        self.dean_main_page_frame.setGeometry(QtCore.QRect(9, 9, 461, 381))
        self.dean_main_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_main_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dean_main_page_frame.setObjectName("dean_main_page_frame")
        self.dean_main_page_welcome_label = QtWidgets.QLabel(
            self.dean_main_page_frame)
        self.dean_main_page_welcome_label.setGeometry(
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
        self.dean_main_page_welcome_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_main_page_welcome_label.setFont(font)
        self.dean_main_page_welcome_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_main_page_welcome_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.dean_main_page_welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_main_page_welcome_label.setObjectName(
            "dean_main_page_welcome_label")
        self.dean_main_page_quote_title_label = QtWidgets.QLabel(
            self.dean_main_page_frame)
        self.dean_main_page_quote_title_label.setGeometry(
            QtCore.QRect(10, 160, 171, 31))
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
        self.dean_main_page_quote_title_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.dean_main_page_quote_title_label.setFont(font)
        self.dean_main_page_quote_title_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_main_page_quote_title_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.dean_main_page_quote_title_label.setObjectName(
            "dean_main_page_quote_title_label")
        self.dean_main_page_quote_body_label = QtWidgets.QLabel(
            self.dean_main_page_frame)
        self.dean_main_page_quote_body_label.setGeometry(
            QtCore.QRect(10, 200, 441, 181))
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
        self.dean_main_page_quote_body_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(12)
        self.dean_main_page_quote_body_label.setFont(font)
        self.dean_main_page_quote_body_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dean_main_page_quote_body_label.setObjectName(
            "dean_main_page_quote_body_label")
        self.dean_main_page_name_label = QtWidgets.QLabel(
            self.dean_main_page_frame)
        self.dean_main_page_name_label.setGeometry(
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
        self.dean_main_page_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(14)
        self.dean_main_page_name_label.setFont(font)
        self.dean_main_page_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_main_page_name_label.setObjectName(
            "dean_main_page_name_label")
        self.dean_main_page_utlogo = QtWidgets.QLabel(
            self.dean_main_page_centralwidget)
        self.dean_main_page_utlogo.setGeometry(QtCore.QRect(350, 10, 111, 111))
        self.dean_main_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.dean_main_page_utlogo.setText("")
        self.dean_main_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.dean_main_page_utlogo.setObjectName("dean_main_page_utlogo")
        dean_main_page.setCentralWidget(self.dean_main_page_centralwidget)
        self.dean_main_page_menu_bar = QtWidgets.QMenuBar(dean_main_page)
        self.dean_main_page_menu_bar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.dean_main_page_menu_bar.setObjectName("dean_main_page_menu_bar")
        self.dean_main_page_menu_Management = QtWidgets.QMenu(
            self.dean_main_page_menu_bar)
        self.dean_main_page_menu_Management.setObjectName(
            "dean_main_page_menu_Management")
        self.dean_main_page_menu_Academics = QtWidgets.QMenu(
            self.dean_main_page_menu_Management)
        self.dean_main_page_menu_Academics.setObjectName(
            "dean_main_page_menu_Academics")
        self.dean_main_page_menu_Students = QtWidgets.QMenu(
            self.dean_main_page_menu_Academics)
        self.dean_main_page_menu_Students.setObjectName(
            "dean_main_page_menu_Students")
        self.dean_main_page_menu_Professors = QtWidgets.QMenu(
            self.dean_main_page_menu_Academics)
        self.dean_main_page_menu_Professors.setObjectName(
            "dean_main_page_menu_Professors")
        self.dean_main_page_menu_Requests = QtWidgets.QMenu(
            self.dean_main_page_menu_Management)
        self.dean_main_page_menu_Requests.setObjectName(
            "dean_main_page_menu_Requests")
        self.dean_main_page_menu_Profile = QtWidgets.QMenu(
            self.dean_main_page_menu_bar)
        self.dean_main_page_menu_Profile.setObjectName(
            "dean_main_page_menu_Profile")
        dean_main_page.setMenuBar(self.dean_main_page_menu_bar)
        self.dean_main_page_action_Edit_Profile = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_Edit_Profile.setObjectName(
            "dean_main_page_action_Edit_Profile")
        self.dean_main_page_action_Change_Password = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_Change_Password.setObjectName(
            "dean_main_page_action_Change_Password")
        self.dean_main_page_action_Sign_Out = QtWidgets.QAction(dean_main_page)
        self.dean_main_page_action_Sign_Out.setObjectName(
            "dean_main_page_action_Sign_Out")
        self.actionStudents = QtWidgets.QAction(dean_main_page)
        self.actionStudents.setObjectName("actionStudents")
        self.actionClasses = QtWidgets.QAction(dean_main_page)
        self.actionClasses.setObjectName("actionClasses")
        self.dean_main_page_action_Student_Request = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_Student_Request.setObjectName(
            "dean_main_page_action_Student_Request")
        self.dean_main_page_action_Class_Request = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_Class_Request.setObjectName(
            "dean_main_page_action_Class_Request")
        self.dean_main_page_action_All_Students = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_All_Students.setObjectName(
            "dean_main_page_action_All_Students")
        self.dean_main_page_action_Top_Students = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_Top_Students.setObjectName(
            "dean_main_page_action_Top_Students")
        self.dean_main_page_action_Classes = QtWidgets.QAction(dean_main_page)
        self.dean_main_page_action_Classes.setObjectName(
            "dean_main_page_action_Classes")
        self.dean_main_page_action_All_Professors = QtWidgets.QAction(
            dean_main_page)
        self.dean_main_page_action_All_Professors.setObjectName(
            "dean_main_page_action_All_Professors")
        self.adean_main_page_action_Top_Professors = QtWidgets.QAction(
            dean_main_page)
        self.adean_main_page_action_Top_Professors.setObjectName(
            "adean_main_page_action_Top_Professors")
        self.dean_main_page_menu_Students.addAction(
            self.dean_main_page_action_All_Students)
        self.dean_main_page_menu_Students.addAction(
            self.dean_main_page_action_Top_Students)
        self.dean_main_page_menu_Professors.addAction(
            self.dean_main_page_action_All_Professors)
        self.dean_main_page_menu_Professors.addAction(
            self.adean_main_page_action_Top_Professors)
        self.dean_main_page_menu_Academics.addAction(
            self.dean_main_page_menu_Professors.menuAction())
        self.dean_main_page_menu_Academics.addAction(
            self.dean_main_page_menu_Students.menuAction())
        self.dean_main_page_menu_Academics.addAction(
            self.dean_main_page_action_Classes)
        self.dean_main_page_menu_Requests.addAction(
            self.dean_main_page_action_Student_Request)
        self.dean_main_page_menu_Requests.addAction(
            self.dean_main_page_action_Class_Request)
        self.dean_main_page_menu_Management.addAction(
            self.dean_main_page_menu_Academics.menuAction())
        self.dean_main_page_menu_Management.addAction(
            self.dean_main_page_menu_Requests.menuAction())
        self.dean_main_page_menu_Profile.addAction(
            self.dean_main_page_action_Edit_Profile)
        self.dean_main_page_menu_Profile.addAction(
            self.dean_main_page_action_Change_Password)
        self.dean_main_page_menu_Profile.addSeparator()
        self.dean_main_page_menu_Profile.addAction(
            self.dean_main_page_action_Sign_Out)
        self.dean_main_page_menu_bar.addAction(
            self.dean_main_page_menu_Management.menuAction())
        self.dean_main_page_menu_bar.addAction(
            self.dean_main_page_menu_Profile.menuAction())

        self.retranslateUi(dean_main_page)
        QtCore.QMetaObject.connectSlotsByName(dean_main_page)

    def retranslateUi(self, dean_main_page):
        _translate = QtCore.QCoreApplication.translate
        dean_main_page.setWindowTitle(
            _translate("dean_main_page", "Main Page"))
        self.dean_main_page_welcome_label.setText(
            _translate("dean_main_page", "Welcome"))
        self.dean_main_page_quote_title_label.setText(
            _translate("dean_main_page", "Quote of the day:"))
        self.dean_main_page_quote_body_label.setText(_translate("dean_main_page", "\"The key to life is accepting challenges.\n"
                                                                " Once someone stops doing this, he\'s dead.\" \n"
                                                                "-Bette Davis"))
        self.dean_main_page_name_label.setText(
            _translate("dean_main_page", "**Name of Dean**"))
        self.dean_main_page_menu_Management.setTitle(
            _translate("dean_main_page", "Ma&nagement"))
        self.dean_main_page_menu_Academics.setTitle(
            _translate("dean_main_page", "&Academics"))
        self.dean_main_page_menu_Students.setTitle(
            _translate("dean_main_page", "&Students"))
        self.dean_main_page_menu_Professors.setTitle(
            _translate("dean_main_page", "&Professors"))
        self.dean_main_page_menu_Requests.setTitle(
            _translate("dean_main_page", "&Requests"))
        self.dean_main_page_menu_Profile.setTitle(
            _translate("dean_main_page", "Profi&le"))
        self.dean_main_page_action_Edit_Profile.setText(
            _translate("dean_main_page", "&Edit Profile"))
        self.dean_main_page_action_Change_Password.setText(
            _translate("dean_main_page", "&Change Password"))
        self.dean_main_page_action_Sign_Out.setText(
            _translate("dean_main_page", "&Sign Out"))
        self.actionStudents.setText(_translate("dean_main_page", "Students"))
        self.actionClasses.setText(_translate("dean_main_page", "Classes"))
        self.dean_main_page_action_Student_Request.setText(
            _translate("dean_main_page", "&New Student Request"))
        self.dean_main_page_action_Class_Request.setText(
            _translate("dean_main_page", "New &Class Request"))
        self.dean_main_page_action_All_Students.setText(
            _translate("dean_main_page", "&All Students"))
        self.dean_main_page_action_Top_Students.setText(
            _translate("dean_main_page", "&Top Students"))
        self.dean_main_page_action_Classes.setText(
            _translate("dean_main_page", "&Classes"))
        self.dean_main_page_action_All_Professors.setText(
            _translate("dean_main_page", "All Professors"))
        self.adean_main_page_action_Top_Professors.setText(
            _translate("dean_main_page", "Top Professors"))


class Ui_dean_students_page(object):
    def setupUi(self, dean_students_page):
        dean_students_page.setObjectName("dean_students_page")
        dean_students_page.resize(329, 440)
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
        dean_students_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_students_page.setWindowIcon(icon)
        self.dean_students_frame = QtWidgets.QFrame(dean_students_page)
        self.dean_students_frame.setGeometry(QtCore.QRect(4, 10, 321, 421))
        self.dean_students_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_students_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dean_students_frame.setObjectName("dean_students_frame")
        self.dean_students_page_utlogo = QtWidgets.QLabel(
            self.dean_students_frame)
        self.dean_students_page_utlogo.setGeometry(
            QtCore.QRect(200, 10, 111, 111))
        self.dean_students_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.dean_students_page_utlogo.setText("")
        self.dean_students_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.dean_students_page_utlogo.setObjectName(
            "dean_students_page_utlogo")
        self.dean_students_tableWidget = QtWidgets.QTableWidget(
            self.dean_students_frame)
        self.dean_students_tableWidget.setGeometry(
            QtCore.QRect(10, 120, 301, 261))
        self.dean_students_tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dean_students_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_students_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_students_tableWidget.setDragEnabled(True)
        self.dean_students_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_students_tableWidget.setShowGrid(True)
        self.dean_students_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.dean_students_tableWidget.setWordWrap(True)
        self.dean_students_tableWidget.setCornerButtonEnabled(True)
        self.dean_students_tableWidget.setObjectName(
            "dean_students_tableWidget")
        self.dean_students_tableWidget.setColumnCount(3)
        self.dean_students_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_students_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_students_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_students_tableWidget.setHorizontalHeaderItem(2, item)
        self.dean_students_buttons = QtWidgets.QDialogButtonBox(
            self.dean_students_frame)
        self.dean_students_buttons.setGeometry(QtCore.QRect(230, 390, 80, 25))
        self.dean_students_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_students_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dean_students_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.dean_students_buttons.setObjectName("dean_students_buttons")
        self.dean_students_page_label = QtWidgets.QLabel(
            self.dean_students_frame)
        self.dean_students_page_label.setGeometry(
            QtCore.QRect(10, 80, 191, 38))
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
        self.dean_students_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_students_page_label.setFont(font)
        self.dean_students_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_students_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_students_page_label.setObjectName("dean_students_page_label")

        self.retranslateUi(dean_students_page)
        self.dean_students_buttons.accepted.connect(dean_students_page.accept)
        self.dean_students_buttons.rejected.connect(dean_students_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_students_page)

    def retranslateUi(self, dean_students_page):
        _translate = QtCore.QCoreApplication.translate
        dean_students_page.setWindowTitle(
            _translate("dean_students_page", "Students"))
        self.dean_students_tableWidget.setSortingEnabled(False)
        item = self.dean_students_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_students_page", "Student ID"))
        item = self.dean_students_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_students_page", "Name"))
        item = self.dean_students_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dean_students_page", "Field"))
        self.dean_students_page_label.setText(
            _translate("dean_students_page", "Students"))


class Ui_dean_profs_page(object):
    def setupUi(self, dean_profs_page):
        dean_profs_page.setObjectName("dean_profs_page")
        dean_profs_page.resize(392, 440)
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
        dean_profs_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_profs_page.setWindowIcon(icon)
        self.dean_profs_frame = QtWidgets.QFrame(dean_profs_page)
        self.dean_profs_frame.setGeometry(QtCore.QRect(10, 10, 371, 421))
        self.dean_profs_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_profs_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dean_profs_frame.setObjectName("dean_profs_frame")
        self.dean_profs_page_utlogo = QtWidgets.QLabel(self.dean_profs_frame)
        self.dean_profs_page_utlogo.setGeometry(
            QtCore.QRect(240, 10, 111, 111))
        self.dean_profs_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.dean_profs_page_utlogo.setText("")
        self.dean_profs_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.dean_profs_page_utlogo.setObjectName("dean_profs_page_utlogo")
        self.dean_profs_tableWidget = QtWidgets.QTableWidget(
            self.dean_profs_frame)
        self.dean_profs_tableWidget.setGeometry(QtCore.QRect(9, 130, 341, 251))
        self.dean_profs_tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dean_profs_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_profs_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_profs_tableWidget.setDragEnabled(True)
        self.dean_profs_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_profs_tableWidget.setShowGrid(True)
        self.dean_profs_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.dean_profs_tableWidget.setWordWrap(True)
        self.dean_profs_tableWidget.setCornerButtonEnabled(True)
        self.dean_profs_tableWidget.setObjectName("dean_profs_tableWidget")
        self.dean_profs_tableWidget.setColumnCount(2)
        self.dean_profs_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_profs_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_profs_tableWidget.setHorizontalHeaderItem(1, item)
        self.dean_profs__button = QtWidgets.QDialogButtonBox(
            self.dean_profs_frame)
        self.dean_profs__button.setGeometry(QtCore.QRect(270, 390, 80, 25))
        self.dean_profs__button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_profs__button.setOrientation(QtCore.Qt.Horizontal)
        self.dean_profs__button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.dean_profs__button.setObjectName("dean_profs__button")
        self.dean_profs_page_label = QtWidgets.QLabel(self.dean_profs_frame)
        self.dean_profs_page_label.setGeometry(QtCore.QRect(10, 90, 231, 38))
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
        self.dean_profs_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_profs_page_label.setFont(font)
        self.dean_profs_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_profs_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_profs_page_label.setObjectName("dean_profs_page_label")

        self.retranslateUi(dean_profs_page)
        self.dean_profs__button.accepted.connect(dean_profs_page.accept)
        self.dean_profs__button.rejected.connect(dean_profs_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_profs_page)

    def retranslateUi(self, dean_profs_page):
        _translate = QtCore.QCoreApplication.translate
        dean_profs_page.setWindowTitle(
            _translate("dean_profs_page", "Professors"))
        self.dean_profs_tableWidget.setSortingEnabled(False)
        item = self.dean_profs_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_profs_page", "Name"))
        item = self.dean_profs_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_profs_page", "Classes"))
        self.dean_profs_page_label.setText(
            _translate("dean_profs_page", "Professors"))


class Ui_dean_classes_page(object):
    def setupUi(self, dean_classes_page):
        dean_classes_page.setObjectName("dean_classes_page")
        dean_classes_page.resize(552, 440)
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
        dean_classes_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_classes_page.setWindowIcon(icon)
        self.dean_classes_tableWidget = QtWidgets.QTableWidget(
            dean_classes_page)
        self.dean_classes_tableWidget.setGeometry(
            QtCore.QRect(20, 130, 511, 261))
        self.dean_classes_tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dean_classes_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_classes_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_classes_tableWidget.setDragEnabled(True)
        self.dean_classes_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_classes_tableWidget.setShowGrid(True)
        self.dean_classes_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.dean_classes_tableWidget.setWordWrap(True)
        self.dean_classes_tableWidget.setCornerButtonEnabled(True)
        self.dean_classes_tableWidget.setObjectName("dean_classes_tableWidget")
        self.dean_classes_tableWidget.setColumnCount(6)
        self.dean_classes_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_classes_tableWidget.setHorizontalHeaderItem(5, item)
        self.dean_classes_page_frame = QtWidgets.QFrame(dean_classes_page)
        self.dean_classes_page_frame.setGeometry(QtCore.QRect(10, 9, 531, 421))
        self.dean_classes_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_classes_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dean_classes_page_frame.setObjectName("dean_classes_page_frame")
        self.dean_classes_button = QtWidgets.QDialogButtonBox(
            self.dean_classes_page_frame)
        self.dean_classes_button.setGeometry(QtCore.QRect(440, 390, 80, 25))
        self.dean_classes_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_classes_button.setOrientation(QtCore.Qt.Horizontal)
        self.dean_classes_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.dean_classes_button.setObjectName("dean_classes_button")
        self.dean_classes_page_utlogo = QtWidgets.QLabel(dean_classes_page)
        self.dean_classes_page_utlogo.setGeometry(
            QtCore.QRect(430, 20, 111, 111))
        self.dean_classes_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.dean_classes_page_utlogo.setText("")
        self.dean_classes_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.dean_classes_page_utlogo.setObjectName("dean_classes_page_utlogo")
        self.dean_classes_page_label = QtWidgets.QLabel(dean_classes_page)
        self.dean_classes_page_label.setGeometry(QtCore.QRect(20, 90, 411, 38))
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
        self.dean_classes_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_classes_page_label.setFont(font)
        self.dean_classes_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_classes_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_classes_page_label.setObjectName("dean_classes_page_label")
        self.dean_classes_page_frame.raise_()
        self.dean_classes_tableWidget.raise_()
        self.dean_classes_page_utlogo.raise_()
        self.dean_classes_page_label.raise_()

        self.retranslateUi(dean_classes_page)
        self.dean_classes_button.accepted.connect(dean_classes_page.accept)
        self.dean_classes_button.rejected.connect(dean_classes_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_classes_page)

    def retranslateUi(self, dean_classes_page):
        _translate = QtCore.QCoreApplication.translate
        dean_classes_page.setWindowTitle(
            _translate("dean_classes_page", "Classes"))
        self.dean_classes_tableWidget.setSortingEnabled(False)
        item = self.dean_classes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_classes_page", "Class"))
        item = self.dean_classes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_classes_page", "Credit"))
        item = self.dean_classes_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dean_classes_page", "Professor"))
        item = self.dean_classes_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dean_classes_page", "Students"))
        item = self.dean_classes_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("dean_classes_page", "Class Schedule"))
        item = self.dean_classes_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("dean_classes_page", "Exam Date"))
        self.dean_classes_page_label.setText(
            _translate("dean_classes_page", " Classes"))


class Ui_dean_top_students_page(object):
    def setupUi(self, dean_top_students_page):
        dean_top_students_page.setObjectName("dean_top_students_page")
        dean_top_students_page.resize(348, 440)
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
        dean_top_students_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_top_students_page.setWindowIcon(icon)
        self.dean_top_students_button = QtWidgets.QDialogButtonBox(
            dean_top_students_page)
        self.dean_top_students_button.setGeometry(
            QtCore.QRect(240, 390, 80, 25))
        self.dean_top_students_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_top_students_button.setOrientation(QtCore.Qt.Horizontal)
        self.dean_top_students_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.dean_top_students_button.setObjectName("dean_top_students_button")
        self.dean_top_students_page_frame = QtWidgets.QFrame(
            dean_top_students_page)
        self.dean_top_students_page_frame.setGeometry(
            QtCore.QRect(10, 9, 321, 421))
        self.dean_top_students_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_top_students_page_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.dean_top_students_page_frame.setObjectName(
            "dean_top_students_page_frame")
        self.dean_top_students_tableWidget = QtWidgets.QTableWidget(
            self.dean_top_students_page_frame)
        self.dean_top_students_tableWidget.setGeometry(
            QtCore.QRect(10, 130, 301, 241))
        self.dean_top_students_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_top_students_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_top_students_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_top_students_tableWidget.setDragEnabled(True)
        self.dean_top_students_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_top_students_tableWidget.setShowGrid(True)
        self.dean_top_students_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.dean_top_students_tableWidget.setWordWrap(True)
        self.dean_top_students_tableWidget.setCornerButtonEnabled(True)
        self.dean_top_students_tableWidget.setObjectName(
            "dean_top_students_tableWidget")
        self.dean_top_students_tableWidget.setColumnCount(3)
        self.dean_top_students_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_students_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_students_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_students_tableWidget.setHorizontalHeaderItem(2, item)
        self.dean_top_students_page_utlogo = QtWidgets.QLabel(
            self.dean_top_students_page_frame)
        self.dean_top_students_page_utlogo.setGeometry(
            QtCore.QRect(220, 20, 111, 111))
        self.dean_top_students_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.dean_top_students_page_utlogo.setText("")
        self.dean_top_students_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.dean_top_students_page_utlogo.setObjectName(
            "dean_top_students_page_utlogo")
        self.dean_top_students_page_label = QtWidgets.QLabel(
            dean_top_students_page)
        self.dean_top_students_page_label.setGeometry(
            QtCore.QRect(20, 90, 211, 51))
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
        self.dean_top_students_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_top_students_page_label.setFont(font)
        self.dean_top_students_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_top_students_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_top_students_page_label.setObjectName(
            "dean_top_students_page_label")
        self.dean_top_students_page_frame.raise_()
        self.dean_top_students_button.raise_()
        self.dean_top_students_page_label.raise_()

        self.retranslateUi(dean_top_students_page)
        self.dean_top_students_button.accepted.connect(
            dean_top_students_page.accept)
        self.dean_top_students_button.rejected.connect(
            dean_top_students_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_top_students_page)

    def retranslateUi(self, dean_top_students_page):
        _translate = QtCore.QCoreApplication.translate
        dean_top_students_page.setWindowTitle(
            _translate("dean_top_students_page", "Top Students"))
        self.dean_top_students_tableWidget.setSortingEnabled(False)
        item = self.dean_top_students_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_top_students_page", "Student ID"))
        item = self.dean_top_students_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_top_students_page", "Name"))
        item = self.dean_top_students_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dean_top_students_page", "GPA"))
        self.dean_top_students_page_label.setText(
            _translate("dean_top_students_page", "Top Students"))


class Ui_dean_top_profs_page(object):
    def setupUi(self, dean_top_profs_page):
        dean_top_profs_page.setObjectName("dean_top_profs_page")
        dean_top_profs_page.resize(365, 446)
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
        dean_top_profs_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_top_profs_page.setWindowIcon(icon)
        self.dean_top_profs_page_utlogo = QtWidgets.QLabel(dean_top_profs_page)
        self.dean_top_profs_page_utlogo.setGeometry(
            QtCore.QRect(240, 20, 111, 111))
        self.dean_top_profs_page_utlogo.setMinimumSize(QtCore.QSize(111, 111))
        self.dean_top_profs_page_utlogo.setText("")
        self.dean_top_profs_page_utlogo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.dean_top_profs_page_utlogo.setObjectName(
            "dean_top_profs_page_utlogo")
        self.dean_top_profs_page_label = QtWidgets.QLabel(dean_top_profs_page)
        self.dean_top_profs_page_label.setGeometry(
            QtCore.QRect(20, 80, 221, 51))
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
        self.dean_top_profs_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_top_profs_page_label.setFont(font)
        self.dean_top_profs_page_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_top_profs_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dean_top_profs_page_label.setObjectName(
            "dean_top_profs_page_label")
        self.dean_top_profs_page_frame = QtWidgets.QFrame(dean_top_profs_page)
        self.dean_top_profs_page_frame.setGeometry(
            QtCore.QRect(10, 9, 341, 421))
        self.dean_top_profs_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_top_profs_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dean_top_profs_page_frame.setObjectName(
            "dean_top_profs_page_frame")
        self.dean_top_profs_tableWidget = QtWidgets.QTableWidget(
            self.dean_top_profs_page_frame)
        self.dean_top_profs_tableWidget.setGeometry(
            QtCore.QRect(10, 130, 311, 241))
        self.dean_top_profs_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_top_profs_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_top_profs_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_top_profs_tableWidget.setDragEnabled(True)
        self.dean_top_profs_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_top_profs_tableWidget.setShowGrid(True)
        self.dean_top_profs_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.dean_top_profs_tableWidget.setWordWrap(True)
        self.dean_top_profs_tableWidget.setCornerButtonEnabled(True)
        self.dean_top_profs_tableWidget.setObjectName(
            "dean_top_profs_tableWidget")
        self.dean_top_profs_tableWidget.setColumnCount(3)
        self.dean_top_profs_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_profs_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_profs_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_top_profs_tableWidget.setHorizontalHeaderItem(2, item)
        self.dean_top_profs_page_buttonBox = QtWidgets.QDialogButtonBox(
            self.dean_top_profs_page_frame)
        self.dean_top_profs_page_buttonBox.setGeometry(
            QtCore.QRect(240, 380, 80, 25))
        self.dean_top_profs_page_buttonBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_top_profs_page_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dean_top_profs_page_buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.dean_top_profs_page_buttonBox.setObjectName(
            "dean_top_profs_page_buttonBox")
        self.dean_top_profs_page_frame.raise_()
        self.dean_top_profs_page_utlogo.raise_()
        self.dean_top_profs_page_label.raise_()

        self.retranslateUi(dean_top_profs_page)
        self.dean_top_profs_page_buttonBox.accepted.connect(
            dean_top_profs_page.accept)
        self.dean_top_profs_page_buttonBox.rejected.connect(
            dean_top_profs_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_top_profs_page)

    def retranslateUi(self, dean_top_profs_page):
        _translate = QtCore.QCoreApplication.translate
        dean_top_profs_page.setWindowTitle(
            _translate("dean_top_profs_page", "Dialog"))
        self.dean_top_profs_page_label.setText(
            _translate("dean_top_profs_page", "Top Professors"))
        self.dean_top_profs_tableWidget.setSortingEnabled(False)
        item = self.dean_top_profs_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_top_profs_page", "Score"))
        item = self.dean_top_profs_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_top_profs_page", "Name"))
        item = self.dean_top_profs_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dean_top_profs_page", "Class"))


class Ui_dean_new_student_request_page(object):
    def setupUi(self, dean_new_student_request_page):
        dean_new_student_request_page.setObjectName(
            "dean_new_student_request_page")
        dean_new_student_request_page.resize(452, 440)
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
        dean_new_student_request_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_new_student_request_page.setWindowIcon(icon)
        self.dean_new_student_request_frame = QtWidgets.QFrame(
            dean_new_student_request_page)
        self.dean_new_student_request_frame.setGeometry(
            QtCore.QRect(10, 10, 431, 421))
        self.dean_new_student_request_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_new_student_request_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.dean_new_student_request_frame.setObjectName(
            "dean_new_student_request_frame")
        self.dean_new_student_request_page_utlogo = QtWidgets.QLabel(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_page_utlogo.setGeometry(
            QtCore.QRect(320, 10, 111, 111))
        self.dean_new_student_request_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.dean_new_student_request_page_utlogo.setText("")
        self.dean_new_student_request_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.dean_new_student_request_page_utlogo.setObjectName(
            "dean_new_student_request_page_utlogo")
        self.dean_new_student_request_buttons = QtWidgets.QDialogButtonBox(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_buttons.setGeometry(
            QtCore.QRect(290, 380, 80, 25))
        self.dean_new_student_request_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_student_request_buttons.setOrientation(
            QtCore.Qt.Horizontal)
        self.dean_new_student_request_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel)
        self.dean_new_student_request_buttons.setObjectName(
            "dean_new_student_request_buttons")
        self.dean_new_student_request_tableWidget = QtWidgets.QTableWidget(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_tableWidget.setGeometry(
            QtCore.QRect(10, 120, 411, 181))
        self.dean_new_student_request_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_new_student_request_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_new_student_request_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_new_student_request_tableWidget.setDragEnabled(True)
        self.dean_new_student_request_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_new_student_request_tableWidget.setShowGrid(True)
        self.dean_new_student_request_tableWidget.setGridStyle(
            QtCore.Qt.SolidLine)
        self.dean_new_student_request_tableWidget.setWordWrap(True)
        self.dean_new_student_request_tableWidget.setCornerButtonEnabled(True)
        self.dean_new_student_request_tableWidget.setObjectName(
            "dean_new_student_request_tableWidget")
        self.dean_new_student_request_tableWidget.setColumnCount(3)
        self.dean_new_student_request_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_student_request_tableWidget.setHorizontalHeaderItem(
            0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_student_request_tableWidget.setHorizontalHeaderItem(
            1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_student_request_tableWidget.setHorizontalHeaderItem(
            2, item)
        self.dean_new_student_request_page_label = QtWidgets.QLabel(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_page_label.setGeometry(
            QtCore.QRect(10, 80, 305, 38))
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
        self.dean_new_student_request_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_new_student_request_page_label.setFont(font)
        self.dean_new_student_request_page_label.setFrameShape(
            QtWidgets.QFrame.Box)
        self.dean_new_student_request_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.dean_new_student_request_page_label.setObjectName(
            "dean_new_student_request_page_label")
        self.layoutWidget = QtWidgets.QWidget(
            self.dean_new_student_request_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 380, 168, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.dean_new_student_request_gridLayout = QtWidgets.QGridLayout(
            self.layoutWidget)
        self.dean_new_student_request_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dean_new_student_request_gridLayout.setObjectName(
            "dean_new_student_request_gridLayout")
        self.dean_new_student_request_accept_Button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.dean_new_student_request_accept_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_student_request_accept_Button.setObjectName(
            "dean_new_student_request_accept_Button")
        self.dean_new_student_request_gridLayout.addWidget(
            self.dean_new_student_request_accept_Button, 0, 0, 1, 1)
        self.dean_new_student_request_decline_button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.dean_new_student_request_decline_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_student_request_decline_button.setObjectName(
            "dean_new_student_request_decline_button")
        self.dean_new_student_request_gridLayout.addWidget(
            self.dean_new_student_request_decline_button, 0, 1, 1, 1)
        self.dean_new_student_request_id_label = QtWidgets.QLabel(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_id_label.setGeometry(
            QtCore.QRect(10, 310, 171, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.dean_new_student_request_id_label.setFont(font)
        self.dean_new_student_request_id_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_new_student_request_id_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.dean_new_student_request_id_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.dean_new_student_request_id_label.setObjectName(
            "dean_new_student_request_id_label")
        self.dean_new_student_request_note_label = QtWidgets.QLabel(
            self.dean_new_student_request_frame)
        self.dean_new_student_request_note_label.setGeometry(
            QtCore.QRect(190, 310, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setItalic(True)
        self.dean_new_student_request_note_label.setFont(font)
        self.dean_new_student_request_note_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dean_new_student_request_note_label.setObjectName(
            "dean_new_student_request_note_label")

        self.retranslateUi(dean_new_student_request_page)
        self.dean_new_student_request_buttons.accepted.connect(
            dean_new_student_request_page.accept)
        self.dean_new_student_request_buttons.rejected.connect(
            dean_new_student_request_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_new_student_request_page)

    def retranslateUi(self, dean_new_student_request_page):
        _translate = QtCore.QCoreApplication.translate
        dean_new_student_request_page.setWindowTitle(_translate(
            "dean_new_student_request_page", "New Student Request"))
        self.dean_new_student_request_tableWidget.setSortingEnabled(False)
        item = self.dean_new_student_request_tableWidget.horizontalHeaderItem(
            0)
        item.setText(_translate("dean_new_student_request_page", "Student ID"))
        item = self.dean_new_student_request_tableWidget.horizontalHeaderItem(
            1)
        item.setText(_translate("dean_new_student_request_page", "Name"))
        item = self.dean_new_student_request_tableWidget.horizontalHeaderItem(
            2)
        item.setText(_translate("dean_new_student_request_page", "Field"))
        self.dean_new_student_request_page_label.setText(_translate(
            "dean_new_student_request_page", "New Student Request"))
        self.dean_new_student_request_accept_Button.setText(
            _translate("dean_new_student_request_page", "Accept"))
        self.dean_new_student_request_decline_button.setText(
            _translate("dean_new_student_request_page", "Decline"))
        self.dean_new_student_request_id_label.setText(
            _translate("dean_new_student_request_page", "Student ID"))
        self.dean_new_student_request_note_label.setText(_translate("dean_new_student_request_page", "NOTE : Double click on the \n"
                                                                    "student from the table and \n"
                                                                    "then click on accept or \n"
                                                                    "decline."))


class Ui_dean_new_class_request_page(object):
    def setupUi(self, dean_new_class_request_page):
        dean_new_class_request_page.setObjectName(
            "dean_new_class_request_page")
        dean_new_class_request_page.resize(540, 522)
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
        dean_new_class_request_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dean_new_class_request_page.setWindowIcon(icon)
        self.dean_new_class_request_frame = QtWidgets.QFrame(
            dean_new_class_request_page)
        self.dean_new_class_request_frame.setGeometry(
            QtCore.QRect(0, 10, 531, 501))
        self.dean_new_class_request_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.dean_new_class_request_frame.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.dean_new_class_request_frame.setObjectName(
            "dean_new_class_request_frame")
        self.dean_new_class_request_page_utlogo = QtWidgets.QLabel(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_page_utlogo.setGeometry(
            QtCore.QRect(420, 10, 111, 111))
        self.dean_new_class_request_page_utlogo.setMinimumSize(
            QtCore.QSize(111, 111))
        self.dean_new_class_request_page_utlogo.setText("")
        self.dean_new_class_request_page_utlogo.setPixmap(
            QtGui.QPixmap("UT_logo.png"))
        self.dean_new_class_request_page_utlogo.setObjectName(
            "dean_new_class_request_page_utlogo")
        self.dean_new_class_request_tableWidget = QtWidgets.QTableWidget(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_tableWidget.setGeometry(
            QtCore.QRect(10, 140, 501, 211))
        self.dean_new_class_request_tableWidget.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_new_class_request_tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dean_new_class_request_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dean_new_class_request_tableWidget.setDragEnabled(True)
        self.dean_new_class_request_tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.dean_new_class_request_tableWidget.setShowGrid(True)
        self.dean_new_class_request_tableWidget.setGridStyle(
            QtCore.Qt.SolidLine)
        self.dean_new_class_request_tableWidget.setWordWrap(True)
        self.dean_new_class_request_tableWidget.setCornerButtonEnabled(True)
        self.dean_new_class_request_tableWidget.setObjectName(
            "dean_new_class_request_tableWidget")
        self.dean_new_class_request_tableWidget.setColumnCount(5)
        self.dean_new_class_request_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_class_request_tableWidget.setHorizontalHeaderItem(
            0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_class_request_tableWidget.setHorizontalHeaderItem(
            1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_class_request_tableWidget.setHorizontalHeaderItem(
            2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_class_request_tableWidget.setHorizontalHeaderItem(
            3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dean_new_class_request_tableWidget.setHorizontalHeaderItem(
            4, item)
        self.dean_new_class_request_page_label = QtWidgets.QLabel(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_page_label.setGeometry(
            QtCore.QRect(10, 80, 411, 51))
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
        self.dean_new_class_request_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dean_new_class_request_page_label.setFont(font)
        self.dean_new_class_request_page_label.setFrameShape(
            QtWidgets.QFrame.Box)
        self.dean_new_class_request_page_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.dean_new_class_request_page_label.setObjectName(
            "dean_new_class_request_page_label")
        self.layoutWidget = QtWidgets.QWidget(
            self.dean_new_class_request_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 460, 221, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.dean_new_class_request_gridLayout = QtWidgets.QGridLayout(
            self.layoutWidget)
        self.dean_new_class_request_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dean_new_class_request_gridLayout.setObjectName(
            "dean_new_class_request_gridLayout")
        self.dean_new_class_request_decline_button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.dean_new_class_request_decline_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_class_request_decline_button.setObjectName(
            "dean_new_class_request_decline_button")
        self.dean_new_class_request_gridLayout.addWidget(
            self.dean_new_class_request_decline_button, 0, 1, 1, 1)
        self.dean_new_class_request_accept_Button = QtWidgets.QPushButton(
            self.layoutWidget)
        self.dean_new_class_request_accept_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_class_request_accept_Button.setObjectName(
            "dean_new_class_request_accept_Button")
        self.dean_new_class_request_gridLayout.addWidget(
            self.dean_new_class_request_accept_Button, 0, 0, 1, 1)
        self.dean_new_class_request_note_label = QtWidgets.QLabel(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_note_label.setGeometry(
            QtCore.QRect(240, 370, 275, 35))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setItalic(True)
        self.dean_new_class_request_note_label.setFont(font)
        self.dean_new_class_request_note_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dean_new_class_request_note_label.setObjectName(
            "dean_new_class_request_note_label")
        self.dean_new_class_request_class_label = QtWidgets.QLabel(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_class_label.setGeometry(
            QtCore.QRect(10, 370, 221, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.dean_new_class_request_class_label.setFont(font)
        self.dean_new_class_request_class_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_new_class_request_class_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.dean_new_class_request_class_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.dean_new_class_request_class_label.setObjectName(
            "dean_new_class_request_class_label")
        self.dean_new_class_request_prof_label = QtWidgets.QLabel(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_prof_label.setGeometry(
            QtCore.QRect(10, 410, 221, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.dean_new_class_request_prof_label.setFont(font)
        self.dean_new_class_request_prof_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.dean_new_class_request_prof_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.dean_new_class_request_prof_label.setAlignment(
            QtCore.Qt.AlignCenter)
        self.dean_new_class_request_prof_label.setObjectName(
            "dean_new_class_request_prof_label")
        self.dean_new_class_request_button = QtWidgets.QDialogButtonBox(
            self.dean_new_class_request_frame)
        self.dean_new_class_request_button.setGeometry(
            QtCore.QRect(430, 470, 80, 25))
        self.dean_new_class_request_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dean_new_class_request_button.setOrientation(QtCore.Qt.Horizontal)
        self.dean_new_class_request_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel)
        self.dean_new_class_request_button.setObjectName(
            "dean_new_class_request_button")

        self.retranslateUi(dean_new_class_request_page)
        self.dean_new_class_request_button.accepted.connect(
            dean_new_class_request_page.accept)
        self.dean_new_class_request_button.rejected.connect(
            dean_new_class_request_page.reject)
        QtCore.QMetaObject.connectSlotsByName(dean_new_class_request_page)

    def retranslateUi(self, dean_new_class_request_page):
        _translate = QtCore.QCoreApplication.translate
        dean_new_class_request_page.setWindowTitle(_translate(
            "dean_new_class_request_page", "New Class Request"))
        self.dean_new_class_request_tableWidget.setSortingEnabled(False)
        item = self.dean_new_class_request_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dean_new_class_request_page", "Class"))
        item = self.dean_new_class_request_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dean_new_class_request_page", "Professor"))
        item = self.dean_new_class_request_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dean_new_class_request_page", "Credit"))
        item = self.dean_new_class_request_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dean_new_class_request_page", "Schedule"))
        item = self.dean_new_class_request_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("dean_new_class_request_page", "Exam Date"))
        self.dean_new_class_request_page_label.setText(
            _translate("dean_new_class_request_page", "New Class Request"))
        self.dean_new_class_request_decline_button.setText(
            _translate("dean_new_class_request_page", "Decline"))
        self.dean_new_class_request_accept_Button.setText(
            _translate("dean_new_class_request_page", "Accept"))
        self.dean_new_class_request_note_label.setText(_translate("dean_new_class_request_page", "NOTE : Double click on the class from the \n"
                                                                  "table and then click on accept or decline."))
        self.dean_new_class_request_class_label.setText(
            _translate("dean_new_class_request_page", "Class"))
        self.dean_new_class_request_prof_label.setText(
            _translate("dean_new_class_request_page", "Professor"))
