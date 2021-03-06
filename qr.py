# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 200)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_url.setGeometry(QtCore.QRect(20, 30, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_url.setFont(font)
        self.lbl_url.setObjectName("lbl_url")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setGeometry(QtCore.QRect(80, 30, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_url.setFont(font)
        self.txt_url.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color: #2B244F;\n"
"}\n"
"QLineEdit::hover{\n"
"border: 3px solid rgb(40, 40, 40);\n"
"border-radius: 10px;\n"
"}")
        self.txt_url.setObjectName("txt_url")
        self.btn_qr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_qr.setGeometry(QtCore.QRect(90, 100, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_qr.setFont(font)
        self.btn_qr.setStyleSheet("QPushButton{\n"
"background-color: black;\n"
"color: #FFF;;\n"
"border-radius: 20px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(44, 44, 44);\n"
"color: rgb(227, 227, 227);\n"
"\n"
"}")
        self.btn_qr.setObjectName("btn_qr")
        self.lbl_qr = QtWidgets.QLabel(self.centralwidget)
        self.lbl_qr.setGeometry(QtCore.QRect(160, 160, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_qr.setFont(font)
        self.lbl_qr.setText("")
        self.lbl_qr.setObjectName("lbl_qr")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(350, 35, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background-color: transparent;\n"
"color: black;\n"
"}\n"
"QPushButton::hover{\n"
"cursor: pointer;\n"
"}")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(270, 100, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton{\n"
"background-color: black;\n"
"color: #FFF;;\n"
"border-radius: 20px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(44, 44, 44);\n"
"color: rgb(227, 227, 227);\n"
"\n"
"}")
        self.btn_save.setObjectName("btn_save")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_url.setText(_translate("MainWindow", "URL:"))
        self.btn_qr.setText(_translate("MainWindow", "Generate QR"))
        self.btn_clear.setText(_translate("MainWindow", "clear"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
