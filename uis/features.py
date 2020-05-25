# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'features.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from uis.chatforumpage import Ui_MainWindow as Ui_ChatWindow
from uis.notesmainpage import Ui_MainNotesWindow
from uis.resources.stylesheets import *

class Ui_FeaturesWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.loged_in_user = user

    def setupUi(self, FeaturesWindow):
        self.window = FeaturesWindow

        FeaturesWindow.setObjectName("FeaturesWindow")
        FeaturesWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(FeaturesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_store_notes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_store_notes.sizePolicy().hasHeightForWidth())
        self.button_store_notes.setSizePolicy(sizePolicy)
        self.button_store_notes.setObjectName("button_store_notes")
        self.gridLayout_2.addWidget(self.button_store_notes, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 4, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 13, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 4, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 11, 2, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 9, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 12, 2, 1, 3)
        self.button_chat_with_friends = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_chat_with_friends.sizePolicy().hasHeightForWidth())
        self.button_chat_with_friends.setSizePolicy(sizePolicy)
        self.button_chat_with_friends.setObjectName("button_chat_with_friends")
        self.gridLayout_2.addWidget(self.button_chat_with_friends, 3, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_return.sizePolicy().hasHeightForWidth())
        self.button_return.setSizePolicy(sizePolicy)
        self.button_return.setObjectName("button_return")
        self.gridLayout_2.addWidget(self.button_return, 0, 0, 1, 1)
        self.button_create_groups = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create_groups.sizePolicy().hasHeightForWidth())
        self.button_create_groups.setSizePolicy(sizePolicy)
        self.button_create_groups.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_create_groups.setObjectName("button_create_groups")
        self.gridLayout_2.addWidget(self.button_create_groups, 9, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 7, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 9, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        FeaturesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FeaturesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        FeaturesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FeaturesWindow)
        self.statusbar.setObjectName("statusbar")
        FeaturesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FeaturesWindow)
        QtCore.QMetaObject.connectSlotsByName(FeaturesWindow)

        FeaturesWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))
        FeaturesWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)



        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32,32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.button_return.setIcon(self.icon)
        self.button_return.setIconSize(QtCore.QSize(32, 32))

        self.store_notes_pixmap = QtGui.QPixmap("resources/notes.png")
        self.store_notes_pixmap = self.store_notes_pixmap.scaled(QtCore.QSize(64,64))
        self.store_notes_icon = QtGui.QIcon(self.store_notes_pixmap)
        self.button_store_notes.setIcon(self.store_notes_icon)
        self.button_store_notes.setIconSize(QtCore.QSize(64,64))

        self.chat_with_friends_pixmap = QtGui.QPixmap("resources/messages.png")
        self.chat_with_friends_pixmap = self.chat_with_friends_pixmap.scaled(QtCore.QSize(64,64))
        self.chat_with_friends_icon = QtGui.QIcon(self.chat_with_friends_pixmap)
        self.button_chat_with_friends.setIcon(self.chat_with_friends_icon)
        self.button_chat_with_friends.setIconSize(QtCore.QSize(64,64))

        self.create_groups_pixmap = QtGui.QPixmap("resources/groups.png")
        self.create_groups_pixmap = self.create_groups_pixmap.scaled(QtCore.QSize(64,64))
        self.create_groups_icon = QtGui.QIcon(self.create_groups_pixmap)
        self.button_create_groups.setIcon(self.create_groups_icon)
        self.button_create_groups.setIconSize(QtCore.QSize(64,64))


        self.button_chat_with_friends.clicked.connect(self.clicked_chat_with_friends)
        self.button_return.clicked.connect(self.clicked_return)
        self.button_create_groups.clicked.connect(self.clicked_create_groups)
        self.button_store_notes.clicked.connect(self.clicked_store_notes)

    def retranslateUi(self, FeaturesWindow):
        _translate = QtCore.QCoreApplication.translate
        FeaturesWindow.setWindowTitle(_translate("FeaturesWindow", "Features"))
        self.label.setText(_translate("FeaturesWindow", "<html><head/><body><p>A full ecosystem of tools</p><p>within a single web app.</p></body></html>"))
        self.label_5.setText(_translate("FeaturesWindow", "Chat with your friends"))
        self.label_7.setText(_translate("FeaturesWindow", "<html><head/><body><p>contact with them individually</p><p>or within groupchats</p></body></html>"))
        self.label_2.setText(_translate("FeaturesWindow", "Create groups"))
        self.label_3.setText(_translate("FeaturesWindow", "<html><head/><body><p>collaborate and communicate </p><p>easier with your team</p></body></html>"))
        self.label_4.setText(_translate("FeaturesWindow", "Store notes"))
        self.label_6.setText(_translate("FeaturesWindow", "<html><head/><body><p>keep all your important</p><p>documents in one place</p></body></html>"))

    def clicked_chat_with_friends(self):
        self.main_window = QtWidgets.QMainWindow()
        self.main_window_ui = Ui_ChatWindow(self, self.loged_in_user)
        self.main_window_ui.setupUi(self.main_window)
        self.main_window.show()
        self.window.hide()
        self.main_window_ui.doSomething()

    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()

    def clicked_create_groups(self):
        print("create groups")

    def clicked_store_notes(self):
        print("store notes")
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesWindow(self, self.loged_in_user)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FeaturesWindow = QtWidgets.QMainWindow()
    ui = Ui_FeaturesWindow()
    ui.setupUi(FeaturesWindow)
    FeaturesWindow.show()
    sys.exit(app.exec_())
