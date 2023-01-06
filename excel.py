# Import necessary libraries
import mysql.connector
import pandas as pd

def main():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",  # Replace with your hostname
        user="root",  # Replace with your MySQL username
        password="190030424",  # Replace with your MySQL password
        database="tara"  # Replace with the name of your database
    )

    # Create a cursor for executing queries
    cursor = db.cursor()

    # Define the query to get the data from the "usb" table
    query = "SELECT * FROM usb"

    # Execute the query and get the data
    cursor.execute(query)
    data = cursor.fetchall()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame as an Excel file with macros
    df.to_excel("usb_data.xlsm", engine="openpyxl", index=False,
                freeze_panes=(1,1),
                macros={"my_macro": "This is a sample macro"})

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
