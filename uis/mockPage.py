# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from resources.stylesheets import button_with_image_style_sheet


class Ui_MockWindow(object):
    def __init__(self, parent=None, mock='notes'):
        self.parent = parent
        self.mock = mock

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(30, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QtGui.QIcon('../resources/taco.png'))
        if self.mock == 'notes':
            MainWindow.setStyleSheet("#MainWindow { border-image: url(resources/mocks/mockNotesMainPage.png) 0 0 0 0 stretch stretch; }")
        else:
            MainWindow.setStyleSheet("#MainWindow { border-image: url(resources/mocks/constructionPage.png) 0 0 0 0 stretch stretch; }")

        self.pushButton.clicked.connect(self.clicked_return)
        self.return_pixmap = QtGui.QPixmap("../resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.pushButton.setIcon(self.icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setStyleSheet(button_with_image_style_sheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Feature"))

    def clicked_return (self):
        print("Return")
        self.parent.window.show()
        self.window.hide()

