# # import mysql.connector
# # import pandas as pd
# # import numpy as np

# # # Connect to the MySQL database
# # cnx = mysql.connector.connect(user='root', password='190030424',
# #                               host='localhost', database='tara', port=3306)
# # cursor = cnx.cursor()

# # # Query the database and retrieve the data
# # query = "SELECT * from ble union all select * from usb"
# # cursor.execute(query)
# # data = cursor.fetchall()

# # # Convert the data to a Pandas DataFrame
# # df = pd.DataFrame(data)
# # column_names = [i[0] for i in cursor.description]
# # df.astype(str)
# # df.replace(['0'], '', inplace=True)
# # df.columns = column_names
# # # Write the DataFrame to an .xlsm file
# # print(df)
# # df.to_excel('usb.xlsx', engine='openpyxl', index=False)
# # # print(df)
# # # Close the cursor and connection
# # cursor.close()
# # cnx.close()

# # lst=["usb","ble", "mqtt"]

# # str=""

# # for i in range(0,len(lst)):

# #     if i==0:

# #         str=f"select * from {lst[i]}"

# #     else:

# #         str=str+f" union all select * from {lst[i]}"

# # print(str)#

# # import os

# # folder_name = "C:\\path\\to\\new_folder"

# # try:
# #     os.mkdir(folder_name)
# #     print("Folder created successfully")
# # except OSError:
# #     print("An error occurred while creating the folder")
# import pandas as pd

# import numpy as np
# df = pd.read_csv('C:\\Users\\DUMA1KOR\\Desktop\\Codes\React\\Master-TARA-API\\output.csv')
# mask = (df != 0) & (df != '0')
# df = df[mask.all(axis=1)]
# print(df)

# import pandas as pd

# # create a sample dataframe
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

# # create a sample dictionary
# d = {'x': 'a', 'y': 'b', 'z': 'd'}

# # extract the values of the dictionary that match any column names of the dataframe
# matching_values = [val for val in d.values() if val in df.columns]

# if len(matching_values) > 0:
#     print(f"Matching Values {matching_values[0], matching_values[1]}")
# else:
#     print("No values in the dictionary match any column names in the dataframe.")

# import mysql.connector
# import pandas as pd
# import openpyxl

# cnx = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="190030424",
#     database="tara"
# )

# cursor = cnx.cursor()
# query = "SELECT * FROM wifi union all select * from jtag"
# cursor.execute(query)
# rows = cursor.fetchall()
# df = pd.DataFrame(rows)
# mask = (df != '') & (df != ' ')
# df = df[mask.all(axis=1)]
# # df.dropna(subset=[0], axis=0, inplace=True)
# # df.reset_index(drop=True, inplace=True)
# print(df)
# # df.update(df[::-1].fillna(method='bfill')[::-1])
# # def fill_null(col):
# #     col = col.dropna()
# #     col = col.str.cat(sep=' ')
# #     return col

# # df = df.apply(fill_null)
# df.to_excel("output.xlsx", index=False)

# cursor.close()
# cnx.close()

# import pandas as pd
# import numpy as np

# data = {'A': [1, 2, np.nan, 4, 5],
#         'B': [6, 7, 8, np.nan, 10],
#         'C': [11, np.nan, 13, 14, 15]}

# df = pd.DataFrame(data)
# df.fillna(method='bfill', inplace=True)

# df.to_excel("output.xlsx", index=False)
# print(df)

# import openpyxl

# # Open the source workbook
# source_wb = openpyxl.load_workbook(
#     filename='C:\\Users\\DUMA1KOR\\Documents\\master.xlsm', keep_vba=True)

# # Open the target workbook
# target_wb = openpyxl.Workbook()

# # Loop through the sheets in the source workbook
# for source_sheet in source_wb:
#     # Copy the sheet to the target workbook
#     target_sheet = target_wb.create_sheet(title=source_sheet.title)

#     # Loop through the rows and columns in the source sheet
#     for row in source_sheet.iter_rows():
#         for cell in row:
#             # Copy the cell value and style to the target sheet
#             target_sheet[cell.coordinate].value = cell.value
#             target_sheet[cell.coordinate].style = cell.style

