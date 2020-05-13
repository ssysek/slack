# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from uis.loginpage_new import Ui_LoginpageWindow
#import psycopg2
import requests


class Ui_RegistrationWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.loged_in_user = user


    def setupUi(self, RegistrationWindow):
        self.window = RegistrationWindow
        RegistrationWindow.resize(592, 372)
        RegistrationWindow.setAutoFillBackground(False)
        RegistrationWindow.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 82, 408, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.edit_surname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_surname.setMinimumSize(QtCore.QSize(200, 40))
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
        self.edit_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_email.setMinimumSize(QtCore.QSize(200, 40))
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
        self.edit_login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_login.setMinimumSize(QtCore.QSize(200, 40))
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
        self.edit_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_password.setMinimumSize(QtCore.QSize(200, 40))
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
        self.edit_confirm_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_confirm_password.setMinimumSize(QtCore.QSize(200, 40))
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
        self.edit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_name.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_name.setStyleSheet("background-color:rgb(230, 230, 230);\n"
                                     "color:rgb(188, 188, 188);\n"
                                     "font: 75 8pt \"SansSerif\";\n"
                                     "border-style:solid;\n"
                                     "border-width:2px;\n"
                                     "border-radius:11px;\n"
                                     "border-color:rgb(225, 225, 225);")
        self.edit_name.setText("")
        self.edit_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.edit_name.setObjectName("edit_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.edit_name)
        self.label_password_error = QtWidgets.QLabel(self.formLayoutWidget)
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
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_password_error)
        self.button_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign_up.setGeometry(QtCore.QRect(243, 262, 110, 40))
        self.button_sign_up.setStyleSheet("background-color:rgb(1, 107, 229);\n"
                                          "color:white;\n"
                                          "font: 75 10pt \"SansSerif\";\n"
                                          "border-style:outset;\n"
                                          "border-width:2px;\n"
                                          "border-radius:10px;\n"
                                          "border-color:white;")
        self.button_sign_up.setObjectName("button_sign_up")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setGeometry(QtCore.QRect(243, 312, 110, 23))
        self.button_cancel.setStyleSheet("background: transparent;\n"
                                         "font: 75 8pt \"SansSerif\";")
        self.button_cancel.setObjectName("button_cancel")
        self.label_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_registration.setGeometry(QtCore.QRect(243, 22, 115, 30))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_registration.setFont(font)
        self.label_registration.setStyleSheet("font: 75 16pt \"SansSerif\";")
        self.label_registration.setObjectName("label_registration")
        self.label_nickname_error = QtWidgets.QLabel(self.centralwidget)
        self.label_nickname_error.setGeometry(QtCore.QRect(505, 140, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_nickname_error.setFont(font)
        self.label_nickname_error.setStyleSheet("font: 8pt \"Sans Serif\";\n"
                                                "color: rgb(255, 47, 57);\n"
                                                "")
        self.label_nickname_error.setText("")
        self.label_nickname_error.setObjectName("label_nickname_error")
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        RegistrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)



        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

        # tu wstawić logikę strony
        self.button_cancel.clicked.connect(self.clicked_cancel)
        self.button_sign_up.clicked.connect(self.clicked_sign_up)


    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.edit_surname.setPlaceholderText(_translate("RegistrationWindow", "Last Name"))
        self.edit_email.setPlaceholderText(_translate("RegistrationWindow", "Email"))
        self.edit_login.setPlaceholderText(_translate("RegistrationWindow", "Nickname"))
        self.edit_password.setPlaceholderText(_translate("RegistrationWindow", "Password"))
        self.edit_confirm_password.setPlaceholderText(_translate("RegistrationWindow", "Confirm Password"))
        self.edit_name.setPlaceholderText(_translate("RegistrationWindow", "First Name"))
        self.button_sign_up.setText(_translate("RegistrationWindow", "Create Account"))
        self.button_cancel.setText(_translate("RegistrationWindow", "Cancel"))
        self.label_registration.setText(_translate("RegistrationWindow", "Registration"))


    def clicked_sign_up(self):
        name = self.edit_name.text()
        surname = self.edit_surname.text()
        login = self.edit_login.text()
        password = self.edit_password.text()
        confirmed_password = self.edit_confirm_password.text()
        to_register = True
        all_users_request = requests.get("http://localhost:86/all_users")
        if all_users_request.json():
            for record in all_users_request.json():
                self.label_nickname_error.setText("")
                if record['login']==login or login=="":
                    self.label_nickname_error.setText("change")
                    to_register = False
                    break
        if confirmed_password!=password or password=="":
            self.label_password_error.setText("unset password or incorrect confirmation")
            to_register = False
        else:
            self.label_password_error.setText("")
        if to_register:
            register_request = requests.post('http://localhost:86/register', json={"user_name":name,"user_surname":surname,"login":login,"password":password})
            print("Success - now log in")
            self.window.hide()
            self.parent.clicked_log_in()


    def clicked_cancel(self):
        self.window.hide()
        print("cancel")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())
