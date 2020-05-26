# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import requests

from PyQt5 import QtCore, QtGui, QtWidgets

from uis.notesSinglePage import Ui_MainNotesPageWindow
from uis.resources.stylesheets import *


class Ui_MainNotesWindow(object):
    def __init__(self, parent=None, logged_in_user=None):
        self.parent = parent
        self.loged_in_user = logged_in_user

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("Notes")
        MainWindow.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Return = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Return.setObjectName("pushButton_Return")
        self.horizontalLayout.addWidget(self.pushButton_Return)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_addNewNote = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addNewNote.setObjectName("pushButton_addNewNote")
        self.pushButton_addNewNote.setMinimumSize(QtCore.QSize(200, 30))
        self.horizontalLayout.addWidget(self.pushButton_addNewNote)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_LogOut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LogOut.setObjectName("pushButton_LogOut")
        self.horizontalLayout.addWidget(self.pushButton_LogOut)
        spacerItem2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.gridLayout_2.setRowStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)


        self.addFrames()

        self.pushButton_Return.clicked.connect(self.clicked_return)
        self.pushButton_LogOut.clicked.connect(self.clicked_log_out)
        self.pushButton_addNewNote.clicked.connect(self.clicked_new_note)

        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.pushButton_Return.setIcon(self.icon)
        self.pushButton_Return.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Return.setStyleSheet(button_with_image_style_sheet)
        self.pushButton_Return.setToolTip("Return")

        self.logout_pixmap = QtGui.QPixmap("resources/logout.png")
        self.logout_pixmap = self.logout_pixmap.scaled(QtCore.QSize(36, 36))
        self.logout_icon = QtGui.QIcon(self.logout_pixmap)
        self.pushButton_LogOut.setIcon(self.logout_icon)
        self.pushButton_LogOut.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_LogOut.setStyleSheet(button_with_image_style_sheet)
        self.pushButton_LogOut.setToolTip("Log out")
        self.pushButton_addNewNote.setStyleSheet(button_small_blue_style_sheet)

        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_addNewNote.setText(_translate("MainWindow", "Add new note"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Notes"))

    # object = [title,text,id], objects=[object1,object2,object3,...]
    #adding notes
    def addFrames(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        url = "http://localhost:86/read_notes?owner_id="
        url += str(self.loged_in_user[0])

        notes = requests.post(url).json()
        i = 0
        row = 0
        column = 0
        return_pixmap = QtGui.QPixmap("resources/notes/n7.png")
        return_pixmap = return_pixmap.scaled(QtCore.QSize(100, 100))
        icon = QtGui.QIcon(return_pixmap)
        return_pixmap_delete = QtGui.QPixmap("resources/delete_bin.png")
        return_pixmap_delete = return_pixmap_delete.scaled(QtCore.QSize(40, 40))
        icon_delete = QtGui.QIcon(return_pixmap_delete)

        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        for note in notes:
            frame = QtWidgets.QFrame(self.centralwidget)
            frame.setMinimumSize(QtCore.QSize(180, 160))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName('frame'+str(i))
            pushButtonFrame = QtWidgets.QPushButton(frame)
            pushButtonFrame.setGeometry(QtCore.QRect(0, 0, 180, 28))
            pushButtonFrame.setObjectName('pushButton'+str(i))
            pushButtonFrame.setText(note["title"]) #title
            pushButtonFrame.setStyleSheet(transparent_background_style_sheet)
            pushButtonFrame.clicked.connect(lambda state, title=note["title"], text=note["notes_content"], noteId=note["note_id"]: self.clicked_single_note(title, text, noteId))
            pushButtonImage = QtWidgets.QPushButton(frame)
            pushButtonImage.setGeometry(QtCore.QRect(0, 30, 180, 130))
            pushButtonImage.setIcon(icon)
            pushButtonImage.setIconSize(QtCore.QSize(100, 100))
            pushButtonImage.setStyleSheet(button_with_image_style_sheet)
            pushButtonImage.clicked.connect(
                lambda state, title=note["title"], text=note["notes_content"], noteId=note["note_id"]: self.clicked_single_note(title, text,
                                                                                                     noteId))
            pushButtonDelete = QtWidgets.QPushButton(frame)
            pushButtonDelete.setGeometry(QtCore.QRect(150, 50, 40, 40))
            pushButtonDelete.setIcon(icon_delete)
            pushButtonDelete.setIconSize(QtCore.QSize(40, 40))
            pushButtonDelete.setStyleSheet(button_with_image_style_sheet)
            pushButtonDelete.clicked.connect(lambda state, noteId=note["note_id"]: self.clicked_delete_note(noteId))
            self.gridLayout.addWidget(frame, row, column, 1, 1)
            if column == 3:
                column = 0
                row = row + 1
            else:
                column = column+1
            i = i + 1
        QtWidgets.QApplication.restoreOverrideCursor()

    def clicked_single_note(self, title, text, id):
        print("Go to single note")
        print(id)
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesPageWindow(self, self.loged_in_user, title, text, id)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()

    #go to single note, set the id to 0
    def clicked_new_note(self):
        self.clicked_single_note("", "", 0)

    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()

    def clicked_log_out(self):
        print('log out')
        self.show_site = self.parent
        while(self.show_site.parent != None):
            self.show_site = self.show_site.parent

        self.show_site.window.show()
        self.window.hide()

    def clicked_delete_note(self, id):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        print("Delete note")
        print(id)
        requests.post('http://localhost:86/delete_note', json={"note_id": id})
        self.addFrames()
        QtWidgets.QApplication.restoreOverrideCursor()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainNotesWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
