import mysql.connector as con
from PyQt5.QtWidgets import QMessageBox

def save_entry_funct(self): #function to save the entry when the button is hit on the new entry page
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor()
            # Retrieve input from the user interface in all text input boxes
        date= self.lineEdit_Date.text()
        Total_tips_earned= self.lineEdit_Total_tips_earned.text()
        workers_on_duty= self. lineEdit_workers.text()
        duration= self.lineEdit_Duration.text()
        customers= self.lineEdit_customers.text()

        #makes sure the user filled out the required fields
        if not date or not Total_tips_earned or not workers_on_duty or not duration: 
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
            return
            
            # SQL query for inserting data
        query = """
        INSERT INTO entries (date, Total_tips_earned, workers_on_duty, duration, customers)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (date, Total_tips_earned, workers_on_duty, duration, customers)

            # Execute the query
        cursor.execute(query, values)
        mydb.commit()  # Commit the transaction
            
        QMessageBox.information(self, "Success", "Entry saved successfully!") #message box successful

        self.lineEdit_Date.setText("")      #resets all text boxes back empty once entry saved
        self.lineEdit_Total_tips_earned.setText("")
        self. lineEdit_workers.setText("")
        self.lineEdit_Duration.setText("")
        self.lineEdit_customers.setText("")   

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
        qry = "SELECT SUM(Total_tips_earned) AS Total_Tips FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        total_tips = result[0] if result and result[0] is not None else 0

        #return
        return total_tips

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")

def calc_avg_tips(): #calculate the average tips in the database
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        qry = "SELECT ROUND(AVG(Total_tips_earned), 2) AS Average_Tips_Per_Entry FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        avg_tips = result[0] if result and result[0] is not None else 0

        #return
        return avg_tips

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_tips_per_hr(): #calculate the total tips per hour f
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        qry = "SELECT ROUND(SUM(Total_tips_earned) / SUM(duration), 2) AS Average_Tips_Per_Hour FROM entries"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        tips_per_hr = result[0] if result and result[0] is not None else 0

        #return
        return tips_per_hr

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_total_hours_worked(): #calculate the total duration worked
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        qry = "SELECT SUM(duration) AS Duration FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        duration = result[0] if result and result[0] is not None else 0

        #return
        return duration

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")
    
def calc_customers(): #calculate the total cars parked
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        qry = "SELECT SUM(customers) AS customers FROM entries;"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        customers = result[0] if result and result[0] is not None else 0

        #return
        return customers

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")

def calc_customers_per_hour():
    try:
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        qry = "SELECT ROUND(SUM(customers) / SUM(duration), 2) AS customers_per_hour FROM entries"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchone()  # Fetch the first result row

        # Handle case where the result is None
        customers_per_hour = result[0] if result and result[0] is not None else 0

        #return
        return customers_per_hour

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")


def display_raw_data(): #displays the raw data from the table
    try:
        # Connect to the SQL database
        mydb = con.connect(host="localhost", user="root", password="", db="valettracker")
        cursor = mydb.cursor()
    
        # Define the query to fetch all rows
        qry = "SELECT id, date, Total_tips_earned, workers_on_duty, duration, customers FROM entries"
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
                f"Workers on Duty: {row[3]}\n"
                f"Duration: {row[4]}\n"
                f"Customers: {row[5]}\n"
                f"{'-' * 30}\n"  # Separator between rows
            )
        
        # Return the formatted output
        return formatted_result

    except con.Error as err:
        # Handle database connection errors
        return f"Database Error: {err}"

def delete_entry(self): #delete a specific entry given by the user in the lineEdit_delete-id box
    try:
     # Get the ID entered by the user in the lineEdit_delete_id field
        entry_id = self.lineEdit_delete_id.text().strip()

                # Validate that the input is not empty and is a valid integer
        if not entry_id.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid numeric ID.")
                    
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
    
def clear_entries(self):    #clears all of the data and trunicates the table. gives a warning box to the user before performing the actions
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
