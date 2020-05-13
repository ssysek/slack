# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from uis.notesSinglePage import Ui_MainNotesPageWindow


class Ui_MainNotesWindow(object):
    def __init__(self, parent=None, logged_in_user=None):
        self.parent = parent
        self.loged_in_user = logged_in_user

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Return = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Return.setObjectName("pushButton_Return")
        self.horizontalLayout.addWidget(self.pushButton_Return)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_addNewNote = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_addNewNote.setObjectName("pushButton_addNewNote")
        self.horizontalLayout.addWidget(self.pushButton_addNewNote)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_LogOut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_LogOut.setObjectName("pushButton_LogOut")
        self.horizontalLayout.addWidget(self.pushButton_LogOut)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 1081, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)


        self.addFrames([['notatka 1', 'treść notatki 1', 1], ['notatka2', 'treśc notatki 2', 2],
                        ['Kolejna notatka', 'Dzisiaj do zrobienia: 1.Nie wiem ', 3],
                        ["notateczka", 'hmhmhmhmhmhmhmhmmhhmhmhmhmhmmhmhmmhmhmhmhmhh', 4],
                        ['Notateczkunia', 'nononononononononononononoononononon', 5], ['notatkaaa', 'Co dzisiaj do zrobienia', 6],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 7],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 8],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 9],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 10],
                        ['Kolejna notatka', 'notatka notatka notatka notatka notatka notatka notatka', 11]])

        self.pushButton_Return.clicked.connect(self.clicked_return)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Return.setText(_translate("MainWindow", "Return"))
        self.pushButton_addNewNote.setText(_translate("MainWindow", "Add new note"))
        self.pushButton_LogOut.setText(_translate("MainWindow", "Log out"))

    def addFrames(self, objects):
        i = 0
        row = 0
        column = 0
        for object in objects:
            frame = QtWidgets.QFrame(self.gridLayoutWidget)
            frame.setMinimumSize(QtCore.QSize(180, 160))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName('frame'+str(i))
            pushButtonFrame = QtWidgets.QPushButton(frame)
            pushButtonFrame.setGeometry(QtCore.QRect(0, 0, 180, 28))
            pushButtonFrame.setObjectName('pushButton'+str(i))
            pushButtonFrame.setText(object[0])
            # pushButtonFrame.clicked.connect(self.goToSingleNote(object[0], object[1], object[2]))
            textBrowserFrame = QtWidgets.QTextBrowser(frame)
            textBrowserFrame.setGeometry(QtCore.QRect(0, 30, 180, 130))
            textBrowserFrame.setObjectName("textBrowser"+str(1))
            textBrowserFrame.setText(object[1])
            self.gridLayout.addWidget(frame, row, column, 1, 1)
            if column == 3:
                column = 0
                row = row + 1
            else:
                column = column+1
            i = i + 1

    def goToSingleNote(self, title, text, id):
        print("Go to single note")
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesPageWindow(self, self.loged_in_user, title, text, id)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()

    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainNotesWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
