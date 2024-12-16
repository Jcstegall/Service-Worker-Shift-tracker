import mysql.connector as con

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
        mydb = con.connect(host = "localhost", user = "root",password = "", db = "valettracker") #Connects to sql database
        cursor = mydb.cursor() #set curser
        #need to when the function is called it calls the query from the table
        qry = "SELECT * FROM entries"
        cursor.execute(qry)
        # Fetch the query result
        result = cursor.fetchall()  # Fetch the first result row

        # Handle case where the result is None or NULL (e.g., no data in the table)
        #raw_data = result[0] if result and result[0] is not None else 0

        #return
        return result

    except con.Error as err:
        QMessageBox.critical(self, "Database Error", f"Could not save entry: {err}")


