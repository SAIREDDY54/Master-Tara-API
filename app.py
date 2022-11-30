from flask_socketio import *
from flask import Flask
from flask_cors import CORS, cross_origin
import os
import eventlet
import socketio

app = Flask(__name__)
CORS(app)
eventlet.monkey_patch()
sio = SocketIO(app, cors_allowed_origins='http://localhost:3000', async_mode="threading")
# sio = socketio.Server()


@sio.event
def interfaces(interfaces):
    # socketio.emit("chat", data)
    print("interfaces",interfaces)
    sio.emit("checkStatus", "SUCCESS")
    return interfaces

# @sio.event
# def filepath(filepath):
#     # socketio.emit("chat", data)
#     abspath = os.path.abspath(filepath)
#     print("filepath",abspath)
#     return abspath

# @sio.event
# def checkStatus():
#     status = "SUCCESS"
#     sio.emit('checkStatus', {'result': status})
#     print("emitted")
# @socketio.on('checkStatus')
# @cross_origin()
# def checkStatus(status):
#     socketio.emit("status", "yes")
#     print("status",status)
#     return status

if __name__ == '__main__':
    sio.run(app, debug=True)

