# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildWindow(object):
    def setupUi(self, ChildWindow):
        ChildWindow.setObjectName("ChildWindow")
        ChildWindow.resize(595, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SAPLogon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChildWindow.setWindowIcon(icon)
        ChildWindow.setStyleSheet("QMainWindow::separator\n"
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
"}")
        self.centralwidget = QtWidgets.QWidget(ChildWindow)
        self.centralwidget.setStyleSheet("\n"
"QWidget\n"
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.getTaxpayerTab = QtWidgets.QWidget()
        self.getTaxpayerTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getTaxpayerTab.setMouseTracking(False)
        self.getTaxpayerTab.setStyleSheet("\n"
"QWidget\n"
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
        self.getTaxpayerTab.setObjectName("getTaxpayerTab")
        self.formLayout = QtWidgets.QFormLayout(self.getTaxpayerTab)
        self.formLayout.setObjectName("formLayout")
        self.label_tax_id = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_tax_id.setFont(font)
        self.label_tax_id.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_tax_id.setObjectName("label_tax_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id)
        self.lineEdit_tax_id = QtWidgets.QLineEdit(self.getTaxpayerTab)
        self.lineEdit_tax_id.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_tax_id.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_tax_id.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_tax_id.setText("")
        self.lineEdit_tax_id.setObjectName("lineEdit_tax_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id)
        self.label_check_id = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_check_id.setFont(font)
        self.label_check_id.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_check_id.setObjectName("label_check_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_check_id)
        self.lineEdit_check_id = QtWidgets.QLineEdit(self.getTaxpayerTab)
        self.lineEdit_check_id.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_check_id.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_check_id.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_check_id.setText("")
        self.lineEdit_check_id.setObjectName("lineEdit_check_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_check_id)
        self.tabWidget.addTab(self.getTaxpayerTab, "")
        self.checkInvoiceTab = QtWidgets.QWidget()
        self.checkInvoiceTab.setStyleSheet("\n"
"QWidget\n"
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
        self.checkInvoiceTab.setObjectName("checkInvoiceTab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.checkInvoiceTab)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_tax_id_check = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_tax_id_check.setFont(font)
        self.label_tax_id_check.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_tax_id_check.setObjectName("label_tax_id_check")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id_check)
        self.lineEdit_tax_id_check = QtWidgets.QLineEdit(self.checkInvoiceTab)
        self.lineEdit_tax_id_check.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_tax_id_check.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_tax_id_check.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_tax_id_check.setText("")
        self.lineEdit_tax_id_check.setObjectName("lineEdit_tax_id_check")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id_check)
        self.label_inv_num_check = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_inv_num_check.setFont(font)
        self.label_inv_num_check.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_inv_num_check.setObjectName("label_inv_num_check")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_inv_num_check)
        self.lineEdit_inv_num_check = QtWidgets.QLineEdit(self.checkInvoiceTab)
        self.lineEdit_inv_num_check.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_inv_num_check.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_inv_num_check.setObjectName("lineEdit_inv_num_check")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inv_num_check)
        self.label_direction_check = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_direction_check.setFont(font)
        self.label_direction_check.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_direction_check.setObjectName("label_direction_check")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_direction_check)
        self.comboBox_direction_check = QtWidgets.QComboBox(self.checkInvoiceTab)
        self.comboBox_direction_check.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_direction_check.setStyleSheet("QComboBox\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    background-color: #31363B;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}")
        self.comboBox_direction_check.setObjectName("comboBox_direction_check")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_direction_check)
        self.label_10 = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_9 = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.tabWidget.addTab(self.checkInvoiceTab, "")
        self.getInvoiceDataTab = QtWidgets.QWidget()
        self.getInvoiceDataTab.setStyleSheet("\n"
"QWidget\n"
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
        self.getInvoiceDataTab.setObjectName("getInvoiceDataTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.getInvoiceDataTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_tax_id_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_tax_id_dat.setFont(font)
        self.label_tax_id_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_tax_id_dat.setObjectName("label_tax_id_dat")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id_dat)
        self.label_inv_num_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_inv_num_dat.setFont(font)
        self.label_inv_num_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_inv_num_dat.setObjectName("label_inv_num_dat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_inv_num_dat)
        self.label_direction_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_direction_dat.setFont(font)
        self.label_direction_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_direction_dat.setObjectName("label_direction_dat")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_direction_dat)
        self.label_resp_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(5)
        self.label_resp_dat.setFont(font)
        self.label_resp_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_resp_dat.setObjectName("label_resp_dat")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_resp_dat)
        self.label_source_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_source_dat.setFont(font)
        self.label_source_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_source_dat.setObjectName("label_source_dat")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_source_dat)
        self.label_trans_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_trans_dat.setFont(font)
        self.label_trans_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_trans_dat.setObjectName("label_trans_dat")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_trans_dat)
        self.label_index_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_index_dat.setFont(font)
        self.label_index_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_index_dat.setObjectName("label_index_dat")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_index_dat)
        self.label_reqv_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_reqv_dat.setFont(font)
        self.label_reqv_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_reqv_dat.setObjectName("label_reqv_dat")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_reqv_dat)
        self.label_inv_save_time_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_inv_save_time_dat.setFont(font)
        self.label_inv_save_time_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_inv_save_time_dat.setObjectName("label_inv_save_time_dat")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_inv_save_time_dat)
        self.label_tech_user_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_tech_user_dat.setFont(font)
        self.label_tech_user_dat.setStyleSheet("QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}")
        self.label_tech_user_dat.setObjectName("label_tech_user_dat")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_tech_user_dat)
        self.lineEdit_tax_id_dat = QtWidgets.QLineEdit(self.getInvoiceDataTab)
        self.lineEdit_tax_id_dat.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_tax_id_dat.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_tax_id_dat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_tax_id_dat.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_tax_id_dat.setText("")
        self.lineEdit_tax_id_dat.setObjectName("lineEdit_tax_id_dat")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id_dat)
        self.lineEdit_inv_num_dat = QtWidgets.QLineEdit(self.getInvoiceDataTab)
        self.lineEdit_inv_num_dat.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_inv_num_dat.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_inv_num_dat.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_inv_num_dat.setObjectName("lineEdit_inv_num_dat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inv_num_dat)
        self.comboBox_direction_dat = QtWidgets.QComboBox(self.getInvoiceDataTab)
        self.comboBox_direction_dat.setMinimumSize(QtCore.QSize(87, 0))
        self.comboBox_direction_dat.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_direction_dat.setBaseSize(QtCore.QSize(0, 38))
        self.comboBox_direction_dat.setStyleSheet("QComboBox\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    background-color: #31363B;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}")
        self.comboBox_direction_dat.setObjectName("comboBox_direction_dat")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_direction_dat)
        self.label_3 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.getInvoiceDataTab)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"background-color: white;\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 273, 281))
        self.scrollAreaWidgetContents.setStyleSheet("\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: white;\n"
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
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.pushButton_save_dat = QtWidgets.QPushButton(self.getInvoiceDataTab)
        self.pushButton_save_dat.setStyleSheet("QPushButton\n"
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
        self.pushButton_save_dat.setObjectName("pushButton_save_dat")
        self.verticalLayout_3.addWidget(self.pushButton_save_dat)
        self.pushButton = QtWidgets.QPushButton(self.getInvoiceDataTab)
        self.pushButton.setStyleSheet("QPushButton\n"
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.getInvoiceDataTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        ChildWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChildWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 22))
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
        ChildWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChildWindow)
        self.statusbar.setStyleSheet("QStatusBar::item {\n"
"    border: 0px transparent dark;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
" }")
        self.statusbar.setObjectName("statusbar")
        ChildWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChildWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ChildWindow)

    def retranslateUi(self, ChildWindow):
        _translate = QtCore.QCoreApplication.translate
        ChildWindow.setWindowTitle(_translate("ChildWindow", "Hungary-tool"))
        self.getTaxpayerTab.setToolTip(_translate("ChildWindow", "<html><head/><body><p>get taxpayer validity</p></body></html>"))
        self.label_tax_id.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.lineEdit_tax_id.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.label_check_id.setText(_translate("ChildWindow", "Taxpayer ID to check:"))
        self.lineEdit_check_id.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id for company that you want to check</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.getTaxpayerTab), _translate("ChildWindow", "Check taxpayer"))
        self.label_tax_id_check.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.lineEdit_tax_id_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.label_inv_num_check.setText(_translate("ChildWindow", "Invoice Number:"))
        self.lineEdit_inv_num_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice number to check</p></body></html>"))
        self.label_direction_check.setText(_translate("ChildWindow", "Direction:"))
        self.comboBox_direction_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Direction of invoice can be INBOUND and OUTBOUND.</p><p>OUTBOUND is your own invoice, and INBOUND is invoice of other company</p></body></html>"))
        self.label_10.setText(_translate("ChildWindow", "                                                                                                          "))
        self.label.setText(_translate("ChildWindow", "Response data:"))
        self.label_2.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Contains the boolean result of the check</p></body></html>"))
        self.label_2.setText(_translate("ChildWindow", "Check result:"))
        self.label_9.setText(_translate("ChildWindow", "                                                                                                             "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.checkInvoiceTab), _translate("ChildWindow", "Check Invoice"))
        self.label_tax_id_dat.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.label_inv_num_dat.setText(_translate("ChildWindow", "Invoice Number:"))
        self.label_direction_dat.setText(_translate("ChildWindow", "Direction:"))
        self.label_resp_dat.setText(_translate("ChildWindow", "Response data:"))
        self.label_source_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice data report source</p></body></html>"))
        self.label_source_dat.setText(_translate("ChildWindow", "Source:"))
        self.label_trans_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice data report transaction ID, if the report was submitted via the computer interface</p></body></html>"))
        self.label_trans_dat.setText(_translate("ChildWindow", "Transaction ID"))
        self.label_index_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice data report transaction index</p></body></html>"))
        self.label_index_dat.setText(_translate("ChildWindow", "Index:"))
        self.label_reqv_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Data report requestVersion value </p></body></html>"))
        self.label_reqv_dat.setText(_translate("ChildWindow", "Original request version:"))
        self.label_inv_save_time_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice data report save time </p></body></html>"))
        self.label_inv_save_time_dat.setText(_translate("ChildWindow", "Invoice data save time:"))
        self.label_tech_user_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Name of the technical user submitting the invoice data report</p></body></html>"))
        self.label_tech_user_dat.setText(_translate("ChildWindow", "Technical user name:"))
        self.lineEdit_tax_id_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.lineEdit_inv_num_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>invoice number to get data </p></body></html>"))
        self.comboBox_direction_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Direction of invoice can be INBOUND and OUTBOUND.</p><p>OUTBOUND is your own invoice, and INBOUND is invoice of other company</p></body></html>"))
        self.pushButton_save_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>save invoice file </p><p><br/></p></body></html>"))
        self.pushButton_save_dat.setText(_translate("ChildWindow", "Save"))
        self.pushButton.setToolTip(_translate("ChildWindow", "<html><head/><body><p>clear current response</p></body></html>"))
        self.pushButton.setText(_translate("ChildWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.getInvoiceDataTab), _translate("ChildWindow", "Get Invoice data"))
