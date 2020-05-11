# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_buttons.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 444)
        self.example_button_blue = QtWidgets.QPushButton(Form)
        self.example_button_blue.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.example_button_blue.setStyleSheet("background-color:rgb(1, 107, 229);\n"
"color:white;\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.example_button_blue.setObjectName("example_button_blue")
        self.transparent_button = QtWidgets.QPushButton(Form)
        self.transparent_button.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.transparent_button.setStyleSheet("background: transparent;\n"
"font: 75 8pt \"SansSerif\";")
        self.transparent_button.setObjectName("transparent_button")
        self.square_button = QtWidgets.QPushButton(Form)
        self.square_button.setGeometry(QtCore.QRect(110, 270, 30, 30))
        self.square_button.setStyleSheet("background: transparent;")
        self.square_button.setObjectName("square_button")
        self.colored_line_edit = QtWidgets.QLineEdit(Form)
        self.colored_line_edit.setGeometry(QtCore.QRect(60, 340, 231, 71))
        self.colored_line_edit.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color:rgb(188, 188, 188);\n"
"font: 75 8pt \"SansSerif\";\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-radius:11px;\n"
"border-color:rgb(225, 225, 225);")
        self.colored_line_edit.setObjectName("colored_line_edit")
        self.image_button = QtWidgets.QPushButton(Form)
        self.image_button.setGeometry(QtCore.QRect(320, 140, 64, 64))
        self.image_button.setObjectName("image_button")
        self.pixmap= QtGui.QPixmap("resources/chats.png")
        self.icon = QtGui.QIcon(self.pixmap)
        self.image_button.setIcon(self.icon)
        self.image_button.setIconSize(QtCore.QSize(128, 128))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.example_button_blue.setText(_translate("Form", "PushButton"))
        self.transparent_button.setText(_translate("Form", "PushButton"))
        self.square_button.setText(_translate("Form", "F"))
        self.colored_line_edit.setText(_translate("Form", "SAMPLE TEXT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
