from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

interfaces = []
filePath = []

@app.route('/interfaces', methods=['POST'])
def getInterfaces():
    global interfaces
    interfaces = request.json["interfaces"]
    return interfaces

@app.route('/filePath', methods=['POST'])
def getFilePath():
    filePath = request.json["filePath"]
    print(filePath)
    print('Absolute path of file:     ',
      os.path.abspath(filePath))
    return filePath
    
def getInput():
    if(len(interfaces) > 0):
        return "YES"
    else:
        return "NO"

@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    if getInput() == "YES":
        return "SUCCESS"
    else:
        return "FAILED"