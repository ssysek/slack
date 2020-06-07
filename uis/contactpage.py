# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resources.stylesheets import *


class Ui_ContactWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.loged_in_user = user
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
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
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setEnabled(True)
        self.button_submit.setMinimumSize(QtCore.QSize(50, 50))
        self.button_submit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_submit.setStyleSheet(button_for_logging_style_sheet)
        self.button_submit.setAutoDefault(False)
        self.button_submit.setDefault(False)
        self.button_submit.setFlat(False)
        self.button_submit.setObjectName("button_submit")
        self.horizontalLayout_6.addWidget(self.button_submit)
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setMinimumSize(QtCore.QSize(50, 50))
        self.button_cancel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_cancel.setToolTipDuration(-1)
        self.button_cancel.setStyleSheet("background-color:    rgb(200, 200, 200);\n"
"color:white;\n"
"font: 450 13pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:19px;\n"
"border-color:white;")
        self.button_cancel.setAutoDefault(False)
        self.button_cancel.setDefault(False)
        self.button_cancel.setFlat(False)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_6.addWidget(self.button_cancel)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 3, 2, 1, 1)
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_return.sizePolicy().hasHeightForWidth())
        self.button_return.setSizePolicy(sizePolicy)
        self.button_return.setObjectName("button_return")
        self.gridLayout_7.addWidget(self.button_return, 0, 0, 1, 1)
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
        self.textEdit_2.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
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
        self.textEdit_4.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
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
        self.textEdit_5.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
        self.textEdit_5.setTabChangesFocus(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_7.addWidget(self.textEdit_5, 3, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setEnabled(True)
        self.textEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_6.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
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
        self.label.setStyleSheet(pretty_big_darker_label_style_sheet)
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
        self.textEdit_3.setStyleSheet("background-color:rgb(221, 222, 235);\n"
                                      "color:black;\n"
                                      "font: 75 8pt \"SansSerif\";\n"
                                      "border-style:solid;\n"
                                      "border-width:2px;\n"
                                      "border-radius:11px;\n"
                                      "border-color:rgb(212, 174, 252);")
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
        MainWindow.setStyleSheet(gradient_style_sheet)

        MainWindow.setWindowIcon(QtGui.QIcon('../resources/taco.png'))

        self.return_pixmap = QtGui.QPixmap("../resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.button_return.setIcon(self.icon)
        self.button_return.setIconSize(QtCore.QSize(32, 32))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_5, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_6)
        MainWindow.setTabOrder(self.textEdit_6, self.button_submit)
        MainWindow.setTabOrder(self.button_submit, self.button_cancel)


        #tutaj logika
        self.button_cancel.clicked.connect(self.clicked_cancel)
        self.button_return.clicked.connect(self.clicked_return)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.button_cancel.setText(_translate("MainWindow", "Cancel"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Email"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.textEdit_6.setPlaceholderText(_translate("MainWindow", "Your message here ..."))
        self.label.setText(_translate("MainWindow", "Contact us"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Subject"))

    def clicked_cancel(self):
        self.parent.window.show()
        self.window.hide()

    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ContactWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
