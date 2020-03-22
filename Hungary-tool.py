from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QSyntaxHighlighter, QFont
from mainui import Ui_MainWindow
from childui import Ui_ChildWindow
import sys
from request import Ping, CallCPI
from functools import partial
from xmlparser import Find_result_set, Find_Element_value, Parse_Transaction_List
import xml.dom.minidom
import base64
from PyQt5.QtWidgets import QFileDialog, QAction, QCompleter
from tinydb import TinyDB, Query

class mywindow(QtWidgets.QMainWindow):
    addr = None
    Usr = None
    Pass = None
    result_set = {}
    result_list = []
    invoice = None
    file_name = None
    db = TinyDB('db.json') 
    def __init__(self):
        super(mywindow, self).__init__()
        # define some custom settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_cred.setStyleSheet('color: red')
        self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        # bind events
        self.ui.lineEdit_pass.textEdited.connect(self.InputFieldCheck)
        self.ui.lineEdit_name.textEdited.connect(self.InputFieldCheck)
        self.ui.SeeButton.clicked.connect(self.ShowPassField)
        self.ui.PingButton.clicked.connect(self.PingCPI)
        self.ui.ContinueButton.clicked.connect(self.OpenChildWindow)
        self.ui.lineEdit_name.setCompleter(self.Get_search_help("User"))
        self.ui.lineEdit_addr.setCompleter(self.Get_search_help("Address"))
    def InputFieldCheck(self):
        if (self.ui.lineEdit_pass.text() != '') and (self.ui.lineEdit_name.text() != ''):
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
        identifier = Ping(self.ui.lineEdit_addr.text(
        ), self.ui.lineEdit_name.text(), self.ui.lineEdit_pass.text())
        if identifier:
            self.ui.label_ping.setText("Success")
            self.ui.label_ping.setStyleSheet('color: green')
            self.Fill_db()

        else:
            self.ui.label_ping.setText("Failed")
            self.ui.label_ping.setStyleSheet('color: red')

    def OpenChildWindow(self):
        w = 1200
        h = 800
        self.addr = application.ui.lineEdit_addr.text()
        self.Usr = application.ui.lineEdit_name.text()
        self.Pass = application.ui.lineEdit_pass.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChildWindow()
        self.ui.setupUi(self.window)
        application.hide()
        self.window.resize(w, h)
        self.window.show()
        # bind events
        self.ui.pushButton_send.clicked.connect(partial(self.SendToCPI, self.ui.pushButton_send))
        self.ui.pushButton_send_check.clicked.connect(partial(self.SendToCPI, self.ui.pushButton_send_check))
        self.ui.pushButton_send_dat.clicked.connect(partial(self.SendToCPI, self.ui.pushButton_send_dat))
        self.ui.pushButton_send_list.clicked.connect(partial(self.SendToCPI, self.ui.pushButton_send_list))
        self.ui.pushButton_save_dat.clicked.connect(self.file_save)
        self.ui.pushButton_clear.clicked.connect(self.clear_file)
        self.action = QAction("Back")
        self.ui.menubar.addAction(self.action)
        self.action.triggered.connect(self.menu_back)
        self.ui.comboBox_direction_check.addItems(['INBOUND', 'OUTBOUND'])
        self.ui.comboBox_direction_dat.addItems(['INBOUND', 'OUTBOUND'])
        self.ui.TimeEdit_from_list.setDisplayFormat("yyyy-MM-dd'T'HH:mm:ss'.000Z" )
        self.ui.TimeEdit_to_list.setDisplayFormat("yyyy-MM-dd'T'HH:mm:ss'.000Z" )
        
    def menu_back(self):
        self.window.hide()
        self.__init__()
        application.show()

    def SendToCPI(self, btn):
        if btn == self.ui.pushButton_send:
          
            self.result_set = {}
            self.Clear_labels()
            resp = CallCPI(self.addr, self.Usr, self.Pass, 'queryTaxpayer', '', '', self.ui.lineEdit_tax_id.text(), self.ui.lineEdit_check_id.text(),'','','')
            try:
                self.result_set = Find_result_set(resp)
                self.ui.label_error.setText('Transmission Successfull. If result is empty - nothing was found')    
                self.ui.label_error.setStyleSheet('color: green') 
            except:
                self.ui.label_error.setText(resp)    
                self.ui.label_error.setStyleSheet('color: red') 

            self.FillLabels()
            if self.result_set.get('ErrorText') != None:
                self.ui.label_error.setText('Something went wrong during Iflow processing.Please go to CPI Tenant and check trace logs')
                self.ui.label_error.setStyleSheet('color: red')

        elif btn == self.ui.pushButton_send_check:
          
            self.result_set = {}
            self.Clear_labels()
            resp = CallCPI(self.addr, self.Usr, self.Pass, 'queryInvoiceCheck', self.ui.comboBox_direction_check.currentText(), self.ui.lineEdit_inv_num_check.text(), self.ui.lineEdit_tax_id_check.text(),'','','','')
            try:
                self.result_set = Find_result_set(resp)
                self.ui.label_error_check.setText('Transmission Successfull. If result is empty - nothing was found')
                self.ui.label_error_check.setStyleSheet('color: green')  
            except:
                self.ui.label_error_check.setText(resp)
                self.ui.label_error_check.setStyleSheet('color: red')      
      
            self.FillLabels()
            if self.result_set.get('ErrorText') != None:
                self.ui.label_error_check.setText('Something went wrong during Iflow processing.Please go to CPI Tenant and check trace logs')
                self.ui.label_error_check.setStyleSheet('color: red')            
            
        elif btn == self.ui.pushButton_send_dat:
          
            self.result_set = {}
            self.Clear_labels()
            resp = CallCPI(self.addr, self.Usr, self.Pass, 'queryInvoiceData', self.ui.comboBox_direction_dat.currentText(), self.ui.lineEdit_inv_num_dat.text(), self.ui.lineEdit_tax_id_dat.text(),'','','','')
            try:
                self.result_set = Find_result_set(resp)
                self.ui.label_error_dat.setText('Transmission Successfull. If result is empty - nothing was found')     
                self.ui.label_error_dat.setStyleSheet('color: green') 
            except:
                self.ui.label_error_dat.setText(resp)     
                self.ui.label_error_dat.setStyleSheet('color: red') 
                
            self.FillLabels()
            if self.result_set.get('ErrorText') != None:
                self.ui.label_error_dat.setText('Something went wrong during Iflow processing.Please go to CPI Tenant and check trace logs')
                self.ui.label_error_dat.setStyleSheet('color: red')
                
        elif btn == self.ui.pushButton_send_list:
            
            self.result_list = []
            self.result_set = {}
            self.Clear_labels()
            page = '1'
            pages = ''
            resp = CallCPI(self.addr, self.Usr, self.Pass, 'queryTransactionList', '', '', self.ui.lineEdit_id_list.text(),'',self.ui.TimeEdit_from_list.text(),self.ui.TimeEdit_to_list.text(), page )
            try:
                self.result_set = Find_result_set(resp)
                if self.result_set.get('ErrorText') != None:
                    self.ui.label_error_list.setText('Something went wrong during Iflow processing.Please go to CPI Tenant and check trace logs')
                    self.ui.label_error_list.setStyleSheet('color: red')
                else:
                    self.result_set = {}
                    
                    self.result_list = Parse_Transaction_List(resp, self.result_list)
                    pages = Find_Element_value(resp, 'availablePage')
                    self.ui.label_error_list.setText('Transmission Successfull. If result is empty - nothing was found')     
                    self.ui.label_error_list.setStyleSheet('color: green')  
            except:
                self.ui.label_error_list.setText(resp)     
                self.ui.label_error_list.setStyleSheet('color: red') 
            if pages != '':                    
                while int(page) < int(pages):
                    page = str(int(page) + 1)
                    resp = CallCPI(self.addr, self.Usr, self.Pass, 'queryTransactionList', '', '', self.ui.lineEdit_id_list.text(),'',self.ui.TimeEdit_from_list.text(),self.ui.TimeEdit_to_list.text(), page )
                    try:
                        self.result_list = Parse_Transaction_List(resp, self.result_list)
                    except:    
                        self.ui.label_error_list.setText('Could not read all information from NAV, please try to start again')     
                        self.ui.label_error_list.setStyleSheet('color: red') 
                        self.result_list = []
            self.Fill_table_list()

    def FillLabels(self):
        self.ui.label_val_.setText(self.result_set.get('taxpayerValidity'))
        self.ui.label_name.setText(self.result_set.get('taxpayerName'))
        self.ui.label_short_name.setText(self.result_set.get('ShortName'))
        self.ui.label_vat_gr.setText(self.result_set.get('vatGroupMembership'))
        self.ui.label_co_code.setText(self.result_set.get('countryCode'))
        self.ui.label_region.setText(self.result_set.get('region'))
        self.ui.label_post_code.setText(self.result_set.get('postalCode'))
        self.ui.label_city.setText(self.result_set.get('city'))
        self.ui.label_streetname.setText(self.result_set.get('streetName'))
        self.ui.label_place_cat.setText(self.result_set.get('publicPlaceCategory'))
        self.ui.label_number.setText(self.result_set.get('number'))
        self.ui.label_build.setText(self.result_set.get('building'))
        self.ui.label_stair.setText(self.result_set.get('staircase'))
        self.ui.label_floor.setText(self.result_set.get('floor'))
        self.ui.label_door.setText(self.result_set.get('door'))
        self.ui.label_lot.setText(self.result_set.get('lotNumber'))
        self.ui.label_result_check.setText(self.result_set.get('invoiceCheckResult'))
        self.ui.label_source_dat_2.setText(self.result_set.get('source'))
        self.ui.label_tr_id_dat.setText(self.result_set.get('transactionId'))
        self.ui.label_index_dat_2.setText(self.result_set.get('index'))
        self.ui.label_version_dat.setText(self.result_set.get('originalRequestVersio'))
        self.ui.label_save_t_dat.setText(self.result_set.get('insDate'))
        self.ui.label_tech_usr_dat.setText(self.result_set.get('insCusUser'))
        
        try:
            self.invoice = (base64.b64decode(self.result_set.get('invoiceData'))).decode('utf-8')
            self.ui.textEdit.setPlainText(self.invoice)
            highlighter = QSyntaxHighlighter(self.ui.textEdit)
        except:
            pass
    def Fill_table_list(self):
      
        self.ui.table_list.setRowCount(0)
        for item in self.result_list:
            rowPosition = self.ui.table_list.rowCount()
            self.ui.table_list.insertRow(rowPosition)
            self.ui.table_list.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(item['transactionId']))
            self.ui.table_list.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(item['insDate']))
            self.ui.table_list.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(item['originalRequestVersion']))   
            self.ui.table_list.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(item['itemCount']))
            

    def file_save(self):
        self.file_name = self.ui.lineEdit_inv_num_dat.text() + '.xml'
        if self.invoice != None:
            name = QFileDialog.getSaveFileName(self, 'Save File', self.file_name)
            try:
                file = open(name[0], 'w')
                file.write(self.invoice)
                file.close()
            except:
                pass


    def clear_file(self):
        self.invoice = None
        self.ui.textEdit.setPlainText(self.invoice)
        
        
    def Clear_labels(self):
        self.ui.label_val_.clear()
        self.ui.label_name.clear()
        self.ui.label_short_name.clear()
        self.ui.label_vat_gr.clear()
        self.ui.label_co_code.clear()
        self.ui.label_region.clear()
        self.ui.label_post_code.clear()
        self.ui.label_city.clear()
        self.ui.label_streetname.clear()
        self.ui.label_place_cat.clear()
        self.ui.label_number.clear()
        self.ui.label_build.clear()
        self.ui.label_stair.clear()
        self.ui.label_floor.clear()
        self.ui.label_door.clear()
        self.ui.label_lot.clear()
        self.ui.label_result_check.clear()
        self.ui.label_source_dat_2.clear()
        self.ui.label_tr_id_dat.clear()
        self.ui.label_index_dat_2.clear()
        self.ui.label_version_dat.clear()
        self.ui.label_save_t_dat.clear()
        self.ui.label_tech_usr_dat.clear()
        self.ui.textEdit.clear()
        self.ui.label_error.clear()
        self.ui.label_error_check.clear()
        self.ui.label_error_dat.clear()
        self.ui.label_error_list.clear()
        self.ui.table_list.clearContents()
    def Fill_db(self):
        Credent = Query()
        
        usr = self.db.search(Credent.User == self.ui.lineEdit_name.text())
        adr = self.db.search( Credent.Address == self.ui.lineEdit_addr.text())

        if usr == []:
            self.db.insert({'User': self.ui.lineEdit_name.text()})
   
        if adr == []:   
            self.db.insert({'Address': self.ui.lineEdit_addr.text()})
    def Get_search_help(self, option):
        Cred = Query()
        search_help_usr = []
        search_help_addr = []
        if option == 'User':
            usrs =  self.db.search(Cred.User)  
        
            for usr in usrs:
                search_help_usr.append(usr['User'])
                
            completer_name = QCompleter(search_help_usr)
            return completer_name
        
        elif option == 'Address':
            adrs = self.db.search(Cred.Address)  
        
            for adr in adrs:
                search_help_addr.append(adr['Address'])
                
            completer_addr = QCompleter(search_help_addr)
            return completer_addr

# Program start

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
