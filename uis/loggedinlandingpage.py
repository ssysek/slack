# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loggedinlandingpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from uis.features import Ui_FeaturesWindow
from uis.contactpage import Ui_ContactWindow
from uis.notesmainpage import Ui_MainNotesWindow
from uis.registrationpage_new import Ui_RegistrationWindow
from uis.chatforumpage import Ui_MainWindow as Ui_ChatWindow
from uis.about import Ui_MainWindow as Ui_AboutWindow
from uis.resources.stylesheets import *


class Ui_MainWindow(object):
    def __init__(self, parent=None, user=None):
        self.parent = parent
        self.logged_in_user = user

    def setupUi(self, MainWindow):
        self.window = MainWindow

        MainWindow.setObjectName("Talco")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setObjectName("button_home")
        self.horizontalLayout_3.addWidget(self.button_home)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_contact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_contact.sizePolicy().hasHeightForWidth())
        self.button_contact.setSizePolicy(sizePolicy)
        self.button_contact.setObjectName("button_contact")
        self.horizontalLayout.addWidget(self.button_contact)
        self.button_about = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_about.sizePolicy().hasHeightForWidth())
        self.button_about.setSizePolicy(sizePolicy)
        self.button_about.setObjectName("button_about")
        self.horizontalLayout.addWidget(self.button_about)
        self.button_features = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_features.sizePolicy().hasHeightForWidth())
        self.button_features.setSizePolicy(sizePolicy)
        self.button_features.setObjectName("button_features")
        self.horizontalLayout.addWidget(self.button_features)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout.addWidget(self.label_username)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.button_log_out = QtWidgets.QPushButton(self.centralwidget)
        self.button_log_out.setObjectName("button_log_out")
        self.horizontalLayout_2.addWidget(self.button_log_out)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(2, 15)
        self.horizontalLayout_3.setStretch(3, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_main_text = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_main_text.sizePolicy().hasHeightForWidth())
        self.label_main_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_main_text.setFont(font)
        self.label_main_text.setScaledContents(False)
        self.label_main_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_main_text.setObjectName("label_main_text")
        self.gridLayout.addWidget(self.label_main_text, 1, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 4, 1, 1)
        self.label_description = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_description.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_description.setFont(font)
        self.label_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_description.setObjectName("label_description")
        self.gridLayout.addWidget(self.label_description, 2, 1, 1, 3)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("example_photo.jpg"))
        self.label_image.setScaledContents(True)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 1, 5, 6, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem10, 3, 1, 1, 1)
        self.button_open_chats = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_chats.setObjectName("button_open_chats")
        self.gridLayout.addWidget(self.button_open_chats, 4, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem11, 5, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem12, 3, 2, 1, 1)
        self.butto_open_notes = QtWidgets.QPushButton(self.centralwidget)
        self.butto_open_notes.setObjectName("butto_open_notes")
        self.gridLayout.addWidget(self.butto_open_notes, 5, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem13, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
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

        MainWindow.setWindowIcon(QtGui.QIcon('resources/taco.png'))
        MainWindow.setStyleSheet(gradient_style_sheet)
        self.centralwidget.setStyleSheet(transparent_background_style_sheet)

        self.butto_open_notes.setStyleSheet(button_big_blue_style_sheet)
        self.button_open_chats.setStyleSheet(button_big_blue_style_sheet)
        self.button_features.setStyleSheet(small_label_style_sheet)
        self.button_contact.setStyleSheet(small_label_style_sheet)
        self.button_about.setStyleSheet(small_label_style_sheet)
        self.label.setStyleSheet(small_label_style_sheet)
        self.label_username.setStyleSheet(small_label_style_sheet)

        self.logout_pixmap = QtGui.QPixmap("resources/logout.png")
        self.logout_pixmap = self.logout_pixmap.scaled(QtCore.QSize(36, 36))
        self.logout_icon = QtGui.QIcon(self.logout_pixmap)
        self.button_log_out.setIcon(self.logout_icon)
        self.button_log_out.setIconSize(QtCore.QSize(36, 36))
        self.button_log_out.setStyleSheet(button_with_image_style_sheet_colored_font)
        self.button_log_out.setText("Log out")

        self.home_pixmap = QtGui.QPixmap("resources/home.png")
        self.home_pixmap = self.home_pixmap.scaled(QtCore.QSize(40, 40))
        self.icon = QtGui.QIcon(self.home_pixmap)
        self.button_home.setIcon(self.icon)
        self.button_home.setIconSize(QtCore.QSize(40, 40))
        self.button_home.setStyleSheet(button_with_image_style_sheet)

        self.button_about.clicked.connect(self.clicked_about)
        self.button_contact.clicked.connect(self.clicked_contact)
        self.button_features.clicked.connect(self.clicked_features)
        self.button_home.clicked.connect(self.clicked_home)
        self.button_log_out.clicked.connect(self.clicked_log_out)
        self.button_open_chats.clicked.connect(self.clicked_open_chats)
        self.butto_open_notes.clicked.connect(self.clicked_open_notes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.button_contact.setText(_translate("MainWindow", "Contact"))
        self.button_about.setText(_translate("MainWindow", "About"))
        self.button_features.setText(_translate("MainWindow", "Features"))
        self.label.setText(_translate("MainWindow", "Hello: "))
        self.label_username.setText(_translate("MainWindow", "username"))
        self.label_main_text.setText(_translate("MainWindow", "<html><head/><body><p>Communicate and </p><p>learn easier.</p></body></html>"))
        self.label_description.setText(_translate("MainWindow", "<html><head/><body><p>A web app that makes communication simpler and</p><p>work more productive.</p></body></html>"))
        self.button_open_chats.setText(_translate("MainWindow", "Open chats"))
        self.butto_open_notes.setText(_translate("MainWindow", "Open notes"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Talco"))

    def clicked_about(self):
        """
        opens up new window with information about team
        :return: void
        """
        self.about_window = QtWidgets.QMainWindow()
        self.about_window_ui = Ui_AboutWindow(self)
        self.about_window_ui.setupUi(self.about_window)

        self.about_window.show()
        self.window.hide()

    def clicked_contact(self):
        """
        opens contact page
        :return: void
        """
        self.contact_window = QtWidgets.QMainWindow()
        self.contact_window_ui = Ui_ContactWindow(self, self.logged_in_user)
        self.contact_window_ui.setupUi(self.contact_window)

        self.contact_window.show()

    def clicked_create_account(self):
        """
        opens create account page
        :return: void
        """
        self.register_window = QtWidgets.QMainWindow()
        self.register_window_ui = Ui_RegistrationWindow(self)
        self.register_window_ui.setupUi(self.register_window)

        self.register_window.show()

    def clicked_features(self):
        """
        opens features page
        :return: void
        """
        self.features_window = QtWidgets.QMainWindow()
        self.features_window_ui = Ui_FeaturesWindow(self,self.logged_in_user)
        self.features_window_ui.setupUi(self.features_window)

        self.window.hide()
        self.features_window.show()


    def clicked_home(self):
        pass
    def clicked_log_out(self):
        """
        goes back to unloged in page
        :return: void
        """
        self.window.hide()
        self.parent.window.show()

    def clicked_open_chats(self):
        """
        opens chatforumpage
        :return: void
        """
        self.main_window = QtWidgets.QMainWindow()
        self.main_window_ui = Ui_ChatWindow(self, self.logged_in_user)
        self.main_window_ui.setupUi(self.main_window)
        self.main_window_ui.collectDataFromDataBase()
        self.main_window.show()
        self.window.hide()

    def clicked_open_notes(self):
        """
        opens notespage
        :return: void
        """
        self.notes_window = QtWidgets.QMainWindow()
        self.notes_window_ui = Ui_MainNotesWindow(self, self.logged_in_user)
        self.notes_window_ui.setupUi(self.notes_window)

        self.window.hide()
        self.notes_window.show()


    def change_username(self, name):
        """
            called by login or register, updates label_username
            resize label_username, not to scale up whole window size on long names
        :param name: new name of loged in user
        :return: void
        """
        self.label_username.setMaximumWidth(int(self.window.geometry().width()/4))
        self.label_username.setText(name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginpageWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(LoginpageWindow)
    LoginpageWindow.show()
    sys.exit(app.exec_())