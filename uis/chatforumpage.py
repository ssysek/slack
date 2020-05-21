# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatforumpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.users = requests.get("http://localhost:86/all_users")

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_right_bar = QtWidgets.QVBoxLayout()
        self.verticalLayout_right_bar.setObjectName("verticalLayout_right_bar")
        self.verticalLayout_channels = QtWidgets.QVBoxLayout()
        self.verticalLayout_channels.setObjectName("verticalLayout_channels")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_channels.addWidget(self.label_4)
        self.listWidget_chanells = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_chanells.setObjectName("listWidget_chanells")
        self.verticalLayout_channels.addWidget(self.listWidget_chanells)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_channels.addItem(spacerItem)
        self.verticalLayout_chats = QtWidgets.QVBoxLayout()
        self.verticalLayout_chats.setObjectName("verticalLayout_chats")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_chats.addWidget(self.label_3)
        self.listWidget_chats = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_chats.setObjectName("listWidget_chats")
        self.verticalLayout_chats.addWidget(self.listWidget_chats)
        self.verticalLayout_channels.addLayout(self.verticalLayout_chats)
        self.verticalLayout_right_bar.addLayout(self.verticalLayout_channels)
        self.gridLayout.addLayout(self.verticalLayout_right_bar, 2, 1, 4, 1)
        self.verticalLayout_left_bar = QtWidgets.QVBoxLayout()
        self.verticalLayout_left_bar.setObjectName("verticalLayout_left_bar")
        self.verticalLayout_notes = QtWidgets.QVBoxLayout()
        self.verticalLayout_notes.setObjectName("verticalLayout_notes")
        self.verticalLayout_forums = QtWidgets.QVBoxLayout()
        self.verticalLayout_forums.setObjectName("verticalLayout_forums")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_forums.addWidget(self.label)
        self.listWidget_forums = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_forums.setObjectName("listWidget_forums")
        self.verticalLayout_forums.addWidget(self.listWidget_forums)
        self.verticalLayout_notes.addLayout(self.verticalLayout_forums)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_notes.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_notes.addWidget(self.label_2)
        self.button_notes = QtWidgets.QPushButton(self.centralwidget)
        self.button_notes.setObjectName("button_notes")
        self.verticalLayout_notes.addWidget(self.button_notes)
        self.verticalLayout_left_bar.addLayout(self.verticalLayout_notes)
        self.gridLayout.addLayout(self.verticalLayout_left_bar, 2, 0, 4, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_4.addWidget(self.button_return)
        spacerItem2 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_opened_box = QtWidgets.QLabel(self.centralwidget)
        self.label_opened_box.setObjectName("label_opened_box")
        self.horizontalLayout_4.addWidget(self.label_opened_box)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.button_log_out = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_log_out.sizePolicy().hasHeightForWidth())
        self.button_log_out.setSizePolicy(sizePolicy)
        self.button_log_out.setObjectName("button_log_out")
        self.horizontalLayout_4.addWidget(self.button_log_out)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(0, 15)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 4, 1)
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
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
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
        url += str(1)
        messages = requests.post(url).json()
        res = [-1, []]
        for i in messages:
            res[1].append(str(i["chat_id"]))
        return res

    #    insert    into    posts    values(1, 1, 1, 'Lorem ipsum');
    # TODO: podmienić hard coded chat_id na aktualny chat_id
    def sendNewMessage(self):
        url = "http://localhost:86/add_new_post"
        if (self.lineEdit.text() != ""):
            register_request = requests.post(url,
                                             json={"owner_id": self.loged_in_user[0], "chat_id": 2,
                                                   "post_content": self.lineEdit.text()})
        self.loadMessagesFromDataBase(2)
        self.loadMessages()

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
        itemN = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widgetButton = self.addButton(objects)
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
        widgetButton = QtWidgets.QPushButton()
        widgetButton.setToolTip(object[0])
        widgetButton_pixmap = QtGui.QPixmap("resources/groups/g1.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)
        widgetButton.clicked.connect(lambda: self.changeChannelButtons(self.listWidget_chanells, object))
        return widgetButton

    def addButton(self, object):
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/add.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)

        widgetButton.clicked.connect(lambda:self.createChannel(object))
        return widgetButton


    def addChannelButton(self, object):
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/add.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)

        widgetButton.clicked.connect(lambda: self.createChannel(object))
        return widgetButton

    def createChannel(self, object):
        print(object)

    def changeChannelButtons(self, nameWidget, objects):
        nameWidget.clear()
        try:
            for object in objects[len(objects)-1]:
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
        except Exception:
            pass
        itemN = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widgetButton = self.addChannelButton(objects)
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
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/messages/m1.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)
        widgetButton.setToolTip(object)
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

    def setUpMessages(self, arg, id):  # arg - name of channel, id - id channel
        # TODO: podmienić na konkretne channels, nie jeden statyczny
        self.loadMessagesFromDataBase(id)

        self.label_opened_box.setText(arg + ":")
        self.label_opened_box.adjustSize()
        self.actual_box = id
        try:
            self.button_send_message.clicked.disconnect()
        except \
                Exception:
            pass
        self.button_send_message.clicked.connect(lambda: self.saveMessageClicked())
        self.loadMessages()

    def loadMessages(self):
        self.listWidget_opened_box.clear()
        for mssg in self.messages:
            itemN = QtWidgets.QListWidgetItem()
            # Create widget
            widget = QtWidgets.QWidget()
            widgetAuthor = QtWidgets.QLabel(mssg[0] + ": ")
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

    def addMessage(self, message, author):  # channel id jest zmienną globalna, message - tresc wiadomosci
        self.messages.append((author, message))

    def clicked_return(self):
        self.parent.window.show()
        self.window.hide()

    # iterates back to the begining of program to show first window
    def clicked_log_out(self):
        self.show_site = self.parent
        while (self.show_site.parent != None):
            self.show_site = self.show_site.parent

        self.show_site.window.show()
        self.window.hide()

    def loadMessagesFromDataBase(self, chat_id):
        url = "http://localhost:86/get_all_posts_at_chats?chat_id="
        url += str(chat_id)
        messages = requests.post(url)
        user_ids = [(i["user_id"], str(i["user_name"]) + " " + str(i["user_surname"])) for i in self.users.json()]
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
        for i in forums:
            chats = self.loadChatsForForum(i["forum_id"])
            result.append([i["forum_name"], i["forum_id"], chats])
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