import mysql.connector as con
from PyQt5.QtWidgets import QMessageBox


def save_entry_funct(self): #function to save the entry when the button is hit on the new entry page
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor()
            # Retrieve input from the user interface in all text input boxes
        date= self.lineEdit_Date.text()
        Total_tips_earned= self.lineEdit_Total_tips_earned.text()
        valets_on_duty= self.lineEdit_Valets_on_duty.text()
        duration= self.lineEdit_Duration.text()
        cars_parked= self.lineEdit_Cars_parked.text()

            # SQL query for inserting data
        query = """
        INSERT INTO entries (date, Total_tips_earned, valets_on_duty, duration, cars_parked)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (date, Total_tips_earned, valets_on_duty, duration, cars_parked)

            # Execute the query
        cursor.execute(query, values)
        mydb.commit()  # Commit the transaction
            
        QMessageBox.information(self, "Success", "Entry saved successfully!") #message box successful

        self.lineEdit_Date.setText("")      #resets all text boxes back empty  once entry saved
        self.lineEdit_Total_tips_earned.setText("")
        self.lineEdit_Valets_on_duty.setText("")
        self.lineEdit_Duration.setText("")
        self.lineEdit_Cars_parked.setText("")   

    except con.Error as err: #all error messages
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
        print(f"SQL Error: {err}")
    except ValueError as ve:
        QMessageBox.critical(self, "Input Error", f"Invalid input: {ve}")
        print(f"Input Error: {ve}")
    except Exception as e:
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
        print(f"Error details: {e}")

def calc_data_tips(): #calculate the total tips in the database
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

        #return
        return total_tips

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")

def calc_avg_tips(): #calculate the average tips in the database
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table and btn.setText(data)
        qry = "SELECT ROUND(AVG(Total_tips_earned), 2) AS Average_Tips_Per_Entry FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        avg_tips = result[0] if result and result[0] is not None else 0

        #return
        return avg_tips

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_tips_per_hr(): #calculate the total tips per hour f
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table
        qry = "SELECT ROUND(SUM(Total_tips_earned) / SUM(duration), 2) AS Average_Tips_Per_Hour FROM entries"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        tips_per_hr = result[0] if result and result[0] is not None else 0

        #return
        return tips_per_hr

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_total_hours_worked(): #calculate the total duration worked
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table
        qry = "SELECT SUM(duration) AS Duration FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        duration = result[0] if result and result[0] is not None else 0

        #return
        return duration

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_cars_parked(): #calculate the total cars parked
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table
        qry = "SELECT SUM(cars_parked) AS cars_parked FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        cars_parked = result[0] if result and result[0] is not None else 0

        #return
        return cars_parked

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")

def calc_cars_per_hour():
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table
        qry = "SELECT ROUND(SUM(cars_parked) / SUM(duration), 2) AS cars_parked_per_hour FROM entries"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        cars_parked_per_hour = result[0] if result and result[0] is not None else 0

        #return
        return cars_parked_per_hour

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")

#function to show the raw data in a big text browser 
#display the entry id and have a text window with a button to delete the entry
#make sure that button resets the page so it updates the query in real time
def display_raw_data():
    try:
        # Connect to the SQL database
        mydb = con.connect(host="localhost", user="root", password="", db="valettracker")
        cursor = mydb.cursor()
        
        # Define the query to fetch all rows
        qry = "SELECT id, date, Total_tips_earned, valets_on_duty, duration, cars_parked FROM entries"
        cursor.execute(qry)
        
        # Fetch all results
        result = cursor.fetchall()
        
        # Check if there are results
        if not result:
            return "No data found in the table."
        
        # Format the output
        formatted_result = ""
        for row in result:
            formatted_result += (
                f"ID: {row[0]}\n"
                f"Date: {row[1]}\n"
                f"Total Tips Earned: {row[2]}\n"
                f"Valets on Duty: {row[3]}\n"
                f"Duration: {row[4]}\n"
                f"Cars Parked: {row[5]}\n"
                f"{'-' * 30}\n"  # Separator between rows
            )
        
        # Return the formatted output
        return formatted_result

    except con.Error as err:
        # Handle database connection errors
        return f"Database Error: {err}"

#this function needs to call self because it needs the input from lineEdit_delete_id 
def delete_entry(self):
    try:
     # Get the ID entered by the user in the lineEdit_delete_id field
        entry_id = self.lineEdit_delete_id.text().strip()

                # Validate that the input is not empty and is a valid integer
        if not entry_id.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid numeric ID.")
                    

                # Convert to integer (safe because of isdigit check)
            #entry_id = int(entry_id)

                # Connect to the database
        mydb = con.connect(host="localhost", user="root", password="", db="valettracker")
        cursor = mydb.cursor()

                # Execute the DELETE query
        qry = "DELETE FROM entries WHERE id = %s"
        cursor.execute(qry, (entry_id,))
        mydb.commit()  # Commit the transaction
        self.lineEdit_delete_id.setText(str("")) #reset the space in the delete edit box empty

    except con.Error as err:
                # Handle database connection errors
        print( f"Database Error: {err}")
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
    
    #clears all of the data and trunicates the table. gives a warning box to the user before perfomring the actions
def clear_entries(self):
    try:
            # Connect to the database
        mydb = con.connect(host="localhost", user="root", password="", db="valettracker")
        cursor = mydb.cursor()
        #warning box parameters 
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("Warning")
        warning.setText("Are you sure you want to delete all data?")
        warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = warning.exec_()

        if response == QMessageBox.Yes: #if the user hits yes execute query to delete data
            qry = "TRUNCATE TABLE entries;"
            cursor.execute(qry)
            mydb.commit()  # Commit the transaction

    except con.Error as err:
        # Handle database connection errors
        print( f"Database Error: {err}")
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
