from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con

ui, _  = loadUiType('ValetTracker.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0) #sets the home page the first to pop up
        self.btn_Create_New_Entry.clicked.connect(self.show_add_new_entry) #calls show_add_new_entry function to opens the new entry page and increment the id
        self.btn_Raw_Data.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3)) #navigates to the calculated stats page 
        #self.btn_TBD.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3)) #navigates to the TBD page that will be set up later 
        self.btn_My_Stats.clicked.connect(self.show_calc_data)
        self.btn_save_changes.clicked.connect(self.save_entry) #button that commits the entries to database in the new entry page
    #keep a count of the id to keep unique

    def show_add_new_entry(self): #add new entry
        self.tabWidget.setCurrentIndex(1) #page position
        self.fill_next_id() #calls method below

    def fill_next_id(self): #function to auto fill the id and autoincrement it to the next id
        try:
            id = 0 #id number
            mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
            cursor = mydb.cursor()
            cursor.execute("select * from entries") #calls entire entries database
            result = cursor.fetchall() #fetch all lines
            if result:
                for ent in result: #for each line in database
                    id += 1 #add one to keep unique key
            self.textBrowser_id.setText(str(id + 1)) 
        except con.Error as e:
            print(f"Database connection error: {e}")
            QMessageBox.critical(self, "Database Error", f"Error connecting to the database: {e}")

    def save_entry(self): #function to save the entry when the button is hit on the new entry page
        try:
            mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
            cursor = mydb.cursor()
            # Retrieve input from the user interface in all text input boxes
            date= self.lineEdit_Date.text()
            Total_tips_earned= self.lineEdit_Total_tips_earned.text()
            valets_on_duty= self.lineEdit_Valets_on_duty.text()
            duration= self.lineEdit_Duration.text()
            cars_parked= self.lineEdit_Cars_parked.text()
            TBD_1= self.lineEdit_TBD_1.text()
            TBD_2= self.lineEdit_TBD_2.text()

            # SQL query for inserting data
            query = """
            INSERT INTO entries (date, Total_tips_earned, valets_on_duty, duration, cars_parked, TBD_1, TBD_2)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (date, Total_tips_earned, valets_on_duty, duration, cars_parked, TBD_1, TBD_2)

            # Execute the query
            cursor.execute(query, values)
            mydb.commit()  # Commit the transaction

            QMessageBox.information(self, "Success", "Entry saved successfully!") #message box successful

            self.lineEdit_Date.setText("")      #resets all text boxes back empty  once entry saved
            self.lineEdit_Total_tips_earned.setText("")
            self.lineEdit_Valets_on_duty.setText("")
            self.lineEdit_Duration.setText("")
            self.lineEdit_Cars_parked.setText("")
            self.lineEdit_TBD_1.setText("")
            self.lineEdit_TBD_2.setText("")

            self.tabWidget.setCurrentIndex(0) #changes the page back to the home page


        except con.Error as err: #all error messages
            QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
            print(f"SQL Error: {err}")
        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {ve}")
            print(f"Input Error: {ve}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            print(f"Error details: {e}")

    def show_calc_data(self): #show calc data page
        self.tabWidget.setCurrentIndex(2) #page position
        self.calc_data_tips() #calls method below


    def calc_data_tips(self): #calculate the total tips in the database and display it in the box 
        try:
            mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
            cursor = mydb.cursor() #set curser
            #need to when the function is called it calls the query from the table and btn.setText(data)
            qry = "SELECT SUM(Total_tips_earned) AS Total_Tips FROM entries;"
            cursor.execute(qry)
            # Fetch the query result
            result = cursor.fetchone()  # Fetch the first result row

            # Handle case where the result is None or NULL (e.g., no data in the table)
            total_tips = result[0] if result and result[0] is not None else 0
        
            # Convert Decimal to float or int, then to string for displaying
            total_tips_str = str(total_tips)  # Convert to string for setText
        
            # Set the result in the line edit widget
            self.textBrowser_Total_Tips_recieved.setText(total_tips_str)
        except con.Error as err:
            QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

