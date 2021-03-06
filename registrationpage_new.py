# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#import psycopg2
import requests

from resources.stylesheets import pretty_big_darker_label_style_sheet, gradient_style_sheet


class Ui_RegistrationWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.loged_in_user = user


    def setupUi(self, RegistrationWindow):
        self.window = RegistrationWindow
        RegistrationWindow.resize(578, 454)
        RegistrationWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_name.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_name.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                     "color:black;\n"
                                     "font: 75 8pt \"SansSerif\";\n"
                                     "border-style:solid;\n"
                                     "border-width:2px;\n"
                                     "border-radius:11px;\n"
                                     "border-color:rgb(212, 174, 252);")
        self.edit_name.setText("")
        self.edit_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.edit_name.setObjectName("edit_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.edit_name)
        self.edit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_surname.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_surname.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_surname.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                        "color:black;\n"
                                        "font: 75 8pt \"SansSerif\";\n"
                                        "border-style:solid;\n"
                                        "border-width:2px;\n"
                                        "border-radius:11px;\n"
                                        "border-color:rgb(212, 174, 252);\n"
                                        "")
        self.edit_surname.setText("")
        self.edit_surname.setCursorPosition(0)
        self.edit_surname.setObjectName("edit_surname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_surname)
        self.edit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_email.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_email.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_email.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
        self.edit_email.setText("")
        self.edit_email.setObjectName("edit_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.edit_email)
        self.edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_login.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_login.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_login.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_login)
        self.edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_password.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_password.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                         "color:black;\n"
                                         "font: 75 8pt \"SansSerif\";\n"
                                         "border-style:solid;\n"
                                         "border-width:2px;\n"
                                         "border-radius:11px;\n"
                                         "border-color:rgb(212, 174, 252);")
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.edit_password)
        self.edit_confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_confirm_password.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_confirm_password.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_confirm_password.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                                 "color:black;\n"
                                                 "font: 75 8pt \"SansSerif\";\n"
                                                 "border-style:solid;\n"
                                                 "border-width:2px;\n"
                                                 "border-radius:11px;\n"
                                                 "border-color:rgb(212, 174, 252);")
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
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
        self.label_registration.setStyleSheet(pretty_big_darker_label_style_sheet)
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
        self.button_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign_up.setMinimumSize(QtCore.QSize(200, 50))
        self.button_sign_up.setMaximumSize(QtCore.QSize(200, 50))
        self.button_sign_up.setStyleSheet("background-color:rgb(128, 45, 181);\n"
                                          "color:white;\n"
                                          "font: 450 13pt \"SansSerif\";\n"
                                          "border-style:outset;\n"
                                          "border-width:2px;\n"
                                          "border-radius:19px;\n"
                                          "border-color:rgb(212, 174, 252);")
        self.button_sign_up.setObjectName("button_sign_up")
        self.gridLayout.addWidget(self.button_sign_up, 0, 1, 1, 1)
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setMinimumSize(QtCore.QSize(200, 23))
        self.button_cancel.setMaximumSize(QtCore.QSize(200, 23))
        self.button_cancel.setStyleSheet("background: transparent;\n"
                                         "color:rgb(164, 66, 227);\n"
                                         "font: 75 8pt \"SansSerif\";")
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem10, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
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
        RegistrationWindow.setStyleSheet(gradient_style_sheet)


        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

        RegistrationWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))

        self.button_sign_up.setAutoDefault(True)
        self.button_cancel.setAutoDefault(True)
        self.button_cancel.clicked.connect(self.clicked_cancel)
        self.button_sign_up.clicked.connect(self.clicked_signup)


    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Register"))
        self.edit_name.setPlaceholderText(_translate("RegistrationWindow", "First Name"))
        self.edit_surname.setPlaceholderText(_translate("RegistrationWindow", "Last Name"))
        self.edit_email.setPlaceholderText(_translate("RegistrationWindow", "Email"))
        self.edit_login.setPlaceholderText(_translate("RegistrationWindow", "Nickname"))
        self.edit_password.setPlaceholderText(_translate("RegistrationWindow", "Password"))
        self.edit_confirm_password.setPlaceholderText(_translate("RegistrationWindow", "Confirm Password"))
        self.button_cancel.setText(_translate("RegistrationWindow", "Cancel"))
        self.button_sign_up.setText(_translate("RegistrationWindow", "Create Account"))
        self.label_registration.setText(_translate("RegistrationWindow", "Registration"))


    def clicked_signup(self):
        """
        checks if credentials provided by user are correct (no empty values, unique login, correct password confirmation) and does request call for registration
        """
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        name = self.edit_name.text()
        surname = self.edit_surname.text()
        email = self.edit_email.text()
        login = self.edit_login.text()
        password = self.edit_password.text()
        confirmed_password = self.edit_confirm_password.text()
        to_register = True
        error_text = ""
        self.label_password_error.setText(error_text)

        if name=="" or surname=="" or login=="" or password=="" or email=="":
            error_text+="at least one info missing"
            self.label_password_error.setText(error_text)
            to_register = False

        all_users_request = requests.get("http://localhost:86/all_users")
        if all_users_request.json():
            for record in all_users_request.json():
                if record['login']==login:
                    if error_text != "":
                        error_text += ", "
                    error_text += "nickname taken"
                    self.label_password_error.setText(error_text)
                    to_register = False
                    break

        if confirmed_password!=password:
            if error_text != "":
                error_text += " and "
            error_text += "incorrect password confirmation"
            self.label_password_error.setText(error_text)
            to_register = False

        if to_register:
            register_request = requests.post('http://localhost:86/register', json={"user_name":name,"user_surname":surname,"login":login,"password":password,"email":email})
            print("Success - now log in")
            self.window.hide()
            self.parent.clicked_log_in()
        QtWidgets.QApplication.restoreOverrideCursor()


    def clicked_cancel(self):
        """
        exits from login window
        """
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
