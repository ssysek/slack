# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from uis.chatforumpage import Ui_MainWindow as Ui_ChatWindow
from uis.registrationpage import Ui_RegistrationWindow
#import psycopg2
import requests

logged_id = -1
logged_name = ""
logged_surname=""

class Ui_LoginpageWindow(object):
    def __init__(self, parent=None):
        self.parent = parent


    def setupUi(self, LoginpageWindow):
        self.window = LoginpageWindow

        LoginpageWindow.setObjectName("LoginpageWindow")
        LoginpageWindow.resize(552, 358)
        self.centralwidget = QtWidgets.QWidget(LoginpageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 491, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(95, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_cancel = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.button_login = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout_3.addWidget(self.button_login)
        self.button_sign_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_sign_up.setObjectName("button_sign_up")
        self.horizontalLayout_3.addWidget(self.button_sign_up)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_username = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.edit_username = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_username.setEnabled(True)
        self.edit_username.setObjectName("edit_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_username)
        self.label__password = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label__password.setFont(font)
        self.label__password.setObjectName("label__password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label__password)
        self.edit_password = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_password)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        LoginpageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginpageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 21))
        self.menubar.setObjectName("menubar")
        LoginpageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginpageWindow)
        self.statusbar.setObjectName("statusbar")
        LoginpageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginpageWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginpageWindow)

        # tu wstawić logikę strony
        self.button_cancel.clicked.connect(self.clicked_cancel)
        self.button_login.clicked.connect(self.clicked_login)
        self.button_sign_up.clicked.connect(self.clicked_sign_up)

        self.register_window = QtWidgets.QMainWindow()
        self.register_window_ui = Ui_RegistrationWindow()
        self.register_window_ui.setupUi(self.register_window)


    def retranslateUi(self, LoginpageWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginpageWindow.setWindowTitle(_translate("LoginpageWindow", "MainWindow"))
        self.button_cancel.setText(_translate("LoginpageWindow", "Cancel"))
        self.button_login.setText(_translate("LoginpageWindow", "Login"))
        self.button_sign_up.setText(_translate("LoginpageWindow", "Sign Up"))
        self.label_username.setText(_translate("LoginpageWindow", "Username"))
        self.label__password.setText(_translate("LoginpageWindow", "Password"))


    def clicked_cancel(self):
        print("cancel")

    def clicked_sign_up(self):
        print("sign up")
        self.register_window.show()

    def warning(self, title, message):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setWindowTitle(title)
        warning_message.setText(message)
        warning_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        warning_message.exec_()

    def clicked_login(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        logged = False
        logged_id = -1
        logged_name = ""
        logged_surname = ""
        r = requests.get("http://localhost:86/all_users")
        if r.json():
            for record in r.json():
                if record['login']==username:
                    if record['password']==password:
                        logged = True
                        logged_id = record['user_id']
                        logged_name = record['user_name']
                        logged_surname = record['user_surname']
                        print("YOU SUCCESSFULLY LOGGED IN")
                        break

        if logged:
            self.main_window = QtWidgets.QMainWindow()
            self.main_window_ui = Ui_ChatWindow()
            self.main_window_ui.setupUi(self.main_window)
            self.main_window.show()
            self.main_window_ui.doSomething()
        else:
            self.warning("error","Wrong username or password!")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginpageWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginpageWindow()
    ui.setupUi(LoginpageWindow)
    LoginpageWindow.show()
    sys.exit(app.exec_())


def list_to_string(mlist):
    if type(mlist)==list:
        mstring =",".join(mlist)
        return mstring
    else:
        return mlist

