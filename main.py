from PyQt5 import QtWidgets, QtGui
from mainui import Ui_MainWindow  
from childui import Ui_ChildWindow
import sys
from request import Ping 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        #define some custom settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_cred.setStyleSheet('color: red')
        self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.ContinueButton.setEnabled(False)
        # bind events
        self.ui.lineEdit_pass.textEdited.connect(self.InputFieldCheck)
        self.ui.lineEdit_name.textEdited.connect(self.InputFieldCheck)
        self.ui.SeeButton.clicked.connect(self.ShowPassField)
        self.ui.PingButton.clicked.connect(self.PingCPI)
        self.ui.ContinueButton.clicked.connect(self.OpenChildWindow)
        
    def InputFieldCheck(self):
        if (self.ui.lineEdit_pass.text() != '')  and (self.ui.lineEdit_name.text() != ''):
           self.ui.label_cred.setText("Credentials are filled")
           self.ui.label_cred.setStyleSheet('color: green')
           self.ui.ContinueButton.setEnabled(True)
        else:
           self.ui.label_cred.setText("Credentials are empty")
           self.ui.label_cred.setStyleSheet('color: red')
           self.ui.ContinueButton.setEnabled(False) 
    def ShowPassField(self):
        if self.ui.lineEdit_pass.echoMode() == QtWidgets.QLineEdit.Password:
           self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
           self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
    def PingCPI(self):
        identifier = Ping(self.ui.lineEdit_addr.text(), self.ui.lineEdit_name.text(), self.ui.lineEdit_pass.text())  
        if identifier:
          self.ui.label_ping.setText("Success")
          self.ui.label_ping.setStyleSheet('color: green')

        else:
          self.ui.label_ping.setText("Failed")
          self.ui.label_ping.setStyleSheet('color: red') 

    def OpenChildWindow(self):
        w = 1200; h = 800
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChildWindow()
        self.ui.setupUi(self.window) 
        application.hide()
        self.window.resize(w, h)
        self.window.show()
        
        self.ui.comboBox_direction_check.addItems(['INBOUND','OUTBOUND'])
        self.ui.comboBox_direction_dat.addItems(['INBOUND','OUTBOUND'])

w = 900; h = 600
app = QtWidgets.QApplication([])
application = mywindow()
application.resize(w, h)
application.show()
 
sys.exit(app.exec())