from flask import Flask, request
from flask_cors import CORS
import win32pipe
import win32file
import time
import os
from subprocess import Popen


app = Flask(__name__)
CORS(app)

interfaces = []
filePath = []
absPath = []
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
    abs.append(os.path.abspath(filePath))
    return os.path.abspath(filePath)


def sendFilePath():
    
    return abs


def getInput():
    if (len(interfaces) > 0):
        return "YES"
    else:
        return "NO"


@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    # main()
    if getInput() == "YES":
        return "SUCCESS"
    else:
        return "FAILED"



if __name__ == '__main__':
    app.run(debug=True)
