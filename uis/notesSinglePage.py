# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from uis.resources.stylesheets import *
import requests


class Ui_MainNotesPageWindow(object):
    def __init__(self, parent=None, logged_in_user=None, title='Tytył', text='Tekst notatki', note_id=0):
        self.parent = parent
        self.loged_in_user = logged_in_user
        self.title = title
        self.text = text
        self.note_id = note_id

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Return = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Return.setObjectName("pushButton_Return")
        self.horizontalLayout.addWidget(self.pushButton_Return)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title.setAutoFillBackground(False)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout.addWidget(self.lineEdit_title)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_LogOut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LogOut.setObjectName("pushButton_LogOut")
        self.horizontalLayout.addWidget(self.pushButton_LogOut)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.textEdit_text = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_text.setObjectName("textEdit_text")
        self.gridLayout.addWidget(self.textEdit_text, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_Return.clicked.connect(self.clicked_return)
        self.pushButton_save.clicked.connect(self.clicked_save)
        self.pushButton_LogOut.clicked.connect(self.clicked_log_out)

        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.pushButton_Return.setIcon(self.icon)
        self.pushButton_Return.setIconSize(QtCore.QSize(32, 32))

        self.pushButton_Return.setStyleSheet(button_with_image_style_sheet)
        self.pushButton_save.setStyleSheet(button_for_logging_style_sheet)

        self.logout_pixmap = QtGui.QPixmap("resources/logout.png")
        self.logout_pixmap = self.logout_pixmap.scaled(QtCore.QSize(36, 36))
        self.logout_icon = QtGui.QIcon(self.logout_pixmap)
        self.pushButton_LogOut.setIcon(self.logout_icon)
        self.pushButton_LogOut.setIconSize(QtCore.QSize(36, 36))
        self.lineEdit_title.setStyleSheet(border_style_sheet)
        self.textEdit_text.setStyleSheet(border_style_sheet)

        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.textEdit_text.setText(_translate("MainWindow", self.text))
        self.lineEdit_title.setText(_translate("MainWindow", self.title))

    def clicked_return(self):
        print("return to notes")
        self.parent.addFrames()
        self.parent.window.show()
        self.window.hide()

    def clicked_log_out(self):
        print('log out')
        self.show_site = self.parent
        while(self.show_site.parent != None):
            self.show_site = self.show_site.parent

        self.show_site.window.show()
        self.window.hide()

    def clicked_save(self):
        print("Save")
        print(self.lineEdit_title.text())
        print(self.textEdit_text.toPlainText())
        print(self.loged_in_user[0])
        #database endpoint to save
        if self.note_id==0:
            print("New note")
            register_request = requests.post('http://localhost:86/create_note',
                                             json={"title": self.lineEdit_title.text(), "notes_content":
            self.textEdit_text.toPlainText(), "owner_id": self.loged_in_user[0]})
            #get id from register_request
            print("Request poszedł")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainNotesPageWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())