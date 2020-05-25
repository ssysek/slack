# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(578, 454)
        RegistrationWindow.setAutoFillBackground(False)
        RegistrationWindow.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_name.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_name.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_name.setText("")
        self.edit_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_name.setObjectName("edit_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.edit_name)
        self.edit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_surname.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_surname.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_surname.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);\n"
"")
        self.edit_surname.setText("")
        self.edit_surname.setCursorPosition(0)
        self.edit_surname.setObjectName("edit_surname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_surname)
        self.edit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_email.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_email.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_email.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_email.setText("")
        self.edit_email.setObjectName("edit_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.edit_email)
        self.edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_login.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_login.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_login.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_login)
        self.edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_password.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_password.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.edit_password)
        self.edit_confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_confirm_password.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_confirm_password.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_confirm_password.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_confirm_password.setText("")
        self.edit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_confirm_password.setObjectName("edit_confirm_password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_confirm_password)
        self.gridLayout_3.addLayout(self.formLayout_2, 2, 1, 1, 1)
        self.label_password_error = QtWidgets.QLabel(self.centralwidget)
        self.label_password_error.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_password_error.setFont(font)
        self.label_password_error.setStyleSheet("font: 8pt \"Sans Serif\";\n"
"color: rgb(255, 47, 57);")
        self.label_password_error.setText("")
        self.label_password_error.setObjectName("label_password_error")
        self.gridLayout_3.addWidget(self.label_password_error, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_registration.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_registration.setFont(font)
        self.label_registration.setStyleSheet("font: 75 16pt \"SansSerif\";")
        self.label_registration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_registration.setObjectName("label_registration")
        self.gridLayout_2.addWidget(self.label_registration, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setMinimumSize(QtCore.QSize(110, 23))
        self.button_cancel.setMaximumSize(QtCore.QSize(110, 23))
        self.button_cancel.setStyleSheet("background: transparent;\n"
"font: 75 8pt \"SansSerif\";")
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 2, 1, 1)
        self.button_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign_up.setMinimumSize(QtCore.QSize(110, 40))
        self.button_sign_up.setMaximumSize(QtCore.QSize(110, 40))
        self.button_sign_up.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 10pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.button_sign_up.setObjectName("button_sign_up")
        self.gridLayout.addWidget(self.button_sign_up, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem10, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem12, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName("menubar")
        RegistrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

        RegistrationWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Register"))
        self.edit_name.setPlaceholderText(_translate("RegistrationWindow", "First Name"))
        self.edit_surname.setPlaceholderText(_translate("RegistrationWindow", "Last Name"))
        self.edit_email.setPlaceholderText(_translate("RegistrationWindow", "Email"))
        self.edit_login.setPlaceholderText(_translate("RegistrationWindow", "Nickname"))
        self.edit_password.setPlaceholderText(_translate("RegistrationWindow", "Password"))
        self.edit_confirm_password.setPlaceholderText(_translate("RegistrationWindow", "Confirm Password"))
        self.label_registration.setText(_translate("RegistrationWindow", "Registration"))
        self.button_cancel.setText(_translate("RegistrationWindow", "Cancel"))
        self.button_sign_up.setText(_translate("RegistrationWindow", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())
