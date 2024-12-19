from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con
from utils import *

#changes
#delete the location input in code and database- it is not needed
#fix bug with id not staying the same when deleting rows. probably making id a public variable instead of only in fill_next_id()
#clean comments to make more readable in main and utils
#change the navigation system so  the top menu works, and hide menu above instead of the buttons 
#redo the main page layout so its not buttons and an inviting info page
#translate mysql to slqlite so it can be deployed as a local application

ui, _  = loadUiType('ValetTracker.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0) #sets the home page the first to pop up
        self.btn_Create_New_Entry.clicked.connect(self.show_add_new_entry) #calls show_add_new_entry function to opens the new entry page and increment the id
        self.btn_Raw_Data.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3)) #navigates to the calculated stats page 
         
        self.btn_My_Stats.clicked.connect(self.show_calc_data)
        self.btn_save_changes.clicked.connect(self.save_entry) #button that commits the entries to database in the new entry page
        self.btn_Raw_Data.clicked.connect(self.show_raw_data)
        self.btn_delete.clicked.connect(self.delete_raw_entry)

    def show_add_new_entry(self): #add new entry
        self.tabWidget.setCurrentIndex(1) #page position
        fill_next_id(self) #calls method to keep count of id's

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

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

