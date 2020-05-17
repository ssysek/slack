# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from uis.notesSinglePage import Ui_MainNotesPageWindow
from uis.resources.stylesheets import *


class Ui_MainNotesWindow(object):
    def __init__(self, parent=None, logged_in_user=None):
        self.parent = parent
        self.loged_in_user = logged_in_user

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
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


        self.addFrames([['notatka 1', 'treść notatki 1', 1], ['notatka2', 'treśc notatki 2', 2],
                        ['Kolejna notatka', 'Dzisiaj do zrobienia: 1.Nie wiem ', 3],
                        ["notateczka", 'hmhmhmhmhmhmhmhmmhhmhmhmhmhmmhmhmmhmhmhmhmhh', 4],
                        ['Notateczkunia', 'nononononononononononononoononononon', 5], ['notatkaaa', 'Co dzisiaj do zrobienia', 6],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 7],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 8],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 9],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 10],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 11],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 12],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 13]])

        self.pushButton_Return.clicked.connect(self.clicked_return)
        self.pushButton_LogOut.clicked.connect(self.clicked_log_out)
        self.pushButton_addNewNote.clicked.connect(self.clicked_new_note)

        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.pushButton_Return.setIcon(self.icon)
        self.pushButton_Return.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Return.setStyleSheet(button_with_image_style_sheet)

        self.pushButton_LogOut.setStyleSheet(button_for_logging_style_sheet)
        self.pushButton_addNewNote.setStyleSheet(button_small_blue_style_sheet )

        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_addNewNote.setText(_translate("MainWindow", "Add new note"))
        self.pushButton_LogOut.setText(_translate("MainWindow", "LogOut"))

    # object = [title,text,id], objects=[object1,object2,object3,...]
    def addFrames(self, objects):
        i = 0
        row = 0
        column = 0
        return_pixmap = QtGui.QPixmap("resources/notes/n7.png")
        return_pixmap = return_pixmap.scaled(QtCore.QSize(100, 100))
        icon = QtGui.QIcon(return_pixmap)
        return_pixmap_delete = QtGui.QPixmap("resources/delete_bin.png")
        return_pixmap_delete = return_pixmap_delete.scaled(QtCore.QSize(40, 40))
        icon_delete = QtGui.QIcon(return_pixmap_delete)

        for object in objects:
            frame = QtWidgets.QFrame(self.centralwidget)
            frame.setMinimumSize(QtCore.QSize(180, 160))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName('frame'+str(i))
            pushButtonFrame = QtWidgets.QPushButton(frame)
            pushButtonFrame.setGeometry(QtCore.QRect(0, 0, 180, 28))
            pushButtonFrame.setObjectName('pushButton'+str(i))
            pushButtonFrame.setText(object[0])
            pushButtonFrame.setStyleSheet(transparent_background_style_sheet)
            pushButtonFrame.clicked.connect(lambda state, title=object[0], text=object[1], noteId=object[2]: self.clicked_single_note(title, text, noteId))
            pushButtonImage = QtWidgets.QPushButton(frame)
            pushButtonImage.setGeometry(QtCore.QRect(0, 30, 180, 130))
            pushButtonImage.setIcon(icon)
            pushButtonImage.setIconSize(QtCore.QSize(100, 100))
            pushButtonImage.setStyleSheet(button_with_image_style_sheet)
            pushButtonImage.clicked.connect(
                lambda state, title=object[0], text=object[1], noteId=object[2]: self.clicked_single_note(title, text,
                                                                                                     noteId))
            pushButtonDelete = QtWidgets.QPushButton(frame)
            pushButtonDelete.setGeometry(QtCore.QRect(150, 50, 40, 40))
            pushButtonDelete.setIcon(icon_delete)
            pushButtonDelete.setIconSize(QtCore.QSize(40, 40))
            pushButtonDelete.setStyleSheet(button_with_image_style_sheet)
            pushButtonDelete.clicked.connect(lambda state, noteId=object[2]: self.clicked_delete_note(noteId))
            self.gridLayout.addWidget(frame, row, column, 1, 1)
            if column == 3:
                column = 0
                row = row + 1
            else:
                column = column+1
            i = i + 1

    # decide later if we get the data again and only need id for data extraction or if we get it from main page notes info
    def clicked_single_note(self, title, text, id):
        print("Go to single note")
        # print(title)
        # print(text)
        print(id)
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesPageWindow(self, self.loged_in_user, title, text, id)
        # self.notes_window_ui = Ui_MainNotesPageWindow(self, self.loged_in_user, "bla", "bla tekst", id)
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
        print("Delete note")
        print(id)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainNotesWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
