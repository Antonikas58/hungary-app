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
        MainWindow.resize(411, 327)
        MainWindow.setBaseSize(QtCore.QSize(700, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SAPLogon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow::separator\n"
"{\n"
"    background-color: #323232;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #76797C;\n"
"    spacing: 2px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    selection-background-color:#323232;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    border: 0px\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_ping = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_ping.setFont(font)
        self.label_ping.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_ping.setText("")
        self.label_ping.setObjectName("label_ping")
        self.gridLayout_2.addWidget(self.label_ping, 5, 4, 1, 1)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}")
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.gridLayout_2.addWidget(self.lineEdit_pass, 1, 2, 1, 2)
        self.SeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SeeButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.SeeButton.setIconSize(QtCore.QSize(55, 45))
        self.SeeButton.setFlat(True)
        self.SeeButton.setObjectName("SeeButton")
        self.gridLayout_2.addWidget(self.SeeButton, 1, 4, 1, 1)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_name.setScaledContents(False)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 2, 1, 2)
        self.lineEdit_addr = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_addr.setFont(font)
        self.lineEdit_addr.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}")
        self.lineEdit_addr.setObjectName("lineEdit_addr")
        self.gridLayout_2.addWidget(self.lineEdit_addr, 3, 1, 3, 3)
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_pass.setFont(font)
        self.label_pass.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_pass.setObjectName("label_pass")
        self.gridLayout_2.addWidget(self.label_pass, 1, 0, 1, 2)
        self.label_cred = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_cred.setFont(font)
        self.label_cred.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_cred.setObjectName("label_cred")
        self.gridLayout_2.addWidget(self.label_cred, 2, 0, 2, 2)
        self.label_tenant = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_tenant.setFont(font)
        self.label_tenant.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_tenant.setObjectName("label_tenant")
        self.gridLayout_2.addWidget(self.label_tenant, 4, 0, 1, 1)
        self.ContinueButton = QtWidgets.QPushButton(self.centralwidget)
        self.ContinueButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.ContinueButton.setObjectName("ContinueButton")
        self.gridLayout_2.addWidget(self.ContinueButton, 6, 4, 1, 1)
        self.PingButton = QtWidgets.QPushButton(self.centralwidget)
        self.PingButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.PingButton.setObjectName("PingButton")
        self.gridLayout_2.addWidget(self.PingButton, 6, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 22))
        self.menubar.setStyleSheet("QMenuBar\n"
"{\n"
"    background-color: #323232;\n"
"    color: #D1DBCB;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: #323232;\n"
"    background: transparent;\n"
"    /* padding: 2px 20px 2px 20px; */\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    /* border: 1px solid #76797C; */\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 0px solid #76797C;\n"
"    background-color: #D1DBCB;\n"
"    color: #000;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar::item {\n"
"    border: 0px transparent dark;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
" }")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hungary-tool"))
        MainWindow.setToolTip(_translate("MainWindow", "Hungary tool"))
        self.lineEdit_pass.setToolTip(_translate("MainWindow", "<html><head/><body><p>password for specified user name</p></body></html>"))
        self.SeeButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>check password</p></body></html>"))
        self.SeeButton.setText(_translate("MainWindow", "Show"))
        self.label_name.setText(_translate("MainWindow", "CPI User name: "))
        self.lineEdit_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>name of tenant user</p></body></html>"))
        self.lineEdit_addr.setToolTip(_translate("MainWindow", "<html><head/><body><p>address of deployed Hungarian API iflow </p></body></html>"))
        self.label_pass.setText(_translate("MainWindow", "CPI user password:"))
        self.label_cred.setText(_translate("MainWindow", "Credentials are empty"))
        self.label_tenant.setText(_translate("MainWindow", "Iflow address:"))
        self.ContinueButton.setText(_translate("MainWindow", "Continue"))
        self.PingButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Perform the check of connection with specified iflow with current credentials</p></body></html>"))
        self.PingButton.setText(_translate("MainWindow", "Ping Tenant"))
