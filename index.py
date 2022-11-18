from flask import Flask, request, make_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

interfaces = []
fileName = []
filePath = []
absPath = []
resp = []

@app.route('/interfaces', methods=['POST'])
def getInterfaces():
    global interfaces
    interfaces = request.json["interfaces"]
    return interfaces

@app.route('/filePath', methods=['POST'])
def getFilePath():
    global filePath
    global resp
    fileName = request.json["filePath"]
    # print(fileName)
    filePath = os.path.abspath(fileName)
    sendFilePath()
    resp = make_response(filePath)
    return filePath

def sendFilePath():
    absPath = filePath
    print("got abs path", absPath)
    # open(r'C:\Users\DUMA1KOR\Desktop\Codes\React\Master-TARA-Creator-main\flask\FilePath.txt', 'w').close()
    with open(r'C:\Users\DUMA1KOR\Desktop\Codes\React\Master-TARA-Creator-main\flask\FilePath.txt', 'a') as f:
        f.writelines(absPath+'\n')
    return absPath
    
def getInput():
    if(len(interfaces) > 0):
        return "YES"
    else:
        return "NO"

@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    if getInput() == "YES":
        print(filePath)
        return "SUCCESS"
    else:
        return "FAILED"