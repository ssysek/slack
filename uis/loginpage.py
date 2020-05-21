# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginpageWindow(object):
    def setupUi(self, LoginpageWindow):
        LoginpageWindow.setObjectName("LoginpageWindow")
        LoginpageWindow.resize(578, 475)
        LoginpageWindow.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(LoginpageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setMinimumSize(QtCore.QSize(0, 60))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("font: 75 16pt \"SansSerif\";")
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("font: 75 8pt \"SansSerif\";")
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)
        self.edit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_username.setEnabled(True)
        self.edit_username.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_username.setStyleSheet("font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(212, 174, 252);\n"
"background-color: rgb(247, 248, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:11px;")
        self.edit_username.setObjectName("edit_username")
        self.verticalLayout.addWidget(self.edit_username)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label__password = QtWidgets.QLabel(self.centralwidget)
        self.label__password.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label__password.setFont(font)
        self.label__password.setStyleSheet("font: 75 8pt \"SansSerif\";")
        self.label__password.setObjectName("label__password")
        self.verticalLayout_2.addWidget(self.label__password)
        self.edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_password.setStyleSheet("font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(212, 174, 252);\n"
"background-color: rgb(247, 248, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:11px;")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.verticalLayout_2.addWidget(self.edit_password)
        self.label_wrong = QtWidgets.QLabel(self.centralwidget)
        self.label_wrong.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_wrong.setStyleSheet("font: 75 8pt \"SansSerif\";\n"
"color: rgb(255, 47, 57);")
        self.label_wrong.setText("")
        self.label_wrong.setObjectName("label_wrong")
        self.verticalLayout_2.addWidget(self.label_wrong)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setMinimumSize(QtCore.QSize(0, 40))
        self.button_login.setMaximumSize(QtCore.QSize(15000, 40))
        self.button_login.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 10pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.button_login.setObjectName("button_login")
        self.verticalLayout_2.addWidget(self.button_login)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_donthave = QtWidgets.QLabel(self.centralwidget)
        self.label_donthave.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_donthave.setStyleSheet("font: 75 8pt \"SansSerif\";")
        self.label_donthave.setObjectName("label_donthave")
        self.horizontalLayout.addWidget(self.label_donthave)
        self.button_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign_up.setMaximumSize(QtCore.QSize(43, 16777215))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.button_sign_up.setFont(font)
        self.button_sign_up.setStyleSheet("background: transparent;\n"
"text-decoration: underline;\n"
"color: rgb(0, 85, 255);\n"
"font: 75 8pt \"SansSerif\";")
        self.button_sign_up.setObjectName("button_sign_up")
        self.horizontalLayout.addWidget(self.button_sign_up)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.button_cancel.setStyleSheet("background: transparent;\n"
"font: 75 8pt \"SansSerif\";")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        LoginpageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginpageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName("menubar")
        LoginpageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginpageWindow)
        self.statusbar.setObjectName("statusbar")
        LoginpageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginpageWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginpageWindow)

    def retranslateUi(self, LoginpageWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginpageWindow.setWindowTitle(_translate("LoginpageWindow", "MainWindow"))
        self.label_title.setText(_translate("LoginpageWindow", "Sign in to your account"))
        self.label_username.setText(_translate("LoginpageWindow", "Your Nickname"))
        self.label__password.setText(_translate("LoginpageWindow", "Your Password"))
        self.button_login.setText(_translate("LoginpageWindow", "Sign in to your account"))
        self.label_donthave.setText(_translate("LoginpageWindow", "   Don\'t have an account?"))
        self.button_sign_up.setText(_translate("LoginpageWindow", "Sign up!"))
        self.button_cancel.setText(_translate("LoginpageWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginpageWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginpageWindow()
    ui.setupUi(LoginpageWindow)
    LoginpageWindow.show()
    sys.exit(app.exec_())
