# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Return = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Return.setObjectName("pushButton_Return")
        self.horizontalLayout.addWidget(self.pushButton_Return)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_title = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_title.setAutoFillBackground(False)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout.addWidget(self.lineEdit_title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_LogOut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_LogOut.setObjectName("pushButton_LogOut")
        self.horizontalLayout.addWidget(self.pushButton_LogOut)
        self.textEdit_text = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_text.setGeometry(QtCore.QRect(30, 60, 731, 501))
        self.textEdit_text.setObjectName("textEdit_text")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_Return.clicked.connect(self.clicked_return)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Return.setText(_translate("MainWindow", "Return"))
        self.pushButton_LogOut.setText(_translate("MainWindow", "Log out"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.textEdit_text.setText(_translate("MainWindow", self.text))
        self.lineEdit_title.setText(_translate("MainWindow", self.title))

    def clicked_return(self):
        print("return to notes")
        # self.parent.window.show()
        # self.window.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainNotesPageWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())