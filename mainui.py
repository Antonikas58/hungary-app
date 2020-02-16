# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(812, 438)
        MainWindow.setBaseSize(QtCore.QSize(700, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SAPLogon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ContinueButton = QtWidgets.QPushButton(self.centralwidget)
        self.ContinueButton.setGeometry(QtCore.QRect(220, 240, 181, 51))
        self.ContinueButton.setObjectName("ContinueButton")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(0, 46, 411, 41))
        self.label_name.setScaledContents(False)
        self.label_name.setObjectName("label_name")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(0, 100, 411, 51))
        self.label_pass.setObjectName("label_pass")
        self.label_cred = QtWidgets.QLabel(self.centralwidget)
        self.label_cred.setGeometry(QtCore.QRect(0, 180, 311, 31))
        self.label_cred.setObjectName("label_cred")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(440, 40, 281, 51))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(442, 99, 281, 51))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.SeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SeeButton.setGeometry(QtCore.QRect(740, 102, 51, 51))
        self.SeeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SeeButton.setIcon(icon1)
        self.SeeButton.setIconSize(QtCore.QSize(70, 60))
        self.SeeButton.setObjectName("SeeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hungary-tool"))
        MainWindow.setToolTip(_translate("MainWindow", "Hungary tool"))
        self.ContinueButton.setText(_translate("MainWindow", "Continue"))
        self.label_name.setText(_translate("MainWindow", "CPI User name: "))
        self.label_pass.setText(_translate("MainWindow", "CPI user password:"))
        self.label_cred.setText(_translate("MainWindow", "Credentials are empty"))
