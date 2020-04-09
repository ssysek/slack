# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(552, 358)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 491, 301))
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
        self.label__confirm_password = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label__confirm_password.setFont(font)
        self.label__confirm_password.setObjectName("label__confirm_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label__confirm_password)
        self.label_confirm_password = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.label_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_confirm_password)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(155, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_cancel = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.button_sign_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_sign_up.setObjectName("button_sign_up")
        self.horizontalLayout_3.addWidget(self.button_sign_up)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 21))
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
        self.label_username.setText(_translate("RegistrationWindow", "Username"))
        self.label__password.setText(_translate("RegistrationWindow", "Password"))
        self.label__confirm_password.setText(_translate("RegistrationWindow", "Confirm password"))
        self.button_cancel.setText(_translate("RegistrationWindow", "Cancel"))
        self.button_sign_up.setText(_translate("RegistrationWindow", "Sign Up"))



    def clicked_sign_up(self):
        print("sign up")

    def clicked_cancel(self):
        print("cancel")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())
