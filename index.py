from flask import Flask, request
from flask_cors import CORS
import win32pipe
import win32file
import time
import os
import pyodbc
from subprocess import Popen


app = Flask(__name__)
CORS(app)

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



interfaces = []
filePath = []
absPath = []
# pipe = ""
abs = []


def runAnotherFile():
    Popen('python db_access.py')


@app.route('/interfaces', methods=['POST'])
def getInterfaces():
    global interfaces
    interfaces = request.json["interfaces"]
    print("pipe interfaces")
    runAnotherFile()
    pipe = win32pipe.CreateNamedPipe(
        r'\\.\pipe\Foo',
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,
        0,
        None)
    try:
        print("waiting for client")
        win32pipe.ConnectNamedPipe(pipe, None)
        print("got client")

        win32file.WriteFile(pipe, str.encode(f"{interfaces}"))
        time.sleep(2)
        win32file.WriteFile(pipe, str.encode(f"{sendFilePath()}"))
        abs.clear()
        # print(sendFilePath())
        print("finished now")
    finally:
        win32file.CloseHandle(pipe)
    return interfaces


@app.route('/filePath', methods=['POST'])
def getFilePath():
    global filePath
    global abs
    filePath = request.json["filePath"]
    # print(filePath)
    # print("file executed",os.path.abspath(filePath))
    abs.append(os.path.abspath(filePath))
    return os.path.abspath(filePath)


def sendFilePath():
    # global abs
    # abs.append(os.path.abspath(filePath))
    # print("got abs path", abs)
    return abs


def getInput():
    if (len(interfaces) > 0):
        return "YES"
    else:
        return "NO"


@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    print("interfaces are", interfaces)
    # main()
    if getInput() == "YES":
        return "SUCCESS"
    else:
        return "FAILED"


def main():
    print("Hello World")
    new_list = []
    record = fetch_data_from_db()

    for i in record:
        if i != None:
            new_list.append(i)

    print("selected interfaces are", getInterfaces())
    # f_path =get_template_path()
    print("Path returned by Front End is ", sendFilePath())

    # print("Value Fetched from the DB is :", new_list)
    print("Value Fetched from the DB Len is :", len(new_list))


if __name__ == '__main__':
    app.run(debug=True)
