from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QSyntaxHighlighter
from mainui import Ui_MainWindow
from childui import Ui_ChildWindow
import sys
from request import Ping, CallCPI
from functools import partial
from xmlparser import Find_result_set
import xml.dom.minidom
import base64
from PyQt5.QtWidgets import QFileDialog, QAction
from QCodeEditor import QCodeEditor, XMLHighlighter


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        # define some custom settings
        self.ui = Ui_ChildWindow()
        self.ui.setupUi(self)


w = 900
h = 600
app = QtWidgets.QApplication([])
application = mywindow()
application.resize(w, h)
application.show()


sys.exit(app.exec())
