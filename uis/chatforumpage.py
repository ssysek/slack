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
from uis.forumadd_new import Ui_NewForumWindow
from uis.chatadd_new import Ui_NewChatWindow
from uis.add_new_user_form import Ui_Form as Ui_Add_New_User

class Ui_MainWindow(object):
    def __init__(self, parent=None, logged_in_user = None):
        self.parent = parent
        self.loged_in_user = logged_in_user
        self.forums = []
        self.chats = []
        self.current_chat = -1
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.current_forum = -1
        self.users = requests.get("http://localhost:86/all_users")
        QtWidgets.QApplication.restoreOverrideCursor()
        self.forum_icons = ["resources/forums/g1.png", "resources/forums/g2.png", "resources/forums/g3.png",
                            "resources/forums/g4.png", "resources/forums/g5.png"]
        self.channel_icons = ["resources/chats/g1.png", "resources/chats/g2.png", "resources/chats/g3.png",
                              "resources/chats/g4.png", "resources/chats/g5.png"]
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
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout_4.addWidget(self.button_refresh)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.button_add_user = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_user.setObjectName("button_add_user")
        self.horizontalLayout_2.addWidget(self.button_add_user)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.button_exit_channel = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit_channel.setObjectName("button_exit_channel")
        self.horizontalLayout_2.addWidget(self.button_exit_channel)
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

        MainWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))
        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)

        self.button_log_out.setStyleSheet(button_with_image_style_sheet)
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

        self.button_refresh.setIcon((QtGui.QIcon('resources/refresh.png')))
        self.button_refresh.setIconSize(QtCore.QSize(32,32))
        self.button_refresh.setStyleSheet(button_with_image_style_sheet)
        self.button_refresh.setToolTip("Refresh")

        self.button_add_user.setIcon((QtGui.QIcon('resources/invite.png')))
        self.button_add_user.setIconSize(QtCore.QSize(32,32))
        self.button_add_user.setStyleSheet(button_with_image_style_sheet)
        self.button_add_user.setToolTip("Add new contributor")

        self.button_exit_channel.setIcon((QtGui.QIcon('resources/exit.png')))
        self.button_exit_channel.setIconSize(QtCore.QSize(32,32))
        self.button_exit_channel.setStyleSheet(button_with_image_style_sheet)
        self.button_exit_channel.setToolTip("Exit from current channel")

        self.logout_pixmap = QtGui.QPixmap("resources/logout.png")
        self.logout_pixmap = self.logout_pixmap.scaled(QtCore.QSize(36, 36))
        self.logout_icon = QtGui.QIcon(self.logout_pixmap)
        self.button_log_out.setIcon(self.logout_icon)
        self.button_log_out.setIconSize(QtCore.QSize(36, 36))
        self.button_log_out.setStyleSheet(button_with_image_style_sheet)
        self.button_log_out.setToolTip("Log out")

        self.button_log_out.clicked.connect(self.clicked_log_out)
        self.button_return.clicked.connect(self.clicked_return)
        self.button_exit_channel.clicked.connect(lambda: self.clicked_exit_channel())
        self.button_add_user.clicked.connect(lambda: self.clicked_add_user())
        self.button_refresh.clicked.connect(lambda: self.refresh())

        self.actual_box = None
        self.messages = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Forums"))
        self.label_4.setText(_translate("MainWindow", "Channels"))
        self.label_2.setText(_translate("MainWindow", "Notes"))
        self.label_3.setText(_translate("MainWindow", "Chats"))
        self.label_opened_box.setText(_translate("MainWindow", "Open chat:"))
        self.button_send_message.setText(_translate("MainWindow", "send message"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat"))



    def loadPrivateChatsForUser(self):
        """ function loading channels which have user_id assigned to
         them but thier forum_id is null"""
        url = "http://localhost:86/user_chats?user_id="
        url += str(1)
        messages = requests.post(url).json()
        res = ["no_forum", -1, []]
        for i in messages:
            res[2].append(str(i["chat_id"]))
        return res

    def refresh(self):
        """refreshes current channel view"""
        self.loadMessagesFromDataBase(self.current_chat)
        self.loadMessages()


    def sendNewMessage(self):
        """sends new message to database and reloads current message view"""
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        url = "http://localhost:86/add_new_post"
        if (self.lineEdit.text() != ""):
            register_request = requests.post(url,
                                             json={"owner_id": self.loged_in_user[0], "chat_id": self.current_chat,
                                                   "post_content": self.lineEdit.text()})
        self.loadMessagesFromDataBase(self.current_chat)
        self.loadMessages()
        QtWidgets.QApplication.restoreOverrideCursor()

    def collectDataFromDataBase(self):
        """initiates data for forum and channel"""
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.forums = self.loadForumsFromDataBase()
        self.changeForumButtons(self.listWidget_forums, self.forums)

        self.chats = self.loadPrivateChatsForUser()
        self.changeChannelButtons(self.listWidget_chats, self.chats)
        QtWidgets.QApplication.restoreOverrideCursor()

    def changeForumButtons(self, nameWidget, objects):
        """
        changes buttons for forums based on data loaded in collectDataFromDataBase()
        :param nameWidget: list widget for forum
        :param objects: list of forum data elements containing  [forum_name, forum_id, [forum chats id]]
        :return:
        """
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
            nameWidget.addItem(itemN)
            nameWidget.setItemWidget(itemN, widget)
        itemN = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widgetButton = self.addForumButton()
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())
        # Add widget to QListWidget funList
        nameWidget.addItem(itemN)
        nameWidget.setItemWidget(itemN, widget)

    def clicked_newForum(self):
        """opens window for creating new forum in database"""
        print("adding new forum")
        self.addforum_window = QtWidgets.QMainWindow()
        self.addforum_window_ui = Ui_NewForumWindow(self, self.loged_in_user)
        self.addforum_window_ui.setupUi(self.addforum_window)

        self.window.hide()
        self.addforum_window.show()


#TODO: podmienić na forum icon zgadzający się z bazą
    def getForumWidgetButton(self, object):
        """creates widget for single forum button
        :param object -- [forum name, forum id, [forum chats]]
        """
        widgetButton = QtWidgets.QPushButton()
        widgetButton.setToolTip(object[0])
        widgetButton_pixmap = QtGui.QPixmap(self.forum_icons[0])
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)
        widgetButton.clicked.connect(lambda: self.changeChannelButtons(self.listWidget_chanells, object))
        return widgetButton

    def addForumButton(self):
        """creates button for new window for crating new forum"""
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/add.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)
        widgetButton.clicked.connect(self.clicked_newForum)
        return widgetButton

    def addChatButton(self, forum_id):
        """creates button for new window for crating new forum
        :param forum_id: -1 when private chat, valid id otherwise
        """
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/add.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)

        widgetButton.clicked.connect(lambda: self.clickednewChat(forum_id))
        return widgetButton

    def clickednewChat(self, forum_id):
        """opens window for creating new chat in database
        :param forum_id: -1 when private chat, valid id otherwise
        """
        print("adding new chat")
        print(self.current_chat)
        print(self.current_forum)
        print(forum_id)
        self.addchat_window = QtWidgets.QMainWindow()
        self.addchat_window_ui = Ui_NewChatWindow(self, self.loged_in_user, forum_id)
        self.addchat_window_ui.setupUi(self.addchat_window)

        self.window.hide()
        self.addchat_window.show()


    def changeChannelButtons(self, nameWidget, objects):
        """
        changes buttons for channels depending on forum which is active in current moment
        :param nameWidget: list widget for private chats od forum chats
        :param objects: list of forum data elements containing  [forum_name, forum_id, [forum chats id]]
        """
        nameWidget.clear()
        self.current_forum = objects[1]
        try:
            for object in objects[len(objects)-1]:
                itemN = QtWidgets.QListWidgetItem()
                widget = QtWidgets.QWidget()
                chanel_info = [objects[1], object]
                widgetButton = self.getChannelWidgetButton(chanel_info)
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
        widgetButton = self.addChatButton(objects[1])
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())
        # Add widget to QListWidget funList
        nameWidget.addItem(itemN)
        nameWidget.setItemWidget(itemN, widget)

    def getChannelWidgetButton(self, channel_info):
        """
        Creates button for channel and connects it to setup current messages viewer to show its content
        :param channel_info: [forum_id, channel_id]
        :return QtWidgets.QPushButton object
        """
        object = channel_info[1]
        widgetButton = QtWidgets.QPushButton()
        widgetButton_pixmap = QtGui.QPixmap("resources/messages/m1.png")
        widgetButton_pixmap = widgetButton_pixmap.scaled(QtCore.QSize(32, 32))
        widgetButtonicon = QtGui.QIcon(widgetButton_pixmap)
        widgetButton.setIcon(widgetButtonicon)
        widgetButton.setIconSize(QtCore.QSize(32, 32))
        widgetButton.setStyleSheet(button_with_image_style_sheet)
        widgetButton.setToolTip(object)
        widgetButton.clicked.connect(lambda: self.setUpMessages(channel_info))
        return widgetButton

    def goToNotes(self):
        """
        opens view for notes storage
        :return: void
        """
        print("Go to notes")
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesWindow(self, self.loged_in_user)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()

    def setUpMessages(self, channel_info):  # arg - name of channel, id - id channel
        """
        setups view of messages for chosen channel
        try except to pass on channels without content
        :param channel_info: [forum_id, channel_id]
        :return: void
        """
        self.current_forum = channel_info[0]
        self.loadMessagesFromDataBase(channel_info[1])
        self.current_chat = channel_info[1]
        self.label_opened_box.setText(channel_info[1] + ":")
        self.label_opened_box.adjustSize()
        self.actual_box = channel_info[1]
        try:
            self.button_send_message.clicked.disconnect()
        except \
                Exception:
            pass
        self.button_send_message.clicked.connect(lambda: self.saveMessageClicked())
        self.loadMessages()

    def loadMessages(self):
        """
        fills listWidget_opened_box with messages from chosen channel/chat
        :return: void
        """
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
        """
        adds new message to database, reloads main box of messages
        :return: void
        """
        self.sendNewMessage()
        self.lineEdit.clear()
        self.loadMessages()


    def clicked_return(self):
        """
        hides current windows shows parent
        :return: void
        """
        self.parent.window.show()
        self.window.hide()

    def clicked_log_out(self):
        """
        iterates back to the begining of program to show first window
        :return: void
        """
        self.show_site = self.parent
        while (self.show_site.parent != None):
            self.show_site = self.show_site.parent

        self.show_site.window.show()
        self.window.hide()

    def loadMessagesFromDataBase(self, chat_id):
        """
        loads messages from database based on chat_id provided
        :param chat_id: unique identifier for chats
        :return: void
        """
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
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
        QtWidgets.QApplication.restoreOverrideCursor()

    def loadForumsFromDataBase(self):
        """
        loads forums from database based on current user
        :return: void
        """
        url = "http://localhost:86/user_forums?permitted_user="
        url += str(self.loged_in_user[0])
        result = []
        forums = requests.post(url).json()
        for i in forums:
            chats = self.loadChatsForForum(i["forum_id"])
            result.append([i["forum_name"], i["forum_id"], chats])
        return result


    def loadChatsForForum(self, forum_id):
        """
        loads chats from database based on selected forum
        :param forum_id: unique forum id from database
        :return: void
        """
        url = "http://localhost:86/chats_inside_forum?upper_forum_id="
        url += str(forum_id)
        message = requests.post(url).json()
        res = []
        for i in message:
            res.append(str(i["chat_id"]))
        return res

#TODO: podpiąć do wychodzenia z bazy, nie ma jeszcze endpointa
    def clicked_exit_channel(self):
        """
        removes user from permmisions for channel
        :return: void
        """
        print(self.loged_in_user)
        print(self.current_chat)

    def clicked_add_user(self):
        """
        creates window for addition of new members to channel/chat
        :return: void
        """
        self.adduser_window = QtWidgets.QWidget()
        self.adduser_window_ui = Ui_Add_New_User(self, self.current_chat, self.current_forum)
        self.adduser_window_ui.setupUi(self.adduser_window)
        self.adduser_window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.collectDataFromDataBase()
    sys.exit(app.exec_())