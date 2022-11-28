from flask_socketio import *
from flask import Flask
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('interfaces')
@cross_origin()
def interfaces(interfaces):
    # socketio.emit("chat", data)
    print("interfaces",interfaces)
    socketio.emit("checkStatus", "SUCCESS")
    return interfaces

@socketio.on('filepath')
@cross_origin()
def filepath(filepath):
    # socketio.emit("chat", data)
    abspath = os.path.abspath(filepath)
    print("filepath",abspath)
    return abspath

# @socketio.on('checkStatus')
# @cross_origin()
# def checkStatus(status):
#     socketio.emit("status", "yes")
#     print("status",status)
#     return status

if __name__ == '__main__':
    socketio.run(app, debug=True)

