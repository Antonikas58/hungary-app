from PyQt5 import QtWidgets, QtGui
from mainui import Ui_MainWindow  # import of our generated main window
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        #define some custom settings
        self.setFixedSize(800, 600)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_name.setFont(QtGui.QFont('SansSerif', 10))
        self.ui.label_pass.setFont(QtGui.QFont('SansSerif', 10))
        self.ui.label_cred.setFont(QtGui.QFont('SansSerif', 5))
        self.ui.label_cred.setStyleSheet('color: red')
        self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_pass.textEdited.connect(self.InputFieldCheck)
        self.ui.lineEdit_name.textEdited.connect(self.InputFieldCheck)
        self.ui.SeeButton.clicked.connect(self.ShowPassField)
        self.ui.ContinueButton.setEnabled(False)

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
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())