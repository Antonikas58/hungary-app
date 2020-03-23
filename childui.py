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
        ChildWindow.resize(852, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SAPLogon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChildWindow.setWindowIcon(icon)
        ChildWindow.setStyleSheet("\n"
"QWidget\n"
"{\n"
"    background-color: #323232;\n"
"}")
        ChildWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(ChildWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"    color: #323232;\n"
"}")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.getTaxpayerTab = QtWidgets.QWidget()
        self.getTaxpayerTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.getTaxpayerTab.setMouseTracking(False)
        self.getTaxpayerTab.setToolTip("")
        self.getTaxpayerTab.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.getTaxpayerTab.setObjectName("getTaxpayerTab")
        self.formLayout = QtWidgets.QFormLayout(self.getTaxpayerTab)
        self.formLayout.setObjectName("formLayout")
        self.label_tax_id = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_tax_id.setMinimumSize(QtCore.QSize(200, 1))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_tax_id.setFont(font)
        self.label_tax_id.setStyleSheet("")
        self.label_tax_id.setObjectName("label_tax_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id)
        self.lineEdit_tax_id = QtWidgets.QLineEdit(self.getTaxpayerTab)
        self.lineEdit_tax_id.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_tax_id.setFont(font)
        self.lineEdit_tax_id.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_tax_id.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_tax_id.setText("")
        self.lineEdit_tax_id.setObjectName("lineEdit_tax_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id)
        self.label_check_id = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_check_id.setMinimumSize(QtCore.QSize(200, 1))
        self.label_check_id.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_check_id.setFont(font)
        self.label_check_id.setStyleSheet("")
        self.label_check_id.setObjectName("label_check_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_check_id)
        self.lineEdit_check_id = QtWidgets.QLineEdit(self.getTaxpayerTab)
        self.lineEdit_check_id.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_check_id.setFont(font)
        self.lineEdit_check_id.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_check_id.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_check_id.setText("")
        self.lineEdit_check_id.setObjectName("lineEdit_check_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_check_id)
        self.label_resp = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_resp.setMinimumSize(QtCore.QSize(200, 0))
        self.label_resp.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_resp.setFont(font)
        self.label_resp.setStyleSheet("")
        self.label_resp.setObjectName("label_resp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_resp)
        self.label_9 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_val_ = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_val_.setFont(font)
        self.label_val_.setStyleSheet("")
        self.label_val_.setText("")
        self.label_val_.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_val_.setObjectName("label_val_")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_val_)
        self.label_10 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_name = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("")
        self.label_name.setText("")
        self.label_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_name)
        self.label_11 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_11.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_short_name = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_short_name.setFont(font)
        self.label_short_name.setStyleSheet("")
        self.label_short_name.setText("")
        self.label_short_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_short_name.setObjectName("label_short_name")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_short_name)
        self.label_12 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_12.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_vat_gr = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_vat_gr.setFont(font)
        self.label_vat_gr.setStyleSheet("")
        self.label_vat_gr.setText("")
        self.label_vat_gr.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_vat_gr.setObjectName("label_vat_gr")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_vat_gr)
        self.label_13 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_13.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_co_code = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_co_code.setFont(font)
        self.label_co_code.setStyleSheet("")
        self.label_co_code.setText("")
        self.label_co_code.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_co_code.setObjectName("label_co_code")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_co_code)
        self.label_14 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_region = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_region.setFont(font)
        self.label_region.setStyleSheet("")
        self.label_region.setText("")
        self.label_region.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_region.setObjectName("label_region")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_region)
        self.label_15 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_15.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_post_code = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_post_code.setFont(font)
        self.label_post_code.setStyleSheet("")
        self.label_post_code.setText("")
        self.label_post_code.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_post_code.setObjectName("label_post_code")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.label_post_code)
        self.label_16 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_16.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_city = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_city.setFont(font)
        self.label_city.setStyleSheet("")
        self.label_city.setText("")
        self.label_city.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_city.setObjectName("label_city")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_city)
        self.label_17 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_17.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_streetname = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_streetname.setFont(font)
        self.label_streetname.setStyleSheet("")
        self.label_streetname.setText("")
        self.label_streetname.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_streetname.setObjectName("label_streetname")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_streetname)
        self.label_18 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_18.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_place_cat = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_place_cat.setFont(font)
        self.label_place_cat.setStyleSheet("")
        self.label_place_cat.setText("")
        self.label_place_cat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_place_cat.setObjectName("label_place_cat")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.label_place_cat)
        self.label_19 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_19.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_number = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_number.setFont(font)
        self.label_number.setStyleSheet("")
        self.label_number.setText("")
        self.label_number.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_number.setObjectName("label_number")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.label_number)
        self.label_20 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_20.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_build = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_build.setFont(font)
        self.label_build.setStyleSheet("")
        self.label_build.setText("")
        self.label_build.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_build.setObjectName("label_build")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.label_build)
        self.label_21 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_21.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_stair = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_stair.setFont(font)
        self.label_stair.setStyleSheet("")
        self.label_stair.setText("")
        self.label_stair.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_stair.setObjectName("label_stair")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.label_stair)
        self.label_22 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_22.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_floor = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_floor.setFont(font)
        self.label_floor.setStyleSheet("")
        self.label_floor.setText("")
        self.label_floor.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_floor.setObjectName("label_floor")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.label_floor)
        self.label_23 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_23.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_door = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_door.setFont(font)
        self.label_door.setStyleSheet("")
        self.label_door.setText("")
        self.label_door.setObjectName("label_door")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.label_door)
        self.label_24 = QtWidgets.QLabel(self.getTaxpayerTab)
        self.label_24.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_lot = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_lot.setFont(font)
        self.label_lot.setStyleSheet("")
        self.label_lot.setText("")
        self.label_lot.setObjectName("label_lot")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.label_lot)
        self.pushButton_send = QtWidgets.QPushButton(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_send.setObjectName("pushButton_send")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_send)
        self.label_error = QtWidgets.QLabel(self.getTaxpayerTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_error)
        self.tabWidget.addTab(self.getTaxpayerTab, "")
        self.checkInvoiceTab = QtWidgets.QWidget()
        self.checkInvoiceTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkInvoiceTab.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.checkInvoiceTab.setObjectName("checkInvoiceTab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.checkInvoiceTab)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_tax_id_check = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_tax_id_check.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_tax_id_check.setFont(font)
        self.label_tax_id_check.setStyleSheet("")
        self.label_tax_id_check.setObjectName("label_tax_id_check")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id_check)
        self.lineEdit_tax_id_check = QtWidgets.QLineEdit(self.checkInvoiceTab)
        self.lineEdit_tax_id_check.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_tax_id_check.setFont(font)
        self.lineEdit_tax_id_check.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_tax_id_check.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_tax_id_check.setText("")
        self.lineEdit_tax_id_check.setObjectName("lineEdit_tax_id_check")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id_check)
        self.label_inv_num_check = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_inv_num_check.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_inv_num_check.setFont(font)
        self.label_inv_num_check.setStyleSheet("")
        self.label_inv_num_check.setObjectName("label_inv_num_check")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_inv_num_check)
        self.lineEdit_inv_num_check = QtWidgets.QLineEdit(self.checkInvoiceTab)
        self.lineEdit_inv_num_check.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_inv_num_check.setFont(font)
        self.lineEdit_inv_num_check.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_inv_num_check.setObjectName("lineEdit_inv_num_check")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inv_num_check)
        self.label_direction_check = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_direction_check.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_direction_check.setFont(font)
        self.label_direction_check.setStyleSheet("")
        self.label_direction_check.setObjectName("label_direction_check")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_direction_check)
        self.comboBox_direction_check = QtWidgets.QComboBox(self.checkInvoiceTab)
        self.comboBox_direction_check.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.comboBox_direction_check.setFont(font)
        self.comboBox_direction_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_direction_check.setStyleSheet("QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}")
        self.comboBox_direction_check.setObjectName("comboBox_direction_check")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_direction_check)
        self.pushButton_send_check = QtWidgets.QPushButton(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send_check.setFont(font)
        self.pushButton_send_check.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_send_check.setObjectName("pushButton_send_check")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_send_check)
        self.label_error_check = QtWidgets.QLabel(self.checkInvoiceTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_error_check.setFont(font)
        self.label_error_check.setStyleSheet("")
        self.label_error_check.setText("")
        self.label_error_check.setObjectName("label_error_check")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_error_check)
        self.label = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_result_check = QtWidgets.QLabel(self.checkInvoiceTab)
        self.label_result_check.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_result_check.setFont(font)
        self.label_result_check.setStyleSheet("")
        self.label_result_check.setText("")
        self.label_result_check.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_result_check.setObjectName("label_result_check")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_result_check)
        self.tabWidget.addTab(self.checkInvoiceTab, "")
        self.getInvoiceDataTab = QtWidgets.QWidget()
        self.getInvoiceDataTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.getInvoiceDataTab.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.getInvoiceDataTab.setObjectName("getInvoiceDataTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.getInvoiceDataTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_tax_id_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_tax_id_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_tax_id_dat.setFont(font)
        self.label_tax_id_dat.setStyleSheet("")
        self.label_tax_id_dat.setObjectName("label_tax_id_dat")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tax_id_dat)
        self.lineEdit_tax_id_dat = QtWidgets.QLineEdit(self.getInvoiceDataTab)
        self.lineEdit_tax_id_dat.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_tax_id_dat.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_tax_id_dat.setFont(font)
        self.lineEdit_tax_id_dat.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_tax_id_dat.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_tax_id_dat.setText("")
        self.lineEdit_tax_id_dat.setObjectName("lineEdit_tax_id_dat")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tax_id_dat)
        self.label_inv_num_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_inv_num_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_inv_num_dat.setFont(font)
        self.label_inv_num_dat.setStyleSheet("")
        self.label_inv_num_dat.setObjectName("label_inv_num_dat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_inv_num_dat)
        self.lineEdit_inv_num_dat = QtWidgets.QLineEdit(self.getInvoiceDataTab)
        self.lineEdit_inv_num_dat.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_inv_num_dat.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_inv_num_dat.setFont(font)
        self.lineEdit_inv_num_dat.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_inv_num_dat.setObjectName("lineEdit_inv_num_dat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inv_num_dat)
        self.label_direction_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_direction_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_direction_dat.setFont(font)
        self.label_direction_dat.setStyleSheet("")
        self.label_direction_dat.setObjectName("label_direction_dat")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_direction_dat)
        self.comboBox_direction_dat = QtWidgets.QComboBox(self.getInvoiceDataTab)
        self.comboBox_direction_dat.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_direction_dat.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_direction_dat.setBaseSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.comboBox_direction_dat.setFont(font)
        self.comboBox_direction_dat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_direction_dat.setStyleSheet("QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}")
        self.comboBox_direction_dat.setObjectName("comboBox_direction_dat")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_direction_dat)
        self.pushButton_send_dat = QtWidgets.QPushButton(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send_dat.setFont(font)
        self.pushButton_send_dat.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_send_dat.setObjectName("pushButton_send_dat")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_send_dat)
        self.label_error_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_error_dat.setFont(font)
        self.label_error_dat.setStyleSheet("")
        self.label_error_dat.setText("")
        self.label_error_dat.setObjectName("label_error_dat")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_error_dat)
        self.label_resp_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_resp_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_resp_dat.setFont(font)
        self.label_resp_dat.setStyleSheet("")
        self.label_resp_dat.setObjectName("label_resp_dat")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_resp_dat)
        self.label_source_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_source_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_source_dat.setFont(font)
        self.label_source_dat.setStyleSheet("")
        self.label_source_dat.setObjectName("label_source_dat")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_source_dat)
        self.label_source_dat_2 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_source_dat_2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_source_dat_2.setFont(font)
        self.label_source_dat_2.setStyleSheet("")
        self.label_source_dat_2.setText("")
        self.label_source_dat_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_source_dat_2.setObjectName("label_source_dat_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_source_dat_2)
        self.label_trans_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_trans_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_trans_dat.setFont(font)
        self.label_trans_dat.setStyleSheet("")
        self.label_trans_dat.setObjectName("label_trans_dat")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_trans_dat)
        self.label_tr_id_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_tr_id_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tr_id_dat.setFont(font)
        self.label_tr_id_dat.setStyleSheet("")
        self.label_tr_id_dat.setText("")
        self.label_tr_id_dat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_tr_id_dat.setObjectName("label_tr_id_dat")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_tr_id_dat)
        self.label_index_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_index_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_index_dat.setFont(font)
        self.label_index_dat.setStyleSheet("")
        self.label_index_dat.setObjectName("label_index_dat")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_index_dat)
        self.label_index_dat_2 = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_index_dat_2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_index_dat_2.setFont(font)
        self.label_index_dat_2.setStyleSheet("")
        self.label_index_dat_2.setText("")
        self.label_index_dat_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_index_dat_2.setObjectName("label_index_dat_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_index_dat_2)
        self.label_reqv_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_reqv_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_reqv_dat.setFont(font)
        self.label_reqv_dat.setStyleSheet("")
        self.label_reqv_dat.setObjectName("label_reqv_dat")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_reqv_dat)
        self.label_version_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_version_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_version_dat.setFont(font)
        self.label_version_dat.setStyleSheet("")
        self.label_version_dat.setText("")
        self.label_version_dat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_version_dat.setObjectName("label_version_dat")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_version_dat)
        self.label_inv_save_time_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_inv_save_time_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_inv_save_time_dat.setFont(font)
        self.label_inv_save_time_dat.setStyleSheet("")
        self.label_inv_save_time_dat.setObjectName("label_inv_save_time_dat")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_inv_save_time_dat)
        self.label_save_t_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_save_t_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_save_t_dat.setFont(font)
        self.label_save_t_dat.setStyleSheet("")
        self.label_save_t_dat.setText("")
        self.label_save_t_dat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_save_t_dat.setObjectName("label_save_t_dat")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_save_t_dat)
        self.label_tech_user_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_tech_user_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_tech_user_dat.setFont(font)
        self.label_tech_user_dat.setStyleSheet("")
        self.label_tech_user_dat.setObjectName("label_tech_user_dat")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_tech_user_dat)
        self.label_tech_usr_dat = QtWidgets.QLabel(self.getInvoiceDataTab)
        self.label_tech_usr_dat.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tech_usr_dat.setFont(font)
        self.label_tech_usr_dat.setStyleSheet("")
        self.label_tech_usr_dat.setText("")
        self.label_tech_usr_dat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_tech_usr_dat.setObjectName("label_tech_usr_dat")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_tech_usr_dat)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QPlainTextEdit(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QPlainTextEdit\n"
"{\n"
"    background-color: white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.pushButton_save_dat = QtWidgets.QPushButton(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_dat.setFont(font)
        self.pushButton_save_dat.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_save_dat.setObjectName("pushButton_save_dat")
        self.verticalLayout_3.addWidget(self.pushButton_save_dat)
        self.pushButton_clear = QtWidgets.QPushButton(self.getInvoiceDataTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_3.addWidget(self.pushButton_clear)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.getInvoiceDataTab, "")
        self.getTransactionListTab = QtWidgets.QWidget()
        self.getTransactionListTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.getTransactionListTab.setStyleSheet("QTableWidget:item:hover\n"
"{\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"QTableWidget:item\n"
"{\n"
"   \n"
"    font: 10pt \"MS Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.getTransactionListTab.setObjectName("getTransactionListTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.getTransactionListTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"\n"
"    color: #b1b1b1;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_id_list = QtWidgets.QLineEdit(self.getTransactionListTab)
        self.lineEdit_id_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.lineEdit_id_list.setFont(font)
        self.lineEdit_id_list.setStyleSheet("QLineEdit\n"
"{\n"
"       color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.lineEdit_id_list.setObjectName("lineEdit_id_list")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id_list)
        self.label_4 = QtWidgets.QLabel(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"\n"
"    color: #b1b1b1;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.TimeEdit_from_list = QtWidgets.QDateTimeEdit(self.getTransactionListTab)
        self.TimeEdit_from_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.TimeEdit_from_list.setFont(font)
        self.TimeEdit_from_list.setStyleSheet("QDateTimeEdit {\n"
"\n"
"    color: #b1b1b1;\n"
"}")
        self.TimeEdit_from_list.setObjectName("TimeEdit_from_list")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TimeEdit_from_list)
        self.label_5 = QtWidgets.QLabel(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"\n"
"    color: #b1b1b1;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.TimeEdit_to_list = QtWidgets.QDateTimeEdit(self.getTransactionListTab)
        self.TimeEdit_to_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.TimeEdit_to_list.setFont(font)
        self.TimeEdit_to_list.setStyleSheet("QDateTimeEdit {\n"
"\n"
"    color: #b1b1b1;\n"
"}")
        self.TimeEdit_to_list.setObjectName("TimeEdit_to_list")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TimeEdit_to_list)
        self.pushButton_send_list = QtWidgets.QPushButton(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send_list.setFont(font)
        self.pushButton_send_list.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_send_list.setObjectName("pushButton_send_list")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_send_list)
        self.label_error_list = QtWidgets.QLabel(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_error_list.setFont(font)
        self.label_error_list.setText("")
        self.label_error_list.setObjectName("label_error_list")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_error_list)
        self.table_list = QtWidgets.QTableWidget(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.table_list.setFont(font)
        self.table_list.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table_list.setAutoFillBackground(False)
        self.table_list.setStyleSheet("QTableWidget\n"
"{  \n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"\n"
"}\n"
"\n"
"")
        self.table_list.setLineWidth(1)
        self.table_list.setCornerButtonEnabled(True)
        self.table_list.setColumnCount(5)
        self.table_list.setObjectName("table_list")
        self.table_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_list.setHorizontalHeaderItem(4, item)
        self.table_list.horizontalHeader().setCascadingSectionResizes(False)
        self.table_list.horizontalHeader().setDefaultSectionSize(200)
        self.table_list.horizontalHeader().setHighlightSections(True)
        self.table_list.horizontalHeader().setMinimumSectionSize(39)
        self.table_list.horizontalHeader().setStretchLastSection(False)
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.table_list)
        self.gridLayout_2.addLayout(self.formLayout_4, 3, 0, 1, 1)
        self.pushButton_save_list = QtWidgets.QPushButton(self.getTransactionListTab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_list.setFont(font)
        self.pushButton_save_list.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.pushButton_save_list.setObjectName("pushButton_save_list")
        self.gridLayout_2.addWidget(self.pushButton_save_list, 4, 0, 1, 1)
        self.tabWidget.addTab(self.getTransactionListTab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        ChildWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChildWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 24))
        self.menubar.setStyleSheet("QMenuBar::item\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}")
        self.menubar.setObjectName("menubar")
        ChildWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChildWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        ChildWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChildWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ChildWindow)

    def retranslateUi(self, ChildWindow):
        _translate = QtCore.QCoreApplication.translate
        ChildWindow.setWindowTitle(_translate("ChildWindow", "Hungary-tool"))
        self.label_tax_id.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.lineEdit_tax_id.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.label_check_id.setText(_translate("ChildWindow", "Taxpayer ID to check:"))
        self.lineEdit_check_id.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id for company that you want to check</p></body></html>"))
        self.label_resp.setText(_translate("ChildWindow", "  Response data:"))
        self.label_9.setToolTip(_translate("ChildWindow", "<html><head/><body><p>The validity status of the tax number queried (provided the specified tax number exists) </p></body></html>"))
        self.label_9.setText(_translate("ChildWindow", "  Taxpayer Validity:"))
        self.label_val_.setToolTip(_translate("ChildWindow", "<html><head/><body><p>The validity status of the tax number queried (provided the specified tax number exists) </p></body></html>"))
        self.label_10.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Name of taxpayer queried </p></body></html>"))
        self.label_10.setText(_translate("ChildWindow", "  Taxpayer name:"))
        self.label_name.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Name of taxpayer queried</p></body></html>"))
        self.label_11.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Taxpayer’s short name </p></body></html>"))
        self.label_11.setText(_translate("ChildWindow", "  Short name:"))
        self.label_short_name.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Taxpayer’s short name</p></body></html>"))
        self.label_12.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Taxpayer’s VAT group membership </p></body></html>"))
        self.label_12.setText(_translate("ChildWindow", "  Vat group membership:"))
        self.label_vat_gr.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Taxpayer’s VAT group membership </p></body></html>"))
        self.label_13.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Country code as per the ISO 3166 alpha-2 standard </p></body></html>"))
        self.label_13.setText(_translate("ChildWindow", "  Country code:"))
        self.label_co_code.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Country code as per the ISO 3166 alpha-2 standard</p></body></html>"))
        self.label_14.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Region code as per the ISO 3166 alpha-2 standard</p></body></html>"))
        self.label_14.setText(_translate("ChildWindow", "  Region"))
        self.label_region.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Region code as per the ISO 3166 alpha-2 standard</p></body></html>"))
        self.label_15.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Postal code </p></body></html>"))
        self.label_15.setText(_translate("ChildWindow", "  Postal code:"))
        self.label_post_code.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Postal code </p></body></html>"))
        self.label_16.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Settlement </p></body></html>"))
        self.label_16.setText(_translate("ChildWindow", "  City:"))
        self.label_city.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Settlement </p></body></html>"))
        self.label_17.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Name of public space </p></body></html>"))
        self.label_17.setText(_translate("ChildWindow", "  Street name:"))
        self.label_streetname.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Name of public space </p></body></html>"))
        self.label_18.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Type of public space </p></body></html>"))
        self.label_18.setText(_translate("ChildWindow", "  Public place category:"))
        self.label_place_cat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Type of public space </p></body></html>"))
        self.label_19.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Street number </p></body></html>"))
        self.label_19.setText(_translate("ChildWindow", "  Number:"))
        self.label_number.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Street number </p></body></html>"))
        self.label_20.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Building</p></body></html>"))
        self.label_20.setText(_translate("ChildWindow", "  Building:"))
        self.label_build.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Building </p></body></html>"))
        self.label_21.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Stairway</p></body></html>"))
        self.label_21.setText(_translate("ChildWindow", "  Staircase:"))
        self.label_stair.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Stairway</p></body></html>"))
        self.label_22.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Floor </p></body></html>"))
        self.label_22.setText(_translate("ChildWindow", "  Floor:"))
        self.label_floor.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Floor</p></body></html>"))
        self.label_23.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Door number </p></body></html>"))
        self.label_23.setText(_translate("ChildWindow", "  Door"))
        self.label_door.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Door number</p></body></html>"))
        self.label_24.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Topographical lot number </p></body></html>"))
        self.label_24.setText(_translate("ChildWindow", "  Lot number"))
        self.label_lot.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Topographical lot number </p></body></html>"))
        self.pushButton_send.setText(_translate("ChildWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.getTaxpayerTab), _translate("ChildWindow", "Check taxpayer"))
        self.label_tax_id_check.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.lineEdit_tax_id_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.label_inv_num_check.setText(_translate("ChildWindow", "Invoice Number:"))
        self.lineEdit_inv_num_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Invoice number to check</p></body></html>"))
        self.label_direction_check.setText(_translate("ChildWindow", "Direction:"))
        self.comboBox_direction_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Direction of invoice can be INBOUND and OUTBOUND.</p><p>OUTBOUND is your own invoice, and INBOUND is invoice of other company</p></body></html>"))
        self.pushButton_send_check.setText(_translate("ChildWindow", "Send"))
        self.label.setText(_translate("ChildWindow", "Response data:"))
        self.label_2.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Contains the boolean result of the check</p></body></html>"))
        self.label_2.setText(_translate("ChildWindow", "Check result:"))
        self.label_result_check.setToolTip(_translate("ChildWindow", "<html><head/><body><p>true if invoice is correct and False in other cases</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.checkInvoiceTab), _translate("ChildWindow", "Check invoice"))
        self.label_tax_id_dat.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.lineEdit_tax_id_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>taxpayer id of your company</p></body></html>"))
        self.label_inv_num_dat.setText(_translate("ChildWindow", "Invoice Number:"))
        self.lineEdit_inv_num_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>invoice number to get data </p></body></html>"))
        self.label_direction_dat.setText(_translate("ChildWindow", "Direction:"))
        self.comboBox_direction_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>Direction of invoice can be INBOUND and OUTBOUND.</p><p>OUTBOUND is your own invoice, and INBOUND is invoice of other company</p></body></html>"))
        self.pushButton_send_dat.setText(_translate("ChildWindow", "Send"))
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
        self.pushButton_save_dat.setToolTip(_translate("ChildWindow", "<html><head/><body><p>save invoice file </p><p><br/></p></body></html>"))
        self.pushButton_save_dat.setText(_translate("ChildWindow", "Save"))
        self.pushButton_clear.setToolTip(_translate("ChildWindow", "<html><head/><body><p>clear current response</p></body></html>"))
        self.pushButton_clear.setText(_translate("ChildWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.getInvoiceDataTab), _translate("ChildWindow", "Get invoice data"))
        self.label_3.setText(_translate("ChildWindow", "Taxpayer ID:"))
        self.label_4.setText(_translate("ChildWindow", "Date from:"))
        self.label_5.setText(_translate("ChildWindow", "Date to:"))
        self.pushButton_send_list.setText(_translate("ChildWindow", "Send"))
        self.table_list.setSortingEnabled(True)
        item = self.table_list.horizontalHeaderItem(0)
        item.setText(_translate("ChildWindow", "Transaction ID"))
        item = self.table_list.horizontalHeaderItem(1)
        item.setText(_translate("ChildWindow", "Date"))
        item = self.table_list.horizontalHeaderItem(2)
        item.setText(_translate("ChildWindow", "Request version"))
        item = self.table_list.horizontalHeaderItem(3)
        item.setText(_translate("ChildWindow", "Item count"))
        item = self.table_list.horizontalHeaderItem(4)
        item.setText(_translate("ChildWindow", "Status"))
        self.pushButton_save_list.setText(_translate("ChildWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.getTransactionListTab), _translate("ChildWindow", "Get transaction list"))
