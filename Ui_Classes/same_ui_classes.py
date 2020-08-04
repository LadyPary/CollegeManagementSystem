from PyQt5 import QtCore, QtGui, QtWidgets

# Classes in this file was created by PyQt Designer.
# These create the base of QMainWindow and Qdialogs
# used to show infomation about the pages that all
# users have.


class Ui_edit_profile_page(object):
    def setupUi(self, edit_profile_page):
        edit_profile_page.setObjectName("edit_profile_page")
        edit_profile_page.resize(480, 440)
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
        edit_profile_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edit_profile_page.setWindowIcon(icon)
        self.layoutWidget_2 = QtWidgets.QWidget(edit_profile_page)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.edit_profile_page_layout = QtWidgets.QGridLayout(
            self.layoutWidget_2)
        self.edit_profile_page_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_profile_page_layout.setObjectName("edit_profile_page_layout")
        self.edit_profile_frame = QtWidgets.QFrame(edit_profile_page)
        self.edit_profile_frame.setGeometry(QtCore.QRect(10, 10, 461, 421))
        self.edit_profile_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.edit_profile_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.edit_profile_frame.setLineWidth(1)
        self.edit_profile_frame.setObjectName("edit_profile_frame")
        self.edit_profile_page_ut_logo = QtWidgets.QLabel(
            self.edit_profile_frame)
        self.edit_profile_page_ut_logo.setGeometry(
            QtCore.QRect(350, 0, 111, 111))
        self.edit_profile_page_ut_logo.setMinimumSize(QtCore.QSize(111, 111))
        self.edit_profile_page_ut_logo.setMaximumSize(
            QtCore.QSize(111, 16777215))
        self.edit_profile_page_ut_logo.setText("")
        self.edit_profile_page_ut_logo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.edit_profile_page_ut_logo.setObjectName(
            "edit_profile_page_ut_logo")
        self.edit_profile_page_label = QtWidgets.QLabel(
            self.edit_profile_frame)
        self.edit_profile_page_label.setGeometry(
            QtCore.QRect(59, 144, 341, 40))
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
        self.edit_profile_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.edit_profile_page_label.setFont(font)
        self.edit_profile_page_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.edit_profile_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_profile_page_label.setObjectName("edit_profile_page_label")
        self.layoutWidget = QtWidgets.QWidget(self.edit_profile_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 190, 116, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.edit_profile_verticalLayout = QtWidgets.QVBoxLayout(
            self.layoutWidget)
        self.edit_profile_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.edit_profile_verticalLayout.setObjectName(
            "edit_profile_verticalLayout")
        self.edit_profile_fullname_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.edit_profile_fullname_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_profile_fullname_label.setFont(font)
        self.edit_profile_fullname_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.edit_profile_fullname_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.edit_profile_fullname_label.setObjectName(
            "edit_profile_fullname_label")
        self.edit_profile_verticalLayout.addWidget(
            self.edit_profile_fullname_label)
        self.edit_profile_gender_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.edit_profile_gender_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_profile_gender_label.setFont(font)
        self.edit_profile_gender_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.edit_profile_gender_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_profile_gender_label.setObjectName(
            "edit_profile_gender_label")
        self.edit_profile_verticalLayout.addWidget(
            self.edit_profile_gender_label)
        self.layoutWidget_3 = QtWidgets.QWidget(self.edit_profile_frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(180, 190, 221, 121))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.edit_profile_verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.layoutWidget_3)
        self.edit_profile_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_profile_verticalLayout_2.setObjectName(
            "edit_profile_verticalLayout_2")
        self.edit_profile_fullname_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget_3)
        self.edit_profile_fullname_lineEdit.setText("")
        self.edit_profile_fullname_lineEdit.setFrame(True)
        self.edit_profile_fullname_lineEdit.setObjectName(
            "edit_profile_fullname_lineEdit")
        self.edit_profile_verticalLayout_2.addWidget(
            self.edit_profile_fullname_lineEdit)
        self.edit_profile_gender_comboBox = QtWidgets.QComboBox(
            self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_profile_gender_comboBox.setFont(font)
        self.edit_profile_gender_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_profile_gender_comboBox.setObjectName(
            "edit_profile_gender_comboBox")
        self.edit_profile_gender_comboBox.addItem("")
        self.edit_profile_gender_comboBox.addItem("")
        self.edit_profile_verticalLayout_2.addWidget(
            self.edit_profile_gender_comboBox)
        self.edit_profile_button = QtWidgets.QDialogButtonBox(
            self.layoutWidget_3)
        self.edit_profile_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_profile_button.setOrientation(QtCore.Qt.Horizontal)
        self.edit_profile_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.edit_profile_button.setObjectName("edit_profile_button")
        self.edit_profile_verticalLayout_2.addWidget(self.edit_profile_button)
        self.edit_profile_frame.raise_()
        self.layoutWidget_2.raise_()

        self.retranslateUi(edit_profile_page)
        self.edit_profile_button.accepted.connect(edit_profile_page.accept)
        self.edit_profile_button.rejected.connect(edit_profile_page.reject)
        QtCore.QMetaObject.connectSlotsByName(edit_profile_page)

    def retranslateUi(self, edit_profile_page):
        _translate = QtCore.QCoreApplication.translate
        edit_profile_page.setWindowTitle(
            _translate("edit_profile_page", "Edit Profile"))
        self.edit_profile_page_label.setToolTip(_translate(
            "edit_profile_page", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.edit_profile_page_label.setText(
            _translate("edit_profile_page", "Edit Profile"))
        self.edit_profile_fullname_label.setText(
            _translate("edit_profile_page", "Full Name:"))
        self.edit_profile_gender_label.setText(
            _translate("edit_profile_page", "Gender:"))
        self.edit_profile_gender_comboBox.setItemText(
            1, _translate("edit_profile_page", "Female"))
        self.edit_profile_gender_comboBox.setItemText(
            0, _translate("edit_profile_page", "Male"))


class Ui_signin_page(object):
    def setupUi(self, signin_page):
        signin_page.setObjectName("signin_page")
        signin_page.resize(480, 440)
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
        signin_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signin_page.setWindowIcon(icon)
        self.signin_page_label = QtWidgets.QLabel(signin_page)
        self.signin_page_label.setGeometry(QtCore.QRect(50, 110, 102, 38))
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
        self.signin_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.signin_page_label.setFont(font)
        self.signin_page_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signin_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_page_label.setObjectName("signin_page_label")
        self.signin_frame = QtWidgets.QFrame(signin_page)
        self.signin_frame.setGeometry(QtCore.QRect(10, 10, 461, 421))
        self.signin_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.signin_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.signin_frame.setLineWidth(1)
        self.signin_frame.setMidLineWidth(2)
        self.signin_frame.setObjectName("signin_frame")
        self.sigin_page_ut_logo = QtWidgets.QLabel(self.signin_frame)
        self.sigin_page_ut_logo.setGeometry(QtCore.QRect(340, 10, 111, 115))
        self.sigin_page_ut_logo.setMinimumSize(QtCore.QSize(111, 111))
        self.sigin_page_ut_logo.setMaximumSize(QtCore.QSize(111, 16777215))
        self.sigin_page_ut_logo.setText("")
        self.sigin_page_ut_logo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.sigin_page_ut_logo.setObjectName("sigin_page_ut_logo")
        self.signin_note_label = QtWidgets.QLabel(self.signin_frame)
        self.signin_note_label.setGeometry(QtCore.QRect(40, 280, 371, 35))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setItalic(True)
        self.signin_note_label.setFont(font)
        self.signin_note_label.setObjectName("signin_note_label")
        self.layoutWidget = QtWidgets.QWidget(signin_page)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 150, 371, 133))
        self.layoutWidget.setObjectName("layoutWidget")
        self.signin_page_gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.signin_page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.signin_page_gridLayout.setObjectName("signin_page_gridLayout")
        self.signin_buttons = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.signin_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.signin_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.signin_buttons.setObjectName("signin_buttons")
        self.signin_page_gridLayout.addWidget(self.signin_buttons, 3, 0, 1, 2)
        self.signin_password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.signin_password_lineEdit.setText("")
        self.signin_password_lineEdit.setFrame(True)
        self.signin_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signin_password_lineEdit.setObjectName("signin_password_lineEdit")
        self.signin_page_gridLayout.addWidget(
            self.signin_password_lineEdit, 2, 1, 1, 1)
        self.signin_password_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signin_password_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signin_password_label.setFont(font)
        self.signin_password_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signin_password_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signin_password_label.setObjectName("signin_password_label")
        self.signin_page_gridLayout.addWidget(
            self.signin_password_label, 2, 0, 1, 1)
        self.signin_username_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signin_username_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signin_username_label.setFont(font)
        self.signin_username_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signin_username_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signin_username_label.setObjectName("signin_username_label")
        self.signin_page_gridLayout.addWidget(
            self.signin_username_label, 1, 0, 1, 1)
        self.signin_username_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.signin_username_lineEdit.setText("")
        self.signin_username_lineEdit.setFrame(True)
        self.signin_username_lineEdit.setObjectName("signin_username_lineEdit")
        self.signin_page_gridLayout.addWidget(
            self.signin_username_lineEdit, 1, 1, 1, 1)
        self.signin_frame.raise_()
        self.layoutWidget.raise_()
        self.signin_page_label.raise_()

        self.retranslateUi(signin_page)
        # self.signin_buttons.accepted.connect(signin_page.accept)
        self.signin_buttons.rejected.connect(signin_page.reject)
        QtCore.QMetaObject.connectSlotsByName(signin_page)

    def retranslateUi(self, signin_page):
        _translate = QtCore.QCoreApplication.translate
        signin_page.setWindowTitle(_translate("signin_page", "Sign In"))
        self.signin_page_label.setToolTip(_translate(
            "signin_page", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.signin_page_label.setText(_translate("signin_page", "Sign In"))
        self.signin_note_label.setText(_translate("signin_page", "NOTE: If you\'re a student, Your username is your\n"
                                                  " Student ID. Otherwise it\'s your email."))
        self.signin_password_label.setText(
            _translate("signin_page", "Password:"))
        self.signin_username_label.setText(
            _translate("signin_page", "Username: "))


class Ui_signup_page(object):
    def setupUi(self, signup_page):
        signup_page.setObjectName("signup_page")
        signup_page.resize(480, 440)
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
        signup_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signup_page.setWindowIcon(icon)
        signup_page.setAutoFillBackground(False)
        signup_page.setSizeGripEnabled(False)
        self.signup_frame = QtWidgets.QFrame(signup_page)
        self.signup_frame.setGeometry(QtCore.QRect(10, 10, 461, 421))
        self.signup_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.signup_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.signup_frame.setLineWidth(1)
        self.signup_frame.setObjectName("signup_frame")
        self.signup_page_ut_logo = QtWidgets.QLabel(self.signup_frame)
        self.signup_page_ut_logo.setGeometry(QtCore.QRect(350, 0, 111, 111))
        self.signup_page_ut_logo.setMinimumSize(QtCore.QSize(111, 111))
        self.signup_page_ut_logo.setMaximumSize(QtCore.QSize(111, 16777215))
        self.signup_page_ut_logo.setText("")
        self.signup_page_ut_logo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.signup_page_ut_logo.setObjectName("signup_page_ut_logo")
        self.signup_note_label = QtWidgets.QLabel(self.signup_frame)
        self.signup_note_label.setGeometry(QtCore.QRect(10, 340, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setItalic(True)
        self.signup_note_label.setFont(font)
        self.signup_note_label.setObjectName("signup_note_label")
        self.signup_page_label = QtWidgets.QLabel(self.signup_frame)
        self.signup_page_label.setGeometry(QtCore.QRect(10, 80, 231, 38))
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
        self.signup_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.signup_page_label.setFont(font)
        self.signup_page_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_page_label.setObjectName("signup_page_label")
        self.layoutWidget = QtWidgets.QWidget(self.signup_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 235, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.signup_page_verticalLayout = QtWidgets.QVBoxLayout(
            self.layoutWidget)
        self.signup_page_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.signup_page_verticalLayout.setSpacing(1)
        self.signup_page_verticalLayout.setObjectName(
            "signup_page_verticalLayout")
        self.signup_fullname_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_fullname_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_fullname_label.setFont(font)
        self.signup_fullname_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_fullname_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_fullname_label.setObjectName("signup_fullname_label")
        self.signup_page_verticalLayout.addWidget(self.signup_fullname_label)
        self.signup_gender_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_gender_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_gender_label.setFont(font)
        self.signup_gender_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_gender_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_gender_label.setObjectName("signup_gender_label")
        self.signup_page_verticalLayout.addWidget(self.signup_gender_label)
        self.signup_username_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_username_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_username_label.setFont(font)
        self.signup_username_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_username_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_username_label.setObjectName("signup_username_label")
        self.signup_page_verticalLayout.addWidget(self.signup_username_label)
        self.signup_password_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_password_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_password_label.setFont(font)
        self.signup_password_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_password_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_password_label.setObjectName("signup_password_label")
        self.signup_page_verticalLayout.addWidget(self.signup_password_label)
        self.signup_passconfirm_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_passconfirm_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_passconfirm_label.setFont(font)
        self.signup_passconfirm_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_passconfirm_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_passconfirm_label.setObjectName("signup_passconfirm_label")
        self.signup_page_verticalLayout.addWidget(
            self.signup_passconfirm_label)
        self.signup_status_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_status_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_status_label.setFont(font)
        self.signup_status_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_status_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_status_label.setObjectName("signup_status_label")
        self.signup_page_verticalLayout.addWidget(self.signup_status_label)
        self.signup_field_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.signup_field_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signup_field_label.setFont(font)
        self.signup_field_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_field_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signup_field_label.setObjectName("signup_field_label")
        self.signup_page_verticalLayout.addWidget(self.signup_field_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.signup_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 120, 201, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.signup_page_verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.layoutWidget1)
        self.signup_page_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.signup_page_verticalLayout_2.setObjectName(
            "signup_page_verticalLayout_2")
        self.signup_fullname_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.signup_fullname_lineEdit.setText("")
        self.signup_fullname_lineEdit.setFrame(True)
        self.signup_fullname_lineEdit.setObjectName("signup_fullname_lineEdit")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_fullname_lineEdit)
        self.signup_gender_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_gender_comboBox.setFont(font)
        self.signup_gender_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_gender_comboBox.setObjectName("signup_gender_comboBox")
        self.signup_gender_comboBox.addItem("")
        self.signup_gender_comboBox.addItem("")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_gender_comboBox)
        self.signup_username_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.signup_username_lineEdit.setAutoFillBackground(False)
        self.signup_username_lineEdit.setText("")
        self.signup_username_lineEdit.setFrame(True)
        self.signup_username_lineEdit.setObjectName("signup_username_lineEdit")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_username_lineEdit)
        self.signup_password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.signup_password_lineEdit.setText("")
        self.signup_password_lineEdit.setFrame(True)
        self.signup_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_password_lineEdit.setObjectName("signup_password_lineEdit")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_password_lineEdit)
        self.signup_passconfirm_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget1)
        self.signup_passconfirm_lineEdit.setText("")
        self.signup_passconfirm_lineEdit.setFrame(True)
        self.signup_passconfirm_lineEdit.setEchoMode(
            QtWidgets.QLineEdit.Password)
        self.signup_passconfirm_lineEdit.setObjectName(
            "signup_passconfirm_lineEdit")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_passconfirm_lineEdit)
        self.signup_status_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_status_comboBox.setFont(font)
        self.signup_status_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_status_comboBox.setObjectName("signup_status_comboBox")
        self.signup_status_comboBox.addItem("")
        self.signup_status_comboBox.addItem("")
        self.signup_status_comboBox.addItem("")
        self.signup_page_verticalLayout_2.addWidget(
            self.signup_status_comboBox)
        self.signup_field_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.signup_field_lineEdit.setText("")
        self.signup_field_lineEdit.setFrame(True)
        self.signup_field_lineEdit.setObjectName("signup_field_lineEdit")
        self.signup_page_verticalLayout_2.addWidget(self.signup_field_lineEdit)
        self.signup_buttons = QtWidgets.QDialogButtonBox(self.layoutWidget1)
        self.signup_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.signup_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.signup_buttons.setObjectName("signup_buttons")
        self.signup_page_verticalLayout_2.addWidget(self.signup_buttons)
        self.layoutWidget2 = QtWidgets.QWidget(signup_page)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.signup_page_gridLayout_2 = QtWidgets.QGridLayout(
            self.layoutWidget2)
        self.signup_page_gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.signup_page_gridLayout_2.setObjectName("signup_page_gridLayout_2")

        self.retranslateUi(signup_page)
    #    self.signup_buttons.accepted.connect(signup_page.accept)
        self.signup_buttons.rejected.connect(signup_page.reject)
        QtCore.QMetaObject.connectSlotsByName(signup_page)

    def retranslateUi(self, signup_page):
        _translate = QtCore.QCoreApplication.translate
        signup_page.setWindowTitle(_translate("signup_page", "Sign Up"))
        self.signup_note_label.setText(_translate("signup_page", "NOTE: If you\'re a student, \n"
                                                  "Your username is your Student ID. \n"
                                                  "Otherwise it\'s your email."))
        self.signup_page_label.setToolTip(_translate(
            "signup_page", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.signup_page_label.setText(_translate("signup_page", "Sign Up"))
        self.signup_fullname_label.setText(
            _translate("signup_page", "Full Name:"))
        self.signup_gender_label.setText(_translate("signup_page", "Gender:"))
        self.signup_username_label.setText(
            _translate("signup_page", "Username: "))
        self.signup_password_label.setText(
            _translate("signup_page", "Password:"))
        self.signup_passconfirm_label.setText(
            _translate("signup_page", "Password  Confirmation:"))
        self.signup_status_label.setText(_translate("signup_page", "Status:"))
        self.signup_field_label.setText(_translate(
            "signup_page", "Field (students only):"))
        self.signup_gender_comboBox.setItemText(
            0, _translate("signup_page", "Male"))
        self.signup_gender_comboBox.setItemText(
            1, _translate("signup_page", "Female"))
        self.signup_status_comboBox.setItemText(
            0, _translate("signup_page", "Student"))
        self.signup_status_comboBox.setItemText(
            1, _translate("signup_page", "Professor"))
        self.signup_status_comboBox.setItemText(
            2, _translate("signup_page", "Dean of the faculty"))


class Ui_change_password_page(object):
    def setupUi(self, student_change_password_page):
        student_change_password_page.setObjectName(
            "student_change_password_page")
        student_change_password_page.resize(480, 440)
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
        student_change_password_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_change_password_page.setWindowIcon(icon)
        self.change_pass_frame = QtWidgets.QFrame(student_change_password_page)
        self.change_pass_frame.setGeometry(QtCore.QRect(10, 10, 461, 411))
        self.change_pass_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.change_pass_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.change_pass_frame.setLineWidth(1)
        self.change_pass_frame.setObjectName("change_pass_frame")
        self.change_pass_page_ut_logo = QtWidgets.QLabel(
            self.change_pass_frame)
        self.change_pass_page_ut_logo.setGeometry(
            QtCore.QRect(350, 0, 111, 111))
        self.change_pass_page_ut_logo.setMinimumSize(QtCore.QSize(111, 111))
        self.change_pass_page_ut_logo.setMaximumSize(
            QtCore.QSize(111, 16777215))
        self.change_pass_page_ut_logo.setText("")
        self.change_pass_page_ut_logo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.change_pass_page_ut_logo.setObjectName("change_pass_page_ut_logo")
        self.layoutWidget = QtWidgets.QWidget(self.change_pass_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 133, 441, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.change_pass_page_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.change_pass_page_layout.setContentsMargins(0, 0, 0, 0)
        self.change_pass_page_layout.setObjectName("change_pass_page_layout")
        self.change_pass_page_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.change_pass_page_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.change_pass_page_label.setFont(font)
        self.change_pass_page_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.change_pass_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.change_pass_page_label.setObjectName("change_pass_page_label")
        self.change_pass_page_layout.addWidget(
            self.change_pass_page_label, 0, 0, 1, 2)
        self.change_pass_password_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.change_pass_password_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.change_pass_password_label.setFont(font)
        self.change_pass_password_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.change_pass_password_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.change_pass_password_label.setObjectName(
            "change_pass_password_label")
        self.change_pass_page_layout.addWidget(
            self.change_pass_password_label, 1, 0, 1, 1)
        self.change_pass_password_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget)
        self.change_pass_password_lineEdit.setText("")
        self.change_pass_password_lineEdit.setFrame(True)
        self.change_pass_password_lineEdit.setEchoMode(
            QtWidgets.QLineEdit.Password)
        self.change_pass_password_lineEdit.setObjectName(
            "change_pass_password_lineEdit")
        self.change_pass_page_layout.addWidget(
            self.change_pass_password_lineEdit, 1, 1, 1, 1)
        self.change_pass_passconfirm_label = QtWidgets.QLabel(
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
        self.change_pass_passconfirm_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.change_pass_passconfirm_label.setFont(font)
        self.change_pass_passconfirm_label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.change_pass_passconfirm_label.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.change_pass_passconfirm_label.setObjectName(
            "change_pass_passconfirm_label")
        self.change_pass_page_layout.addWidget(
            self.change_pass_passconfirm_label, 2, 0, 1, 1)
        self.change_pass_passconfirm_lineEdit = QtWidgets.QLineEdit(
            self.layoutWidget)
        self.change_pass_passconfirm_lineEdit.setText("")
        self.change_pass_passconfirm_lineEdit.setFrame(True)
        self.change_pass_passconfirm_lineEdit.setEchoMode(
            QtWidgets.QLineEdit.Password)
        self.change_pass_passconfirm_lineEdit.setObjectName(
            "change_pass_passconfirm_lineEdit")
        self.change_pass_page_layout.addWidget(
            self.change_pass_passconfirm_lineEdit, 2, 1, 1, 1)
        self.change_pass_buttons = QtWidgets.QDialogButtonBox(
            self.layoutWidget)
        self.change_pass_buttons.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_pass_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.change_pass_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.change_pass_buttons.setObjectName("change_pass_buttons")
        self.change_pass_page_layout.addWidget(
            self.change_pass_buttons, 3, 1, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(student_change_password_page)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.change_pass_page_layout_2 = QtWidgets.QGridLayout(
            self.layoutWidget_2)
        self.change_pass_page_layout_2.setContentsMargins(0, 0, 0, 0)
        self.change_pass_page_layout_2.setObjectName(
            "change_pass_page_layout_2")

        self.retranslateUi(student_change_password_page)
        # self.change_pass_buttons.accepted.connect(student_change_password_page.accept)
        self.change_pass_buttons.rejected.connect(
            student_change_password_page.reject)
        QtCore.QMetaObject.connectSlotsByName(student_change_password_page)

    def retranslateUi(self, student_change_password_page):
        _translate = QtCore.QCoreApplication.translate
        student_change_password_page.setWindowTitle(_translate(
            "student_change_password_page", "Change Password"))
        self.change_pass_page_label.setToolTip(_translate(
            "student_change_password_page", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.change_pass_page_label.setText(_translate(
            "student_change_password_page", "Change password"))
        self.change_pass_password_label.setText(
            _translate("student_change_password_page", "Password:"))
        self.change_pass_passconfirm_label.setText(_translate(
            "student_change_password_page", "Password  Confirmation:"))


class Ui_first_page(object):
    def setupUi(self, first_page):
        first_page.setObjectName("first_page")
        first_page.setEnabled(True)
        first_page.resize(480, 440)
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
        first_page.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UT.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        first_page.setWindowIcon(icon)
        first_page.setAutoFillBackground(False)
        self.cfirst_page_entralwidget = QtWidgets.QWidget(first_page)
        self.cfirst_page_entralwidget.setObjectName("cfirst_page_entralwidget")
        self.first_page_frame = QtWidgets.QFrame(self.cfirst_page_entralwidget)
        self.first_page_frame.setGeometry(QtCore.QRect(10, 10, 461, 401))
        self.first_page_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.first_page_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.first_page_frame.setObjectName("first_page_frame")
        self.first_page_ut_logo = QtWidgets.QLabel(self.first_page_frame)
        self.first_page_ut_logo.setGeometry(QtCore.QRect(340, 10, 111, 111))
        self.first_page_ut_logo.setMinimumSize(QtCore.QSize(111, 111))
        self.first_page_ut_logo.setMaximumSize(QtCore.QSize(111, 16777215))
        self.first_page_ut_logo.setText("")
        self.first_page_ut_logo.setPixmap(QtGui.QPixmap("UT_logo.png"))
        self.first_page_ut_logo.setObjectName("first_page_ut_logo")
        self.layoutWidget = QtWidgets.QWidget(self.first_page_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 275, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.first_page_gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.first_page_gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.first_page_gridLayout_2.setObjectName("first_page_gridLayout_2")
        self.first_page_date_and_time_Label = QtWidgets.QLabel(
            self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 180, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.HighlightedText, brush)
        self.first_page_date_and_time_Label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.first_page_date_and_time_Label.setFont(font)
        self.first_page_date_and_time_Label.setTabletTracking(False)
        self.first_page_date_and_time_Label.setFrameShape(
            QtWidgets.QFrame.Panel)
        self.first_page_date_and_time_Label.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.first_page_date_and_time_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_page_date_and_time_Label.setObjectName(
            "first_page_date_and_time_Label")
        self.first_page_gridLayout_2.addWidget(
            self.first_page_date_and_time_Label, 1, 0, 1, 1)
        self.first_page_welcome_label = QtWidgets.QLabel(self.layoutWidget)
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
        self.first_page_welcome_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pagul")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.first_page_welcome_label.setFont(font)
        self.first_page_welcome_label.setFrameShape(QtWidgets.QFrame.Box)
        self.first_page_welcome_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.first_page_welcome_label.setScaledContents(True)
        self.first_page_welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_page_welcome_label.setObjectName("first_page_welcome_label")
        self.first_page_gridLayout_2.addWidget(
            self.first_page_welcome_label, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.first_page_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 200, 88, 88))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.first_page_gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.first_page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.first_page_gridLayout.setObjectName("first_page_gridLayout")
        self.first_page_sign_up_button = QtWidgets.QPushButton(
            self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.first_page_sign_up_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.first_page_sign_up_button.setFont(font)
        self.first_page_sign_up_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_page_sign_up_button.setObjectName(
            "first_page_sign_up_button")
        self.first_page_gridLayout.addWidget(
            self.first_page_sign_up_button, 2, 0, 1, 1)
        self.first_page_sign_in_button = QtWidgets.QPushButton(
            self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 249, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.HighlightedText, brush)
        self.first_page_sign_in_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.first_page_sign_in_button.setFont(font)
        self.first_page_sign_in_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_page_sign_in_button.setObjectName(
            "first_page_sign_in_button")
        self.first_page_gridLayout.addWidget(
            self.first_page_sign_in_button, 0, 0, 1, 1)
        first_page.setCentralWidget(self.cfirst_page_entralwidget)
        self.statusbar = QtWidgets.QStatusBar(first_page)
        self.statusbar.setObjectName("statusbar")
        first_page.setStatusBar(self.statusbar)

        self.retranslateUi(first_page)
        QtCore.QMetaObject.connectSlotsByName(first_page)

    def retranslateUi(self, first_page):
        _translate = QtCore.QCoreApplication.translate
        first_page.setWindowTitle(_translate("first_page", "First Page"))
        self.first_page_date_and_time_Label.setText(
            _translate("first_page", "TextLabel"))
        self.first_page_welcome_label.setText(_translate("first_page", "Welcome to the\n"
                                                         " Modern University"))
        self.first_page_sign_up_button.setText(
            _translate("first_page", "Sign Up"))
        self.first_page_sign_in_button.setText(
            _translate("first_page", "Sign In"))
