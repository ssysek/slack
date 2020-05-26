# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.loged_in_user = user
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 647)
        MainWindow.setMinimumSize(QtCore.QSize(620, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem1, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.example_button_blue_7 = QtWidgets.QPushButton(self.centralwidget)
        self.example_button_blue_7.setEnabled(True)
        self.example_button_blue_7.setMinimumSize(QtCore.QSize(50, 50))
        self.example_button_blue_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.example_button_blue_7.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.example_button_blue_7.setAutoDefault(False)
        self.example_button_blue_7.setDefault(False)
        self.example_button_blue_7.setFlat(False)
        self.example_button_blue_7.setObjectName("example_button_blue_7")
        self.horizontalLayout_6.addWidget(self.example_button_blue_7)
        self.example_button_blue_4 = QtWidgets.QPushButton(self.centralwidget)
        self.example_button_blue_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.example_button_blue_4.sizePolicy().hasHeightForWidth())
        self.example_button_blue_4.setSizePolicy(sizePolicy)
        self.example_button_blue_4.setMinimumSize(QtCore.QSize(50, 50))
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
        self.horizontalLayout_6.addWidget(self.example_button_blue_4)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 3, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_2.setBaseSize(QtCore.QSize(0, 0))
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
        self.gridLayout_7.addWidget(self.textEdit_2, 5, 1, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_4.setBaseSize(QtCore.QSize(0, 0))
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
        self.gridLayout_7.addWidget(self.textEdit_4, 3, 3, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy)
        self.textEdit_5.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
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
        self.gridLayout_7.addWidget(self.textEdit_5, 3, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setEnabled(True)
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
        self.gridLayout_7.addWidget(self.textEdit_6, 8, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem5, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_3.setBaseSize(QtCore.QSize(0, 0))
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
        self.gridLayout_7.addWidget(self.textEdit_3, 5, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 3, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem7, 9, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem8, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 1, 0, 3, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_5, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_6)
        MainWindow.setTabOrder(self.textEdit_6, self.example_button_blue_7)
        MainWindow.setTabOrder(self.example_button_blue_7, self.example_button_blue_4)

        #tutaj logika
        self.example_button_blue_4.clicked.connect(self.clicked_cancel)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.example_button_blue_7.setText(_translate("MainWindow", "Submit"))
        self.example_button_blue_4.setText(_translate("MainWindow", "Cancel"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Email"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.textEdit_6.setPlaceholderText(_translate("MainWindow", "Your message here ..."))
        self.label.setText(_translate("MainWindow", "Contact us"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Subject"))

    def clicked_cancel(self):
        self.window.hide()
        print("cancel")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ContactWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
