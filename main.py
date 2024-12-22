from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con
from utils import *

#change
#redo the main page layout so its not buttons and an inviting info page
#translate mysql to slqlite so it can be deployed as a local application

#can create a upload saved  database which can read a previouly downloaded database and upload into database, make sure to clear current table

ui, _  = loadUiType('ValetTracker.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0) #sets the home page the first to pop up
        self.menubar.setVisible(False) #hides menu bar

        self.tabWidget.currentChanged.connect(self.on_tab_changed) #calls function to fill calc data when tab clicked
        self.tabWidget.currentChanged.connect(self.on_tab_changed) #calls function to fill raw data when tab clicked

        self.btn_save_changes.clicked.connect(self.save_entry) #btn to commit entries to database
        self.btn_delete.clicked.connect(self.delete_raw_entry) #btn to delete selected entry
        self.btn_clear.clicked.connect(self.clear_raw_entries) #btn to trunicate database table

    # Check if tab_5 or tab_6 is the currently selected tab to properly navigate 
    def on_tab_changed(self, index):
        if self.tabWidget.indexOf(self.tab_5) == index:
            self.show_calc_data()
        if self.tabWidget.indexOf(self.tab_6) == index:
            self.show_raw_data()

    def save_entry(self): #function to call save entry for btn_save_changes
        save_entry_funct(self)

    def show_calc_data(self): #show calc data page
        self.tabWidget.setCurrentIndex(2) #page position

        self.textBrowser_Total_Tips_recieved.setText(str(calc_data_tips()))   #output of calc_data_tips to textBrowser
        self.textBrowser_Average_tips_per_shift.setText(str(calc_avg_tips()))  #output of calc_avg_tips to textBrowser
        self.textBrowser_Average_tips_per_hr.setText(str(calc_tips_per_hr()))   #output of calc_tips_per_hr to textBrowser
        self.textBrowser_Total_hours_worked.setText(str(calc_total_hours_worked()))  #output of duration to textBrowser
        self.textBrowser_Total_cars_parked.setText(str(calc_cars_parked()))  #output of cars_parked to textBrowser
        self.textBrowser_Cars_per_hour.setText(str(calc_cars_per_hour()))  #output of cars_parked to textBrowser

    #function to print the raw data in a good format so the user can view 
    def show_raw_data(self):
        self.tabWidget.setCurrentIndex(3) #page position to raw data
        self.textBrowser_raw_data.setText(str(display_raw_data())) # dispaly the data
    
    #function to delete an entry entirely from the raw data tab
    def delete_raw_entry(self):
        delete_entry(self)
        self.show_raw_data() #recall function to reload page to show updated version
    
    #function to clear(trunicate) entire table and reset
    def clear_raw_entries(self):
        clear_entries(self)
        self.show_raw_data()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


