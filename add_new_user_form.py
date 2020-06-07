from PyQt5 import QtCore, QtGui, QtWidgets
from resources.stylesheets import *
import requests

class Ui_Form(object):
    def __init__(self, parent=None, chat_id=-1, forum_id=-1):
        self.parent = parent
        self.chat_id = chat_id
        self.forum_id = forum_id

    def setupUi(self, Form):
        self.window = Form

        Form.setObjectName("Form")
        Form.resize(350, 200)
        Form.setMinimumSize(350, 200)
        Form.setMaximumSize(350, 200)
        self.button_return = QtWidgets.QPushButton(Form)
        self.button_return.setGeometry(QtCore.QRect(20, 10, 32, 32))
        self.button_return.setObjectName("button_return")

        self.colored_line_edit = QtWidgets.QLineEdit(Form)
        self.colored_line_edit.setGeometry(QtCore.QRect(40, 100, 200, 64))
        self.colored_line_edit.setObjectName("colored_line_edit")

        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setObjectName("info_label")
        self.info_label.setGeometry(QtCore.QRect(20, 60, 300, 20))
        self.info_label.setText("Enter unique user id here:")

        self.button_add = QtWidgets.QPushButton(Form)
        self.button_add.setGeometry(QtCore.QRect(250, 100, 64, 64))
        self.button_add.setObjectName("button_add")
        self.pixmap = QtGui.QPixmap("resources/add.png")
        self.pixmap = self.pixmap.scaled(QtCore.QSize(64, 64))
        self.icon = QtGui.QIcon(self.pixmap)
        self.button_add.setIcon(self.icon)
        self.button_add.setIconSize(QtCore.QSize(64, 64))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setWindowIcon(QtGui.QIcon('resources/taco.png'))

        self.return_pixmap = QtGui.QPixmap("resources/return.png")
        self.return_pixmap = self.return_pixmap.scaled(QtCore.QSize(32, 32))
        self.icon = QtGui.QIcon(self.return_pixmap)
        self.button_return.setIcon(self.icon)
        self.button_return.setIconSize(QtCore.QSize(32, 32))
        self.button_return.setStyleSheet(button_with_image_style_sheet)

        self.window.setStyleSheet(gradient_style_sheet)
        self.button_add.setStyleSheet(button_with_image_style_sheet)
        self.colored_line_edit.setStyleSheet(colored_line_edit_style_sheet)
        self.info_label.setStyleSheet(pretty_small_label_style_sheet)

        self.button_return.clicked.connect(lambda: self.clicked_return())
        self.button_add.clicked.connect(lambda: self.clicked_add())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add user"))
        self.colored_line_edit.setText(_translate("Form", ""))

    def clicked_return(self):
        self.window.hide()

    def clicked_add(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        url = "http://localhost:86/add_user_to_chat"
        if (self.colored_line_edit.text() != "" and self.chat_id != -1):
            register_request = requests.post(url, json={"chat_id": str(self.chat_id), "permitted_user": self.colored_line_edit.text()})
            if (self.forum_id != -1):
                url = "http://localhost:86/add_user_to_forum"
                register_request = requests.post(url, json={"forum_id": str(self.forum_id),
                                                            "permitted_user": self.colored_line_edit.text()})
            print("Succes")
        else:
            print("Fail")
        self.window.hide()
        QtWidgets.QApplication.restoreOverrideCursor()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())