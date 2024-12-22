from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con
from utils import *

#changes
#delete the location input in code and database- it is not needed
#make it mandatory to enter tips, valets on duty, duration, maybe car parked(change calculation for car to only entries where the car # were entered)
#clean comments to make more readable in main and utils
#redo the main page layout so its not buttons and an inviting info page
#translate mysql to slqlite so it can be deployed as a local application

#can create a upload saved database which can read a previouly downloaded database and upload into database, make sure to clear current table


ui, _  = loadUiType('ValetTracker.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0) #sets the home page the first to pop up
        self.menubar.setVisible(False) #hides menu bar

        self.tabWidget.currentChanged.connect(self.on_tab_changed) #calls function to fill calc data when tab clicked
        self.tabWidget.currentChanged.connect(self.on_tab_changed) #calls function to fill raw data when tab clicked

        self.btn_save_changes.clicked.connect(self.save_entry) #button that commits the entries to database in the new entry page
        self.btn_delete.clicked.connect(self.delete_raw_entry) #btn to delete a selected entry in the raw data tab
        self.btn_clear.clicked.connect(self.clear_raw_entries) #btn to clear all data from table and reset id

    # Check if tab_5 or tab_6 is the currently selected tab to properly navigate 
    def on_tab_changed(self, index):
        if self.tabWidget.indexOf(self.tab_5) == index:
            self.show_calc_data()
        if self.tabWidget.indexOf(self.tab_6) == index:
            self.show_raw_data()

    def show_add_new_entry(self): #add new entry
        self.tabWidget.setCurrentIndex(1) #page position
        #fill_next_id(self) #calls method to keep count of id's

    def save_entry(self): #function to call save entry for btn_save_changes
        save_entry_funct(self)

    def show_calc_data(self): #show calc data page
        self.tabWidget.setCurrentIndex(2) #page position

        self.textBrowser_Total_Tips_recieved.setText(str(calc_data_tips()))   #output of calc_data_tips to the button
        self.textBrowser_Average_tips_per_shift.setText(str(calc_avg_tips()))  #output of calc_avg_tips to the button
        self.textBrowser_Average_tips_per_hr.setText(str(calc_tips_per_hr()))   #output of calc_tips_per_hr to the button
        self.textBrowser_Total_hours_worked.setText(str(calc_total_hours_worked()))  #output of duration to the button
        self.textBrowser_Total_cars_parked.setText(str(calc_cars_parked()))  #output of cars_parked to the button
        self.textBrowser_Cars_per_hour.setText(str(calc_cars_per_hour()))  #output of cars_parked to the button

    #function to print the raw data in a good format so the user can view, delete(by id,error message if invalid id) and maybe edit
    def show_raw_data(self):
        self.tabWidget.setCurrentIndex(3) #page position to raw data
        self.textBrowser_raw_data.setText(str(display_raw_data())) # dispaly the data
    
    #function to delete an entry entirely from the raw data tab
    def delete_raw_entry(self):
        delete_entry(self)
        self.show_raw_data() #recall function to reload page to show updated version
    
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

