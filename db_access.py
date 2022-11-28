# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:12:58 2022

@author: SYA6COB
"""

import pyodbc

# from cmd_write_line import sendFileData

import time
import sys
import win32pipe
import win32file
import pywintypes
import os, errno


conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\DUMA1KOR\Downloads\Database3.accdb;')
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

# resp = []



# def pipe_client():
#     print("pipe client")
#     quit = False
#     output = []
#     while not quit:
#         try:
#             handle = win32file.CreateFile(
#                 r'\\.\pipe\Foo',
#                 win32file.GENERIC_READ | win32file.GENERIC_WRITE,
#                 0,
#                 None,
#                 win32file.OPEN_EXISTING,
#                 0,
#                 None
#             )
#             res = win32pipe.SetNamedPipeHandleState(
#                 handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
#             if res == 0:
#                 print(f"SetNamedPipeHandleState return code: {res}")
#             while True:
#                 resp = win32file.ReadFile(handle, 64*1024)
#                 # print(resp,"\n")
#                 # print(f"message: {resp}\n")
#                 # resp=str(resp, 'utf-8')
#                 output.append(resp)


                

#         except pywintypes.error as e:
#             if e.args[0] == 2:
#                 print("no pipe, trying again in a sec")
#                 time.sleep(1)
#             elif e.args[0] == 109:
#                 print("broken pipe, bye bye")
#                 quit = True

#     output=str(output)
#     substring = "0, b"
#     output_string = ""
#     str_list = output.split(substring)
#     for element in str_list:
#         output_string += element
#     return output_string

FIFO = "mypipe"

def pipe_client():
    print("pipe client")
    quit = False
    output = []
    while not quit:
        try:
            handle = win32file.CreateFile(
                r'\\.\pipe\Foo',
                win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                0,
                None,
                win32file.OPEN_EXISTING,
                0,
                None
            )
            res = win32pipe.SetNamedPipeHandleState(
                handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
            if res == 0:
                print(f"SetNamedPipeHandleState return code: {res}")
            while True:
                resp = win32file.ReadFile(handle, 64*1024)
                # print(resp,"\n")
                # print(f"message: {resp}\n")
                # resp=str(resp, 'utf-8')
                output.append(resp)


                

        except pywintypes.error as e:
            if e.args[0] == 2:
                print("no pipe, trying again in a sec")
                time.sleep(1)
            elif e.args[0] == 109:
                print("broken pipe, bye bye")
                quit = True

    output=str(output)
    substring = "0, b"
    output_string = ""
    str_list = output.split(substring)
    for element in str_list:
        output_string += element
    return output_string

## <--- LINUX READ FILE FIFO --->

    # try:
    #     os.mkfifo(FIFO)
    # except OSError as oe:
    #     if oe.errno != errno.EEXIST:
    #         raise

    # while True:
    #     print("Opening FIFO...")
    #     with open(FIFO) as fifo:
    #         print("FIFO opened")
    #         while True:
    #             data = fifo.read()
    #             if len(data) == 0:
    #                 print("Writer closed")
    #                 break
    #             print('Read: "{0}"'.format(data))


def main():
    print("Hello World")
    new_list = []
    record = fetch_data_from_db()

    for i in record:
        if i != None:
            new_list.append(i)

    # f_path =get_template_path()
    print("Path returned by Front End is ", pipe_client())

    print("Value Fetched from the DB is :", new_list)
    print("Value Fetched from the DB Len is :", len(new_list))


if __name__ == "__main__":
    main()
