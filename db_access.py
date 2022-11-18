# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:12:58 2022

@author: SYA6COB
"""

import pyodbc

from index import sendFilePath



conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\DUMA1KOR\Downloads\Database3.accdb;')
cursor = conn.cursor()
# cursor.execute('select * from Sheet1 where col_name=Field1')
cursor.execute('select Field1 from Sheet3')

db_list = [] 


def fetch_data_from_db():
    records = cursor.fetchall()
    for record in records:
        db_list.append(record[0])
    #     if(record[0].Value=="None"):
    #         db_list.append(record[0])
    #         print("Hello World")
    return db_list


def get_template_path():
    fs = open(r'C:\Users\DUMA1KOR\Desktop\Codes\React\Master-TARA-Creator-main\flask\FilePath.txt','r')
    con = fs.read()
    print(con + '\n')
    fs.close()
    return con


def main():
    print("Hello World")
    new_list = []
    record = fetch_data_from_db()

    for i in record:
        if i != None:
            new_list.append(i)
            
    # f_path =get_template_path()
    print ("Path returned by Front End is ",get_template_path())
        
    

    print ("Value Fetched from the DB is :",new_list)
    print ("Value Fetched from the DB Len is :",len(new_list))



if __name__ == "__main__":
    main()
