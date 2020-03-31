# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_forum_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_chanells = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_chanells.setObjectName("listWidget_chanells")
        self.gridLayout.addWidget(self.listWidget_chanells, 2, 1, 1, 1)
        self.listWidget_chats = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_chats.setObjectName("listWidget_chats")
        self.gridLayout.addWidget(self.listWidget_chats, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.listWidget_forums = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_forums.setObjectName("listWidget_forums")
        self.gridLayout.addWidget(self.listWidget_forums, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.listWidget_notes = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_notes.setObjectName("listWidget_notes")
        self.gridLayout.addWidget(self.listWidget_notes, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_opened_box = QtWidgets.QLabel(self.centralwidget)
        self.label_opened_box.setObjectName("label_opened_box")
        self.verticalLayout_3.addWidget(self.label_opened_box)
        self.listWidget_opened_box = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_opened_box.setObjectName("listWidget_opened_box")
        self.verticalLayout_3.addWidget(self.listWidget_opened_box)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.button_send_message = QtWidgets.QPushButton(self.centralwidget)
        self.button_send_message.setObjectName("button_send_message")
        self.horizontalLayout_2.addWidget(self.button_send_message)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(1, 15)
        self.verticalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 4, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button_log_out = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_log_out.sizePolicy().hasHeightForWidth())
        self.button_log_out.setSizePolicy(sizePolicy)
        self.button_log_out.setObjectName("button_log_out")
        self.horizontalLayout_4.addWidget(self.button_log_out)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actual_box = None
        self.messages = [('Adam1', 'Wiadomosc1'), ('Adam2', 'Wiadomosc2'), ('Adam3', 'Wiadomosc3'),
                         ('Adam4', 'Wiadomosc4'), ('Adam5', 'Wiadomosc5')]


    def doSomething(self):
        self.changeForumButtons(self.listWidget_forums,
                                [['test1', ['bla', 'ah', 'no']], ['haha', ['1', '2']], ['przycisk', ['a', 'b', 'c']]])
        self.changeNotesButtons(self.listWidget_notes,['aa', 'note1', 'bored'])
        self.changeChannelButtons(self.listWidget_chats, ['chat1', 'aga', 'bla', 'oj'])


    def changeForumButtons(self, nameWidget, objects):
        # Create widget
        for object in objects:
            itemN = QtWidgets.QListWidgetItem()
            widget = QtWidgets.QWidget()
            widgetButton = self.getForumWidgetButton(object)
            widgetLayout = QtWidgets.QHBoxLayout()
            widgetLayout.addWidget(widgetButton)
            widgetLayout.addStretch()
            widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            widget.setLayout(widgetLayout)
            itemN.setSizeHint(widget.sizeHint())
            # Add widget to QListWidget funList
            nameWidget.addItem(itemN)
            nameWidget.setItemWidget(itemN, widget)

    def getForumWidgetButton(self, object):
        widgetButton = QtWidgets.QPushButton(object[0])
        widgetButton.clicked.connect(lambda: self.changeChannelButtons(self.listWidget_chanells, object[1]))
        return widgetButton


    def changeChannelButtons(self, nameWidget, list):
        print(list)
        nameWidget.clear()
        for object in list:
            itemN = QtWidgets.QListWidgetItem()
            widget = QtWidgets.QWidget()
            widgetButton = self.getChannelWidgetButton(object)
            widgetLayout = QtWidgets.QHBoxLayout()
            widgetLayout.addWidget(widgetButton)
            widgetLayout.addStretch()
            widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            widget.setLayout(widgetLayout)
            itemN.setSizeHint(widget.sizeHint())
            # Add widget to QListWidget funList
            nameWidget.addItem(itemN)
            nameWidget.setItemWidget(itemN, widget)

    def getChannelWidgetButton(self, object):
        widgetButton = QtWidgets.QPushButton(object)
        print(object)
        widgetButton.clicked.connect(lambda: self.setUpMessages(object, object))
        return widgetButton


    def changeNotesButtons(self, nameWidget, list):
        print(list)
        nameWidget.clear()
        for object in list:
            itemN = QtWidgets.QListWidgetItem()
            widget = QtWidgets.QWidget()
            widgetButton = self.getChannelWidgetButton(object)
            widgetLayout = QtWidgets.QHBoxLayout()
            widgetLayout.addWidget(widgetButton)
            widgetLayout.addStretch()
            widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            widget.setLayout(widgetLayout)
            itemN.setSizeHint(widget.sizeHint())
            # Add widget to QListWidget funList
            nameWidget.addItem(itemN)
            nameWidget.setItemWidget(itemN, widget)

    def getNotesWidgetButton(self, object):
        widgetButton = QtWidgets.QPushButton(object)
        print(object)
        widgetButton.clicked.connect(lambda: self.printSecond('1'))
        return widgetButton



    def setUpMessages(self, arg, id): #arg - name of channel, id - id channel
        self.label_opened_box.setText(arg)
        self.label_opened_box.adjustSize()
        self.actual_box = id
        try:
            self.button_send_message.clicked.disconnect()
        except \
                Exception:pass
        self.button_send_message.clicked.connect(lambda: self.saveMessageClicked())
        self.loadMessages()

    def loadMessages(self):
        self.listWidget_opened_box.clear()
        for mssg in self.messages:
            itemN = QtWidgets.QListWidgetItem()
            # Create widget
            widget = QtWidgets.QWidget()
            widgetAuthor = QtWidgets.QLabel(mssg[0]+": ")
            widgetMssg = QtWidgets.QLabel(mssg[1])
            widgetLayout = QtWidgets.QHBoxLayout()
            widgetLayout.addWidget(widgetAuthor)
            widgetLayout.addWidget(widgetMssg)
            widgetLayout.addStretch()

            widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            widget.setLayout(widgetLayout)
            itemN.setSizeHint(widget.sizeHint())

            # Add widget to QListWidget funList
            self.listWidget_opened_box.addItem(itemN)
            self.listWidget_opened_box.setItemWidget(itemN, widget)

    def saveMessageClicked(self):
        self.addMessage(self.lineEdit.text(), 'Autor Jakis')
        self.lineEdit.clear()
        self.loadMessages()

    def addMessage(self, message, author): #channel id jest zmienną globalna, message - tresc wiadomosci
        self.messages.append((author, message))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Forums"))
        self.label_4.setText(_translate("MainWindow", "Channels"))
        self.label_2.setText(_translate("MainWindow", "Notes"))
        self.label_3.setText(_translate("MainWindow", "Chats"))
        self.label_opened_box.setText(_translate("MainWindow", "opened box"))
        self.button_send_message.setText(_translate("MainWindow", "send message"))
        self.button_log_out.setText(_translate("MainWindow", "log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.doSomething()
    sys.exit(app.exec_())