# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forumadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewForumWindow(object):
    def setupUi(self, NewForumWindow):
        NewForumWindow.setObjectName("NewForumWindow")
        NewForumWindow.resize(660, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewForumWindow.sizePolicy().hasHeightForWidth())
        NewForumWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(NewForumWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setMinimumSize(QtCore.QSize(75, 23))
        self.button_return.setMaximumSize(QtCore.QSize(75, 40))
        self.button_return.setText("")
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_2.addWidget(self.button_return)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_logout = QtWidgets.QPushButton(self.centralwidget)
        self.button_logout.setMinimumSize(QtCore.QSize(75, 0))
        self.button_logout.setMaximumSize(QtCore.QSize(75, 40))
        self.button_logout.setObjectName("button_logout")
        self.horizontalLayout_2.addWidget(self.button_logout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setMinimumSize(QtCore.QSize(110, 40))
        self.button_submit.setMaximumSize(QtCore.QSize(110, 40))
        self.button_submit.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 10pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.button_submit.setObjectName("button_submit")
        self.horizontalLayout_3.addWidget(self.button_submit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 1, 1, 1)
        self.edit_invite = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_invite.setMinimumSize(QtCore.QSize(400, 40))
        self.edit_invite.setMaximumSize(QtCore.QSize(300, 40))
        self.edit_invite.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.edit_invite.setText("")
        self.edit_invite.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_invite.setObjectName("edit_invite")
        self.gridLayout.addWidget(self.edit_invite, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 9, 1, 1, 1)
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setMinimumSize(QtCore.QSize(200, 40))
        self.edit_name.setMaximumSize(QtCore.QSize(400, 40))
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
        self.gridLayout.addWidget(self.edit_name, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 7, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 1)
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 8, 1, 1, 1)
        self.label_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_registration.setMinimumSize(QtCore.QSize(160, 70))
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
        self.gridLayout.addWidget(self.label_registration, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_icon1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_icon1.setText("")
        self.button_icon1.setObjectName("button_icon1")
        self.horizontalLayout.addWidget(self.button_icon1)
        self.button_icon2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_icon2.setText("")
        self.button_icon2.setObjectName("button_icon2")
        self.horizontalLayout.addWidget(self.button_icon2)
        self.button_icon3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_icon3.setText("")
        self.button_icon3.setObjectName("button_icon3")
        self.horizontalLayout.addWidget(self.button_icon3)
        self.button_icon4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_icon4.setText("")
        self.button_icon4.setObjectName("button_icon4")
        self.horizontalLayout.addWidget(self.button_icon4)
        self.button_icon5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_icon5.setText("")
        self.button_icon5.setObjectName("button_icon5")
        self.horizontalLayout.addWidget(self.button_icon5)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem10, 11, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        NewForumWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewForumWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        NewForumWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewForumWindow)
        self.statusbar.setObjectName("statusbar")
        NewForumWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewForumWindow)
        QtCore.QMetaObject.connectSlotsByName(NewForumWindow)

    def retranslateUi(self, NewForumWindow):
        _translate = QtCore.QCoreApplication.translate
        NewForumWindow.setWindowTitle(_translate("NewForumWindow", "MainWindow"))
        self.button_logout.setText(_translate("NewForumWindow", "Log out"))
        self.button_submit.setText(_translate("NewForumWindow", "Submit"))
        self.edit_invite.setPlaceholderText(_translate("NewForumWindow", "Invite someone"))
        self.edit_name.setPlaceholderText(_translate("NewForumWindow", "Name your forum"))
        self.label_registration.setText(_translate("NewForumWindow", "Create a forum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewForumWindow = QtWidgets.QMainWindow()
    ui = Ui_NewForumWindow()
    ui.setupUi(NewForumWindow)
    NewForumWindow.show()
    sys.exit(app.exec_())
