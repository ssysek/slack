# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_forum_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from uis.resources.stylesheets import *

from uis.notesmainpage import Ui_MainNotesWindow


class Ui_MainWindow(object):
    def __init__(self, parent=None, logged_in_user = None):
        self.parent = parent
        self.loged_in_user = logged_in_user
        self.forums = []
        self.chats = []

    def setupUi(self, MainWindow):
        self.window = MainWindow

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
        self.button_notes = QtWidgets.QPushButton(self.centralwidget)
        self.button_notes.setObjectName("button_go_to_notes")
        self.gridLayout.addWidget(self.button_notes, 4, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

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
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_4.addWidget(self.button_return)
        spacerItem = QtWidgets.QSpacerItem(140, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_opened_box = QtWidgets.QLabel(self.centralwidget)
        self.label_opened_box.setObjectName("label_opened_box")
        self.horizontalLayout_4.addWidget(self.label_opened_box)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)

        self.button_log_out.setStyleSheet(button_for_logging_style_sheet)
        self.button_send_message.setStyleSheet(button_for_logging_style_sheet)
        self.lineEdit.setStyleSheet(colored_line_edit_style_sheet)
        self.label.setStyleSheet(pretty_small_label_style_sheet)
        self.label_2.setStyleSheet(pretty_small_label_style_sheet)
        self.label_3.setStyleSheet(pretty_small_label_style_sheet)
        self.label_4.setStyleSheet(pretty_small_label_style_sheet)
        self.label_opened_box.setStyleSheet(pretty_big_label_style_sheet)


        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32,32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.button_return.setIcon(self.icon)
        self.button_return.setIconSize(QtCore.QSize(32, 32))
        self.button_return.setStyleSheet(button_with_image_style_sheet)


        self.button_notes.setIcon(QtGui.QIcon('resources/notes.png'))
        self.button_notes.setIconSize(QtCore.QSize(100, 100))
        self.button_notes.setStyleSheet(button_with_image_style_sheet)
        self.button_notes.clicked.connect(self.goToNotes)



        self.button_log_out.clicked.connect(self.clicked_log_out)
        self.button_return.clicked.connect(self.clicked_return)


        self.actual_box = None
        self.messages = []


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Forums"))
        self.label_4.setText(_translate("MainWindow", "Channels"))
        self.label_2.setText(_translate("MainWindow", "Notes"))
        self.label_3.setText(_translate("MainWindow", "Chats"))
        self.label_opened_box.setText(_translate("MainWindow", "Open chat:"))
        self.button_send_message.setText(_translate("MainWindow", "send message"))
        self.button_log_out.setText(_translate("MainWindow", "LogOut"))

    def loadPrivateChatsForUser(self):
        url = "http://localhost:86/user_chats?user_id="
        url +=str(1)
        messages = requests.post(url).json()
        res = []
        for i in messages:
            res.append(str(i["chat_id"]))
        return res

#    insert    into    posts    values(1, 1, 1, 'Lorem ipsum');
# TODO: podmienić hard coded chat_id na aktualny chat_id
    def sendNewMessage(self):
        url = "http://localhost:86/add_new_post"
        if(self.lineEdit.text()!=""):
            register_request = requests.post(url,
                                             json={"owner_id": self.loged_in_user[0], "chat_id": 2, "post_content": self.lineEdit.text()})

    def doSomething(self):
        self.forums = self.loadForumsFromDataBase()
        self.changeForumButtons(self.listWidget_forums, self.forums)

        self.chats = self.loadPrivateChatsForUser()
        self.changeChannelButtons(self.listWidget_chats, self.chats)


        # statycznie załadowane messages z chatu nr 1
        self.loadMessagesFromDataBase(2)




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
        widgetButton.setStyleSheet(button_small_blue_style_sheet)

        # TODO podmienić na ładowanie z bazy
        widgetButton.clicked.connect(lambda: self.changeChannelButtons(self.listWidget_chanells, object[1]))
        return widgetButton


    def changeChannelButtons(self, nameWidget, list):
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
        widgetButton.setStyleSheet(button_small_blue_style_sheet)
        widgetButton.clicked.connect(lambda: self.setUpMessages(object, object))
        return widgetButton

    def getNotesWidgetButton(self, object):
        widgetButton = QtWidgets.QPushButton(object)

        widgetButton.clicked.connect(lambda: self.printSecond('1'))
        return widgetButton


    def goToNotes(self):
        print("Go to notes")
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesWindow(self, self.loged_in_user)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()

    def setUpMessages(self, arg, id): #arg - name of channel, id - id channel

        #TODO: podmienić na konkretne channels, nie jeden statyczny
        self.loadMessagesFromDataBase(2)

        self.label_opened_box.setText(arg+ ":")
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
        self.sendNewMessage()
        self.lineEdit.clear()
        self.loadMessages()

    def addMessage(self, message, author): #channel id jest zmienną globalna, message - tresc wiadomosci
        self.messages.append((author, message))



    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()


    #iterates back to the begining of program to show first window
    def clicked_log_out(self):
        self.show_site = self.parent
        while(self.show_site.parent != None):
            self.show_site = self.show_site.parent

        self.show_site.window.show()
        self.window.hide()


    def loadMessagesFromDataBase(self, chat_id):
        url = "http://localhost:86/get_all_posts_at_chats?chat_id="
        url +=str(chat_id)
        messages = requests.post(url)
        users = requests.get("http://localhost:86/all_users")
        user_ids = [(i["user_id"], str(i["user_name"]) + " " + str(i["user_surname"])) for i in users.json()]
        messages_to_print = []
        for i in messages.json():
            message_has_owner = False
            for j in user_ids:
                if (j[0] == i["user_id"]):
                    messages_to_print.append((j[1], i["post_content"]))
                    message_has_owner = True
                    break
            if (not message_has_owner):
                messages_to_print.append(("Unkown", i["post_content"]))
        self.messages = messages_to_print

    def loadForumsFromDataBase(self):
        url = "http://localhost:86/user_forums?permitted_user="
        url += str(self.loged_in_user[0])
        result = []
        forums = requests.post(url).json()
        print(forums)
        for i in forums:
            chats = self.loadChatsForForum(i["forum_id"])
            print(chats)
            result.append([i["forum_name"], chats])
        return result

    def loadChatsForForum(self, forum_id):
        url = "http://localhost:86/chats_inside_forum?upper_forum_id="
        url += str(forum_id)
        message = requests.post(url).json()
        res = []
        for i in message:
            res.append(str(i["chat_id"]))
        return res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.doSomething()
    ui.loadMessagesFromDataBase(2)
    sys.exit(app.exec_())