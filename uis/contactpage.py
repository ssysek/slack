# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactWindow(object):
    def __init__(self, parent = None):
        self.patent = parent

    def setupUi(self, ContactWindow):
        self.window = ContactWindow

        ContactWindow.setObjectName("ContactWindow")
        ContactWindow.resize(1201, 641)
        self.centralwidget = QtWidgets.QWidget(ContactWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1181, 581))
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
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.edit_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_name.setEnabled(True)
        self.edit_name.setObjectName("edit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
        self.label_email = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.edit_email = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.edit_email.setObjectName("edit_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_email)
        self.label_phone = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.edit_phone = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_phone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.edit_phone.setObjectName("edit_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_phone)
        self.edit_message = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.edit_message.setObjectName("edit_message")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edit_message)
        self.label__message = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label__message.setFont(font)
        self.label__message.setObjectName("label__message")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label__message)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(91, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_cancel = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.button_submit = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_submit.setObjectName("button_submit")
        self.horizontalLayout_3.addWidget(self.button_submit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        ContactWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ContactWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 21))
        self.menubar.setObjectName("menubar")
        ContactWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ContactWindow)
        self.statusbar.setObjectName("statusbar")
        ContactWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ContactWindow)
        QtCore.QMetaObject.connectSlotsByName(ContactWindow)

        self.button_cancel.clicked.connect(self.clicked_cancel)
        self.button_submit.clicked.connect(self.clicked_submit)

    def retranslateUi(self, ContactWindow):
        _translate = QtCore.QCoreApplication.translate
        ContactWindow.setWindowTitle(_translate("ContactWindow", "MainWindow"))
        self.label_name.setText(_translate("ContactWindow", "Name"))
        self.label_email.setText(_translate("ContactWindow", "E-mail"))
        self.label_phone.setText(_translate("ContactWindow", "Phone No"))
        self.label__message.setText(_translate("ContactWindow", "Message"))
        self.button_cancel.setText(_translate("ContactWindow", "Cancel"))
        self.button_submit.setText(_translate("ContactWindow", "Submit"))


    def clicked_cancel(self):
        self.patent.window.show()
        self.window.hide()

    def clicked_submit(self):
        print(self.edit_email.text())
        print(self.edit_name.text())
        print(self.edit_phone.text())
        print(self.edit_message.toPlainText())
        self.patent.window.show()
        self.window.hide()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactWindow = QtWidgets.QMainWindow()
    ui = Ui_ContactWindow()
    ui.setupUi(ContactWindow)
    ContactWindow.show()
    sys.exit(app.exec_())
