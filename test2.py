# import mysql.connector
# import pandas as pd
# import numpy as np

# # Connect to the MySQL database
# cnx = mysql.connector.connect(user='root', password='190030424',
#                               host='localhost', database='tara', port=3306)
# cursor = cnx.cursor()

# # Query the database and retrieve the data
# query = "SELECT * from ble union all select * from usb"
# cursor.execute(query)
# data = cursor.fetchall()

# # Convert the data to a Pandas DataFrame
# df = pd.DataFrame(data)
# column_names = [i[0] for i in cursor.description]
# df.astype(str)
# df.replace(['0'], '', inplace=True)
# df.columns = column_names
# # Write the DataFrame to an .xlsm file
# print(df)
# df.to_excel('usb.xlsx', engine='openpyxl', index=False)
# # print(df)
# # Close the cursor and connection
# cursor.close()
# cnx.close()

# lst=["usb","ble", "mqtt"]

# str=""

# for i in range(0,len(lst)):

#     if i==0:

#         str=f"select * from {lst[i]}"

#     else:

#         str=str+f" union all select * from {lst[i]}"

# print(str)#

# import os

# folder_name = "C:\\path\\to\\new_folder"

# try:
#     os.mkdir(folder_name)
#     print("Folder created successfully")
# except OSError:
#     print("An error occurred while creating the folder")