#     # Copy the images in the source sheet to the target sheet
#     for img in source_sheet._images:
#         target_sheet._images.append(img)

# # Save the target workbook
# target_wb.save(filename='target.xlsm')

# import openpyxl

# # Open the source workbook
# source_wb = openpyxl.load_workbook(
#     filename='C:\\Users\\DUMA1KOR\\Documents\\master.xlsm', keep_vba=True)

# # Open the target workbook
# target_wb = openpyxl.Workbook()

# # Loop through the first 4 sheets in the source workbook
# for source_sheet in source_wb.worksheets[:4]:
#     # Copy the sheet to the target workbook
#     target_sheet = target_wb.create_sheet(title=source_sheet.title)

#     # Loop through the rows and columns in the source sheet
#     for row in source_sheet.iter_rows():
#         for cell in row:
#             # Copy the cell value and style to the target sheet
#             target_sheet[cell.coordinate].value = cell.value
#             # target_sheet[cell.coordinate].style = cell.style

# # Save the target workbook
# target_wb.save(filename='C:\\Users\\DUMA1KOR\\Documents\\target.xlsm')

# import xlwings as xw

# # def delete_sheets(file_path: str):
# wb = xw.Book('C:\\Users\\DUMA1KOR\\Downloads\\TRA_and_RRA_Template_v2.3.2  (1).xlsm')
# sheets_to_delete = ["About", "Methodology", "TechDescription", "Scope"]
# for sheet_name in sheets_to_delete:
#     if sheet_name in [sheet.name for sheet in wb.sheets]:
#         wb.sheets[sheet_name].delete()
# wb.save()
# wb.close()

# import openpyxl

# # Load the workbook
# wb = openpyxl.load_workbook("C:\\Users\\DUMA1KOR\\Downloads\\TRA_and_RRA_Template_v2.3.2.xlsm")

# # List of sheet names to delete
# sheets_to_delete = ["About", "Methodology", "TechDescription", "Scope"]

# # Iterate through all sheets
# for sheet_name in wb.sheetnames:
#     # Check if the sheet name is in the list of sheets to delete
#     if sheet_name in sheets_to_delete:
#         # Remove the sheet
#         wb.remove(wb[sheet_name])

# # Save the changes
# wb.save()


# import win32com.client as win32

# # Load the excel application
# excel = win32.gencache.EnsureDispatch("Excel.Application")

# # Load the workbook
# wb = excel.Workbooks.Open("C:\\Users\\DUMA1KOR\\Downloads\\TRA_and_RRA_Template_v2.3.2.xlsm")

# # Array of sheet names to delete
# sheets_to_delete = ["About", "Methodology", "TechDescription", "Scope"]

# # Iterate through the array of sheet names
# for sheet_name in sheets_to_delete:
#     # Check if the sheet exists in the workbook
#     if sheet_name in [sheet.Name for sheet in wb.Sheets]:
#         # Remove the sheet from the workbook
#         wb.Sheets(sheet_name).Delete()

# # Save the changes to the excel file
# wb.Save()

# # Close the excel application
# excel.Quit()

import pandas as pd

# Load the excel file as a pandas dataframe
df = pd.read_excel("C:\\Users\\DUMA1KOR\\Downloads\\TRA_and_RRA_Template_v2.3.2.xlsm", sheet_name=None)

# Array of sheet names to delete
sheets_to_delete = ["About", "Methodology", "TechDescription", "Scope"]

# Iterate through the array of sheet names
for sheet_name in sheets_to_delete:
    # Check if the sheet exists in the dataframe
    if sheet_name in df:
        # Remove the sheet from the dataframe
        df.pop(sheet_name)

# Save the changes to the excel file
with pd.ExcelWriter("C:\\Users\\DUMA1KOR\\Downloads\\TRA_and_RRA_Template_v2.3.2.xlsm") as writer:
    for sheet_name, sheet_data in df.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
