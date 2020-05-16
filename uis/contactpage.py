# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactWindow(object):
    def setupUi(self, ContactWindow):
        ContactWindow.setObjectName("ContactWindow")
        ContactWindow.resize(1201, 648)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        ContactWindow.setFont(font)
        ContactWindow.setStyleSheet("3")
        self.centralwidget = QtWidgets.QWidget(ContactWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.example_button_blue_4 = QtWidgets.QPushButton(self.centralwidget)
        self.example_button_blue_4.setEnabled(True)
        self.example_button_blue_4.setGeometry(QtCore.QRect(280, 460, 151, 41))
        self.example_button_blue_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.example_button_blue_4.setToolTipDuration(-1)
        self.example_button_blue_4.setStyleSheet("background-color:    rgb(200, 200, 200);\n"
"color:white;\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.example_button_blue_4.setAutoDefault(False)
        self.example_button_blue_4.setDefault(False)
        self.example_button_blue_4.setFlat(False)
        self.example_button_blue_4.setObjectName("example_button_blue_4")
        self.example_button_blue_6 = QtWidgets.QPushButton(self.centralwidget)
        self.example_button_blue_6.setEnabled(True)
        self.example_button_blue_6.setGeometry(QtCore.QRect(120, 460, 151, 41))
        self.example_button_blue_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.example_button_blue_6.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.example_button_blue_6.setAutoDefault(False)
        self.example_button_blue_6.setDefault(False)
        self.example_button_blue_6.setFlat(False)
        self.example_button_blue_6.setObjectName("example_button_blue_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setEnabled(True)
        self.textEdit_6.setGeometry(QtCore.QRect(120, 246, 641, 191))
        self.textEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_6.setStyleSheet("background-color:     rgb(225, 225, 225);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.textEdit_6.setTabChangesFocus(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 190, 311, 41))
        self.textEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_2.setStyleSheet("background-color:     rgb(225, 225, 225);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(450, 190, 311, 41))
        self.textEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_3.setStyleSheet("background-color:     rgb(225, 225, 225);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(450, 130, 311, 41))
        self.textEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_4.setToolTip("")
        self.textEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_4.setStyleSheet("background-color:     rgb(225, 225, 225);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.textEdit_4.setTabChangesFocus(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(120, 130, 311, 41))
        self.textEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_5.setStyleSheet("background-color:     rgb(225, 225, 225);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.textEdit_5.setTabChangesFocus(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1101, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        ContactWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ContactWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
        self.menubar.setObjectName("menubar")
        ContactWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ContactWindow)
        self.statusbar.setObjectName("statusbar")
        ContactWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ContactWindow)
        QtCore.QMetaObject.connectSlotsByName(ContactWindow)
        ContactWindow.setTabOrder(self.textEdit_5, self.textEdit_4)
        ContactWindow.setTabOrder(self.textEdit_4, self.textEdit_2)
        ContactWindow.setTabOrder(self.textEdit_2, self.textEdit_3)
        ContactWindow.setTabOrder(self.textEdit_3, self.textEdit_6)
        ContactWindow.setTabOrder(self.textEdit_6, self.example_button_blue_6)
        ContactWindow.setTabOrder(self.example_button_blue_6, self.example_button_blue_4)

    def retranslateUi(self, ContactWindow):
        _translate = QtCore.QCoreApplication.translate
        ContactWindow.setWindowTitle(_translate("ContactWindow", "MainWindow"))
        self.example_button_blue_4.setText(_translate("ContactWindow", "Cancel"))
        self.example_button_blue_6.setText(_translate("ContactWindow", "Submit"))
        self.label.setText(_translate("ContactWindow", "Contact us"))
        self.textEdit_6.setPlaceholderText(_translate("ContactWindow", "Your message here ..."))
        self.textEdit_2.setPlaceholderText(_translate("ContactWindow", "Email"))
        self.textEdit_3.setPlaceholderText(_translate("ContactWindow", "Subject"))
        self.textEdit_4.setPlaceholderText(_translate("ContactWindow", "Last Name"))
        self.textEdit_5.setPlaceholderText(_translate("ContactWindow", "First Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactWindow = QtWidgets.QMainWindow()
    ui = Ui_ContactWindow()
    ui.setupUi(ContactWindow)
    ContactWindow.show()
    sys.exit(app.exec_())
